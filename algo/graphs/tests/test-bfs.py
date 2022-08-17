from algo.graphs.bfs import bfs
import unittest

class TestBfs(unittest.TestCase):
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'F'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D', 'F'],
        'F': ['E', 'B'],
    }

    def test_value_not_in_graph(self):
        START_NODE = 'A'
        VALUE = 'Z'

        value = bfs(self.graph, START_NODE, VALUE)

        self.assertEqual(value, None)

    def test_value_in_graph(self):
        START_NODE = 'A'
        VALUE = 'E'

        value = bfs(self.graph, START_NODE, VALUE)

        self.assertEqual(value, 'E')

    def test_start_value_not_in_graph(self):
        START_NODE = 'Z'
        VALUE = 'E'

        value = bfs(self.graph, START_NODE, VALUE)

        self.assertEqual(value, None)


if __name__ == "__main__":
    unittest.main()