from snap import *
import unittest

def has_euler_path(graph):
  vertices = set()
  # Check connectivity
  if not IsConnected(graph):
    return False, vertices

  # Count odd degree vertices
  odd_vertices = []
  for node in graph.Nodes():
    if node.GetDeg() % 2 == 1:
      odd_vertices.append(node.GetId())

  # Euler path exists if there are exactly 2 odd degree vertices
  if len(odd_vertices) == 2:
    vertices = set(odd_vertices)
    return True, vertices

  return False, vertices


def has_euler_circuit(graph):
  # Check connectivity
  if not IsConnected(graph):
    return False

  # All vertices must have even degree
  for node in graph.Nodes():
    if node.GetDeg() % 2 == 1:
      return False

  return True

class TestEulerMethods(unittest.TestCase):

  def test_has_euler_path_but_not_circuit(self):
    # Linear path: 0-1-2-3-4
    graph = TUNGraph.New()
    for i in range(5):
      graph.AddNode(i)

    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(2, 3)
    graph.AddEdge(3, 4)

    result, vertices = has_euler_path(graph)
    self.assertTrue(result)
    self.assertEqual(len(vertices), 2)

  def test_does_not_have_euler_path(self):
    # Star graph: center connected to 4 leaves
    graph = TUNGraph.New()
    for i in range(5):
      graph.AddNode(i)

    graph.AddEdge(0, 1)
    graph.AddEdge(0, 2)
    graph.AddEdge(0, 3)
    graph.AddEdge(0, 4)

    result, vertices = has_euler_path(graph)
    self.assertFalse(result)
    self.assertEqual(len(vertices), 0)

  def test_has_euler_circuit(self):
    # Large cycle graph with at least 1000 nodes
    graph = TUNGraph.New()
    num_nodes = 1000
    for i in range(num_nodes):
      graph.AddNode(i)

    for i in range(num_nodes - 1):
      graph.AddEdge(i, i + 1)
    graph.AddEdge(num_nodes - 1, 0)  # Close the cycle

    result = has_euler_circuit(graph)
    self.assertTrue(result)
    self.assertTrue(graph.GetNodes()>=1000)

  def test_does_not_have_euler_circuit(self):
    # Linear path (same as test 1)
    graph = TUNGraph.New()
    for i in range(5):
      graph.AddNode(i)

    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(2, 3)
    graph.AddEdge(3, 4)

    result = has_euler_circuit(graph)
    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
