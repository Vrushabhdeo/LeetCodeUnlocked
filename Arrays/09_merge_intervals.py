"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         result = list()
#         visited = [0] * len(intervals)
#
#         for i in range(len(intervals)):
#             if not visited[i]:
#                 visited[i] = 1
#                 first_i, first_j = intervals[i]
#
#                 if i < len(intervals)-1:
#                     second_i, second_j = intervals[i+1]
#                 else:
#                     result.append(intervals[i])
#                     continue
#
#                 if first_i < first_j < second_i < second_j:
#                     result.append(intervals[i])
#                     continue
#                 elif first_i == first_j:
#                     result.append(intervals[i])
#                     continue
#                 elif second_i == second_j:
#                     visited[i+1] = 1
#                     result.append(intervals[i])
#                     result.append(intervals[i+1])
#                     continue
#                 else:
#                     visited[i+1] = 1
#                     interval_i = min(first_i, second_i)
#                     interval_j = max(first_j, second_j)
#                     result.append([interval_i, interval_j])
#
#         return result
# solution = Solution()
# print(solution.merge(intervals =[[1,4],[0,0]]))

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 1. Sort by start
        intervals.sort(key=lambda x: x[0])

        result = []
        # Initialize with the first interval
        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= cur_end:
                # Overlaps: merge
                cur_end = max(cur_end, end)
            else:
                # No overlap: add the previous interval and reset current
                result.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        # Append the last interval
        result.append([cur_start, cur_end])
        return result

# Example usage:
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
# Output: [[1,6],[8,10],[15,18]]
