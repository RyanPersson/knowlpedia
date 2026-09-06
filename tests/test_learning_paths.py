import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location('learning_paths', Path(__file__).parents[1] / 'scripts/check_learning_paths.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class LearningPathTests(unittest.TestCase):
    def contract(self):
        return {'reviews': [{'id': 'basic', 'review_count_before': 0}],
                'learning_paths': [{'name': 'Foundations to result', 'concepts': ['basic', 'result']}],
                'forbidden_prerequisite_ancestors': {'basic': ['advanced']}}

    def test_accepts_transitive_path_and_reports_unreviewed_side_inputs(self):
        graph = {'basic': [], 'middle': ['basic'], 'side': [], 'result': ['middle', 'side']}
        result = checker.check_contract(graph, {'basic': 1, 'middle': 1}, self.contract())
        self.assertTrue(result['ok'])
        self.assertEqual(result['paths'][0]['prerequisite_count'], 3)
        self.assertEqual(result['paths'][0]['unreviewed_prerequisite_count'], 1)

    def test_disconnected_path_fails_even_when_graph_is_acyclic(self):
        result = checker.check_contract({'basic': [], 'result': []}, {'basic': 1}, self.contract())
        self.assertFalse(result['ok'])
        self.assertTrue(any('no prerequisite path' in message for message in result['errors']))

    def test_forbidden_transitive_ancestor_fails_without_a_cycle(self):
        graph = {'advanced': [], 'middle': ['advanced'], 'basic': ['middle'], 'result': ['basic']}
        result = checker.check_contract(graph, {'basic': 1}, self.contract())
        self.assertFalse(result['ok'])
        self.assertIn('basic: advanced dependency reintroduced: advanced', result['errors'])

    def test_cycle_and_missing_target_and_unrecorded_review_fail(self):
        graph = {'basic': ['result'], 'result': ['basic', 'missing']}
        result = checker.check_contract(graph, {}, self.contract())
        self.assertFalse(result['ok'])
        self.assertTrue(any('cyclic' in message for message in result['errors']))
        self.assertTrue(any('missing prerequisite' in message for message in result['errors']))
        self.assertTrue(any('completed review' in message for message in result['errors']))

    def test_missing_exclusion_target_fails(self):
        contract = self.contract()
        contract['forbidden_prerequisite_ancestors'] = {'absent': ['advanced']}
        result = checker.check_contract({'basic': [], 'result': ['basic']}, {'basic': 1}, contract)
        self.assertFalse(result['ok'])
        self.assertTrue(any('target is missing' in message for message in result['errors']))

    def test_fully_reviewed_path_rejects_new_unreviewed_side_dependency(self):
        contract = self.contract()
        contract['learning_paths'][0]['max_unreviewed_prerequisites'] = 0
        graph = {'basic': [], 'side': [], 'result': ['basic', 'side']}
        result = checker.check_contract(graph, {'basic': 1, 'result': 1}, contract)
        self.assertFalse(result['ok'])
        self.assertEqual(result['paths'][0]['unreviewed_prerequisites'], ['side'])
        self.assertTrue(checker.check_contract(graph, dict.fromkeys(graph, 1), contract)['ok'])

    def test_empty_path_is_reported_as_error(self):
        contract = self.contract()
        contract['learning_paths'][0]['concepts'] = []
        result = checker.check_contract({'basic': []}, {'basic': 1}, contract)
        self.assertFalse(result['ok'])
        self.assertIn('Foundations to result: learning path is empty', result['errors'])

    def test_full_review_rejects_any_new_unreviewed_node(self):
        contract = self.contract()
        contract['require_full_review'] = True
        graph = {'basic': [], 'result': ['basic'], 'new': []}
        result = checker.check_contract(graph, {'basic': 1, 'result': 1}, contract)
        self.assertFalse(result['ok'])
        self.assertTrue(any('unreviewed concepts remain' in e for e in result['errors']))

    def test_latest_review_detects_after_list_drift(self):
        contract = self.contract()
        contract['reviews'][0]['after'] = []
        result = checker.check_contract({'basic': ['result'], 'result': []},
                                        {'basic': 1, 'result': 1}, contract)
        self.assertFalse(result['ok'])
        self.assertTrue(any('latest review prerequisite list drifted' in e for e in result['errors']))

    def test_merge_uses_re_review_with_higher_before_count(self):
        old = {'reviews': [{'id': 'basic', 'review_count_before': 0, 'after': []}]}
        new = {'reviews': [{'id': 'basic', 'review_count_before': 1, 'after': ['middle']}]}
        merged = checker.merge_contracts([old, new])
        self.assertEqual(merged['reviews'], new['reviews'])

    def test_merge_preserves_old_paths_exclusions_and_latest_review(self):
        old = self.contract()
        new = {'reviews': [{'id': 'basic', 'review_count_before': 2}],
               'forbidden_prerequisite_ancestors': {'basic': ['other']}}
        merged = checker.merge_contracts([new, old])
        self.assertEqual(merged['reviews'], new['reviews'])
        self.assertEqual(merged['learning_paths'], old['learning_paths'])
        self.assertEqual(merged['forbidden_prerequisite_ancestors']['basic'], {'advanced', 'other'})

    def test_coverage_distinguishes_reviewed_nodes_from_reviewed_closures(self):
        graph = {'a/basic': [], 'a/side': [], 'b/result': ['a/basic', 'a/side'], 'b/other': ['a/side']}
        result = checker.review_coverage(graph, {'a/basic': 1, 'b/result': 1})
        self.assertEqual(result['reviewed_concepts'], 2)
        self.assertEqual(result['reviewed_with_all_prerequisites_reviewed'], 1)
        self.assertEqual(result['by_domain']['a'], {'total': 2, 'reviewed': 1})
        self.assertEqual(result['next_candidates'][0], {'id': 'a/side', 'direct_dependents': 2, 'reviewed_direct_dependents': 1})


if __name__ == '__main__':
    unittest.main()
