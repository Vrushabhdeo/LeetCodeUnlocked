"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # new_interval_start = newInterval[0]
        # new_interval_end = newInterval[1]
        # result_list = []

        # for each_index in range(len(intervals)):
        #     if intervals[each_index][1] < new_interval_start:
        #         result_list.append(intervals[each_index])
        #     elif intervals[each_index][0] <= new_interval_start <=intervals[each_index][1]:
        #         merge_start = intervals[each_index][0]
        #         end_merger = each_index
        #         while not end_merger < len(intervals) and (intervals[end_merger][0] <= new_interval_end <=intervals[end_merger][1]):
        #             end_merger +=1
        #         merge_end = intervals[end_merger][1]
        #         result_list.append([merge_start, merge_end])
        #         break
        # if end_merger:
        #     result_list.extend(intervals[end_merger+1:])
        # return result_list
        left = [x for x in intervals if x[1] < newInterval[0]]
        right = [x for x in intervals if x[0] > newInterval[1]]

        if left + right != intervals:  # Overlaps exist
            merged_start = min(newInterval[0], intervals[len(left)][0])
            merged_end = max(newInterval[1], intervals[-len(right) - 1][1])
            newInterval = [merged_start, merged_end]

        return left + [newInterval] + right

solution = Solution()
assert solution.insert(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8])


"""
DFS: Iterative Array Implementation using Stack

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process the node
            # Push neighbors in reverse order to match recursive DFS
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Undirected graph example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nIterative DFS:")
dfs_iterative(graph, 'A')  # Start from node 'A'

T: O(V + E)
S: O(V)

----------------------------

BFS: Iterative Array Implementation using Queue

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process the node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("\nBFS:")
bfs(graph, 'A')  # Start from node 'A'

T: O(V + E)
S: O(V)

"""