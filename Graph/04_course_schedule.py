"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    def can_finish(self, numCourses, prerequisites):
        # Build adjacency list
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)  # Must take b before a

        visited = [False] * numCourses
        rec_stack = [False] * numCourses  # To detect cycles

        def has_cycle(node):
            if rec_stack[node]:
                return True  # Cycle detected
            if visited[node]:
                return False  # Already processed, no cycle

            visited[node] = True
            rec_stack[node] = True

            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True

            rec_stack[node] = False  # Backtrack
            return False

        for course in range(numCourses):
            if not visited[course]:
                if has_cycle(course):
                    return False  # Cycle found, can't finish

        return True  # No cycle, can finish

# Test Case (Example from LeetCode)
solution = Solution()
prerequisites_with_cycle = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]  # Cycle: 0 → 1 → 0
print(solution.can_finish(numCourses=6, prerequisites=prerequisites_with_cycle))  # Output: False (cycle)

"""
Extra: Topological Sort Using DFS

def topological_sort(v, edges):
    # Build adjacency list
    adj = [[] for _ in range(v)]
    for u, v_dest in edges:
        adj[u].append(v_dest)
    
    visited = [False] * v
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for node in range(v):
        if not visited[node]:
            dfs(node)
    
    return stack[::-1]  # Return reversed stack (topological order)

# Given graph
v = 6
edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

# Get topological order
topological_order = topological_sort(v, edges)
print("Topological Order:", topological_order)

"""