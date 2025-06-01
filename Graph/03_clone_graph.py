"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # if not node:
        #     return Node()

        # if not node.neighbors:
        #     return Node(node.val)

        # neighbour_queue = deque([node])
        # root_cloned_graph = None

        # while neighbour_queue:
        #     current_node = neighbour_queue.popleft()
        #     if current_node.neighbors:
        #         neighbour_queue.append(current_node.neighbors)
        #         current_node = Node(current_node.val, current_node.neighbors)
        #     else:
        #         current_node = Node(current_node.val)
        #     if not root_cloned_graph:
        #         root_cloned_graph = current_node

        # return root_cloned_graph

        if not node:
            return None

        # Dictionary to map original nodes to their clones
        node_map = {}

        # Initialize queue with the original node
        queue = deque([node])

        # Create the clone of the first node
        node_map[node] = Node(node.val)

        while queue:
            current_node = queue.popleft()

            # Iterate through all neighbors of the current node
            for neighbor in current_node.neighbors:
                if neighbor not in node_map:
                    # Clone the neighbor if not already cloned
                    node_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add the cloned neighbor to the current clone's neighbors
                node_map[current_node].neighbors.append(node_map[neighbor])

        return node_map[node]

# Input Graph:
# 1 -- 2
# |    |
# 4 -- 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Test
cloned = Solution().cloneGraph(node1)
