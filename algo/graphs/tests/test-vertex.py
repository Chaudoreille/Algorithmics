from unittest import TestCase, main
from algo.graphs.vertex import Vertex


class TestVertex(TestCase):
    def test_str(self):
        v = Vertex("A", {"wieght": 1}, ["B"])
        EXPECTED_RESULT = "A"

        self.asssertEqual(str(v), EXPECTED_RESULT)


if __name__ == "__main__":
    main()
