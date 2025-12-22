import snap
import unittest
import sys

sys.setrecursionlimit(10000)


def has_euler_path(graph):
    # Check connectivity
    if not snap.IsConnected(graph):
        return False

    # Count odd degree vertices
    odd_count = 0
    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            odd_count += 1

    return odd_count == 2


def has_euler_circuit(graph):
    # Check connectivity
    if not snap.IsConnected(graph):
        return False

    # All vertices must have even degree
    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            return False

    return True


class TestEulerMethods(unittest.TestCase):

    def test_has_euler_path_but_not_circuit(self):
        # Linear path: 0-1-2-3-4
        graph = snap.TUNGraph.New()
        for i in range(5):
            graph.AddNode(i)

        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)

        self.assertTrue(has_euler_path(graph))
        self.assertFalse(has_euler_circuit(graph))

    def test_does_not_have_euler_path(self):
        # Star graph: center connected to 4 leaves
        graph = snap.TUNGraph.New()
        for i in range(5):
            graph.AddNode(i)

        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(0, 4)

        self.assertFalse(has_euler_path(graph))

    def test_has_euler_circuit(self):
        # Cycle graph: 0-1-2-3-0
        graph = snap.TUNGraph.New()
        for i in range(4):
            graph.AddNode(i)

        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 0)

        self.assertTrue(has_euler_circuit(graph))

    def test_does_not_have_euler_circuit(self):
        # Linear path (same as test 1)
        graph = snap.TUNGraph.New()
        for i in range(5):
            graph.AddNode(i)

        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)

        self.assertFalse(has_euler_circuit(graph))


if __name__ == '__main__':
    unittest.main()
