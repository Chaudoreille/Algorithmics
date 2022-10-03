from unittest import TestCase, main
from algo.graphs.vertex import Vertex


class TestVertex(TestCase):
    def test_str(self):
        a = Vertex("A", [Vertex("B")])
        EXPECTED_RESULT = "A"

        self.assertEqual(str(a), EXPECTED_RESULT)

    def test_get_item(self):
        b = Vertex("B")
        a = Vertex("A", [b])

        self.assertEqual(b, a["B"])

    def test_set_item(self):
        a = Vertex("A")
        b = Vertex("B")

        a["B"] = b
        b["A"] = a

        self.assertEqual(b, a["B"])
        self.assertEqual(a, b["A"])
    
    def test_append(self):
        a = Vertex("A")
        b = Vertex("B")
        c = Vertex("C")

        a.append(b)
        a.append(c)

        self.assertEqual(b, a["B"])
        self.assertEqual(c, a["C"])

    def test_delitem(self):
        a = Vertex("A", [Vertex("B")])
        b = a["B"]

        del a["B"]

        self.assertRaises(KeyError, a.__getitem__, "B")
        self.assertEqual(b.name, "B")

if __name__ == "__main__":
    main()
