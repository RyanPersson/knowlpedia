import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from link_review_progress import summarize

class LinkProgressTests(unittest.TestCase):
    def test_containers_are_opt_in_and_need_current_reviews(self):
        audit = {'inventory':[{'id':'article','kind':'document','source_sha256':'abc'}], 'counts':{}}
        ledger = {'reviews':[{'id':'article','outcome':'reviewed_unchanged','source_sha256':'abc','evidence':'Read document and checked relevant links without converting it into a definition.'}]}
        self.assertEqual(summarize(audit, {'reviews':[]})['eligible_knowls'], 0)
        self.assertEqual(summarize(audit, ledger, include_containers=True)['reviewed_current'], 1)
        ledger['reviews'][0]['source_sha256'] = 'old'
        self.assertEqual(summarize(audit, ledger, include_containers=True)['remaining_review'], 1)
