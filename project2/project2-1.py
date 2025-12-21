"""
Project 2 - Part 1: Euler Paths and Circuits
AUEB M.Sc. Data Science - Social Network Analysis
Due: December 28, 2025

This script implements functions to detect Euler paths and circuits in graphs
using the SNAP library.
"""

import snap
import unittest
import sys

# Set recursion limit for large graphs
sys.setrecursionlimit(10000)


def has_euler_path(graph):
    """
    Check if a graph has an Euler path.

    An Euler path is a path that uses every edge of a graph exactly once.
    An Euler path starts and ends at different vertices.

    Requirements:
    - Graph must be connected
    - Exactly 2 vertices must have odd degree

    Args:
        graph: A SNAP undirected graph (TUNGraph)

    Returns:
        bool: True if graph has an Euler path, False otherwise
    """
    # Check if graph is connected
    if not snap.IsConnected(graph):
        return False

    # Count vertices with odd degree
    odd_degree_count = 0
    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            odd_degree_count += 1

    # Euler path exists if exactly 2 vertices have odd degree
    return odd_degree_count == 2


def has_euler_circuit(graph):
    """
    Check if a graph has an Euler circuit.

    An Euler circuit is a circuit that uses every edge of a graph exactly once.
    An Euler circuit starts and ends at the same vertex.

    Requirements:
    - Graph must be connected
    - All vertices must have even degree

    Args:
        graph: A SNAP undirected graph (TUNGraph)

    Returns:
        bool: True if graph has an Euler circuit, False otherwise
    """
    # Check if graph is connected
    if not snap.IsConnected(graph):
        return False

    # Check if all vertices have even degree
    for node in graph.Nodes():
        if node.GetDeg() % 2 == 1:
            return False

    return True


class TestEulerMethods(unittest.TestCase):
    """Test cases for Euler path and circuit detection."""

    def test_has_euler_path_but_not_circuit(self):
        """
        Test Case 1: Graph that has an Euler path but NOT an Euler circuit.

        Creates a linear path graph: 0-1-2-3-4
        - Vertices 0 and 4 have degree 1 (odd)
        - Vertices 1, 2, 3 have degree 2 (even)
        - Total: exactly 2 odd-degree vertices -> Euler path exists
        - Not all degrees even -> No Euler circuit
        """
        print("\n[Test 1] Creating linear path graph (0-1-2-3-4)...")
        graph = snap.TUNGraph.New()

        # Add nodes
        for i in range(5):
            graph.AddNode(i)

        # Create linear path
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)

        # Verify degree distribution
        degrees = [graph.GetNI(i).GetDeg() for i in range(5)]
        print(f"  Node degrees: {degrees}")
        print(f"  Odd degree nodes: {sum(1 for d in degrees if d % 2 == 1)}")

        # Assertions
        self.assertTrue(has_euler_path(graph),
                       "Linear path should have Euler path")
        self.assertFalse(has_euler_circuit(graph),
                        "Linear path should NOT have Euler circuit")

        print("  ✓ Test 1 PASSED: Has Euler path but NOT circuit")

    def test_does_not_have_euler_path(self):
        """
        Test Case 2: Graph that does NOT have an Euler path.

        Creates a star graph with center connected to 4 leaves:
        - Center node (0) has degree 4 (even)
        - Four leaf nodes (1,2,3,4) each have degree 1 (odd)
        - Total: 4 odd-degree vertices -> Violates "exactly 2" rule
        - Therefore, no Euler path exists
        """
        print("\n[Test 2] Creating star graph (center + 4 leaves)...")
        graph = snap.TUNGraph.New()

        # Add nodes
        for i in range(5):
            graph.AddNode(i)

        # Create star graph (center node 0 connected to all others)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(0, 4)

        # Verify degree distribution
        degrees = [graph.GetNI(i).GetDeg() for i in range(5)]
        print(f"  Node degrees: {degrees}")
        print(f"  Odd degree nodes: {sum(1 for d in degrees if d % 2 == 1)}")

        # Assertion
        self.assertFalse(has_euler_path(graph),
                        "Star graph with 4 leaves should NOT have Euler path")

        print("  ✓ Test 2 PASSED: Does NOT have Euler path")

    def test_has_euler_circuit(self):
        """
        Test Case 3: Graph that has an Euler circuit.

        Creates a cycle graph: 0-1-2-3-0
        - All 4 vertices have degree 2 (even)
        - Graph is connected
        - All even degrees -> Euler circuit exists
        """
        print("\n[Test 3] Creating cycle graph (0-1-2-3-0)...")
        graph = snap.TUNGraph.New()

        # Add nodes
        for i in range(4):
            graph.AddNode(i)

        # Create cycle
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 0)

        # Verify degree distribution
        degrees = [graph.GetNI(i).GetDeg() for i in range(4)]
        print(f"  Node degrees: {degrees}")
        print(f"  All degrees even: {all(d % 2 == 0 for d in degrees)}")

        # Assertion
        self.assertTrue(has_euler_circuit(graph),
                       "Cycle graph should have Euler circuit")

        print("  ✓ Test 3 PASSED: Has Euler circuit")

    def test_does_not_have_euler_circuit(self):
        """
        Test Case 4: Graph that does NOT have an Euler circuit.

        Uses the same linear path as Test 1:
        - Has odd-degree vertices (0 and 4)
        - Not all degrees are even -> No Euler circuit
        """
        print("\n[Test 4] Creating linear path (same as Test 1)...")
        graph = snap.TUNGraph.New()

        # Add nodes
        for i in range(5):
            graph.AddNode(i)

        # Create linear path
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)

        # Verify degree distribution
        degrees = [graph.GetNI(i).GetDeg() for i in range(5)]
        print(f"  Node degrees: {degrees}")
        print(f"  All degrees even: {all(d % 2 == 0 for d in degrees)}")

        # Assertion
        self.assertFalse(has_euler_circuit(graph),
                        "Linear path should NOT have Euler circuit")

        print("  ✓ Test 4 PASSED: Does NOT have Euler circuit")


if __name__ == '__main__':
    print("=" * 70)
    print("PROJECT 2 - PART 1: EULER PATHS AND CIRCUITS")
    print("=" * 70)
    print("\nTesting Euler path and circuit detection algorithms")
    print("Using SNAP (Stanford Network Analysis Platform)")
    print("=" * 70)

    # Run tests with verbose output
    unittest.main(verbosity=2, exit=True)
