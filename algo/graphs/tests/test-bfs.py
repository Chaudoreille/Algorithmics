from unittest import TestCase, main
from xml.dom import NotFoundErr

from algo.graphs.graph import Graph

DEFAULT_GRAPH = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'F'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D', 'F'],
        'F': ['E', 'B'],
    }

class TestBfs(TestCase):
    def test_graph_default_constructor(self):
        graph = Graph()
        length = len(graph)

        self.assertEqual(length, 0)

    def test_value_not_in_graph(self):
        graph = Graph(DEFAULT_GRAPH)
        START_NODE = 'A'
        VALUE = 'Z'

        self.assertRaises(NotFoundErr, graph.bfs, START_NODE, VALUE)

    def test_value_in_graph(self):
        graph = Graph(DEFAULT_GRAPH)
        START_NODE = 'A'
        VALUE = 'E'

        value = graph.bfs(START_NODE, VALUE)

        self.assertEqual(value, 'E')

    def test_start_value_not_in_graph(self):
        graph = Graph(DEFAULT_GRAPH)
        START_NODE = 'Z'
        VALUE = 'E'

        self.assertRaises(ValueError, graph.bfs, START_NODE, VALUE)
        


if __name__ == "__main__":
    main()