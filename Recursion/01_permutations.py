"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


from typing import List

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#
#         result = []
#         if len(nums) == 1:
#             return nums
#
#         for index in range(len(nums)):
#             temp_result = [nums[index]] + self.permute(nums = nums[:index] + nums[index+1:])
#             result.append(temp_result)
#
#         return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        if len(nums) == 1:
            return [nums]

        for index in range(len(nums)):
            current = nums[index]
            remaining = nums[:index] + nums[index+1:]

            for p in self.permute(nums=remaining):
                result.append([current] + p)

        return result

solution = Solution()
print(solution.permute(nums = [1,2,3]))