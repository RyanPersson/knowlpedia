import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location('check_reading_order', Path(__file__).parents[1] / 'scripts/check_reading_order.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ReadingOrderTests(unittest.TestCase):
    graph = {'set': [], 'ring': ['set'], 'module': ['ring'], 'submodule': ['module', 'set'], 'quotient': ['submodule']}

    def test_accepts_prerequisite_order_and_reports_entry_assumptions(self):
        result = checker.check_reading_order(self.graph, ['ring', 'module', 'submodule', 'quotient'])
        self.assertTrue(result['ok'])
        self.assertEqual(result['linked'], 4)
        self.assertEqual(result['entry_assumptions'], {'set': ['ring', 'submodule']})

    def test_rejects_transitive_prerequisite_placed_later(self):
        result = checker.check_reading_order(self.graph, ['quotient', 'module'])
        self.assertFalse(result['ok'])
        self.assertEqual(result['violations'], [
            {'knowl': 'quotient', 'prerequisite': 'module', 'position': 0, 'prerequisite_position': 1}])

    def test_reports_repeated_and_missing_links(self):
        result = checker.check_reading_order(self.graph, ['ring', 'unknown', 'ring'])
        self.assertTrue(result['ok'])
        self.assertEqual(result['repeated'], ['ring'])
        self.assertEqual(result['missing'], ['unknown'])

    def test_suggested_order_keeps_valid_pages_and_repairs_invalid_ones(self):
        valid = ['ring', 'module', 'submodule', 'quotient']
        self.assertEqual(checker.suggested_order(self.graph, valid), valid)
        self.assertEqual(checker.suggested_order(self.graph, ['quotient', 'ring', 'module']), ['ring', 'module', 'quotient'])

    def test_suggested_order_is_none_for_cycles(self):
        self.assertIsNone(checker.suggested_order({'a': ['b'], 'b': ['a']}, ['a', 'b']))


if __name__ == '__main__':
    unittest.main()
