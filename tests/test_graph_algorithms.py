import importlib.util
import sys
import unittest
from pathlib import Path


MODULE = Path(__file__).parents[1] / "packages" / "compiler" / "graph_algorithms.py"
SPEC = importlib.util.spec_from_file_location("graph_algorithms", MODULE)
assert SPEC and SPEC.loader
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)


class GraphAlgorithmTests(unittest.TestCase):
    def test_long_chain_is_iterative_and_stably_sorted(self):
        chain = {f"n{i:04d}": ([f"n{i - 1:04d}"] if i else []) for i in range(3000)}
        self.assertEqual(graph.strongly_connected_components(chain)[0], ("n0000",))
        self.assertEqual(len(graph.topological_order(chain)), 3000)
        self.assertEqual(graph.cycle_components(chain), [])

    def test_disconnected_and_self_cycles_are_reported_deterministically(self):
        graph_data = {
            "z": ["z"],
            "b": ["c"],
            "c": ["b"],
            "isolated": [],
        }
        self.assertEqual(graph.cycle_components(graph_data), [("b", "c"), ("z",)])
        self.assertIsNone(graph.topological_order(graph_data))

    def test_duplicate_edges_do_not_change_order_or_components(self):
        graph_data = {"a": [], "b": ["a", "a"], "c": ["b", "b"]}
        self.assertEqual(graph.normalized_adjacency(graph_data)["b"], ("a",))
        self.assertEqual(graph.topological_order(graph_data), ("a", "b", "c"))

    def test_cycle_witness_is_a_closed_walk_using_real_edges(self):
        graph_data = {"a": ["b"], "b": ["c"], "c": ["a", "d"], "d": []}
        witnesses = graph.cycle_witnesses(graph_data)
        self.assertEqual(witnesses, [("a", "b", "c", "a")])
        for witness in witnesses:
            self.assertEqual(witness[0], witness[-1])
            for source, target in zip(witness, witness[1:]):
                self.assertIn(target, graph_data[source])


if __name__ == "__main__":
    unittest.main()
