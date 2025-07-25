"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         red_count = 0
#         white_count = 0
#         blue_count = 0
#         for i in range(len(nums)):
#             colour = nums[i]
#             if colour == 0:
#                 red_count +=1
#             elif colour == 1:
#                 white_count +=1
#             else:
#                 blue_count +=1
#
#         for i in range(len(nums)):
#             if not red_count == 0:
#                 nums[i] = 0
#                 red_count -=1
#             elif not white_count == 0:
#                 nums[i] = 1
#                 white_count -= 1
#             else:
#                 nums[i] = 2
#                 blue_count -=1


# Dutch National Flag Algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

solution = Solution()
assert solution.sortColors(nums=[2,0,2,1,1,0]) == [0,0,1,1,2,2]