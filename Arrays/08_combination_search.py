"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""


from typing import List

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort() # nlogn
#
#         for i in range(len(candidates)):
#
#             if candidates[i] == target:
#                 res.append([candidates[i]])
#
#             if i>0 and candidates[i-1] == candidates[i]:
#                 continue
#
#             j = i+1
#             k = len(candidates) - 1
#
#             while j<k:
#                 total = candidates[i] + candidates[j] + candidates[k]
#                 if total > target:
#                     k -=1
#                 elif total < target:
#                     j +=1
#                 else:
#                     res.append([candidates[i], candidates[j], candidates[k]])
#                     j +=1
#                     while candidates[j] == candidates[j-1] and j<k:
#                         j+=1
#
#             freq = target // candidates[i]
#             for _ in range(1, freq+1, 1):
#                 compliment = target - (candidates[i] * _)
#                 if compliment in candidates:
#                     res.append([candidates[i]]*_ + [compliment])
#         return res

class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                backtrack(i, path + [candidates[i]], remaining - candidates[i])

        res = []
        candidates.sort()
        backtrack(0, [], target)
        return res

solution = Solution()
print(solution.combinationSum(candidates=[2,3,5], target=8))