"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#
#         result = ''
#         for i in range(n):
#             j = i + 1
#             k = j + 1
#             local_result = s[i]
#             while j < n and k < n:
#                 if s[j] not in local_result and s[k] not in local_result: # if both not present add
#                     local_result += s[j]
#                     local_result += s[k]
#                 elif s[j] not in local_result and s[k] in local_result: # if first not present and second present then add first
#                     local_result += s[j]
#                 j = k+1
#                 k = j+1
#             if len(local_result) > len(result):
#                 result = local_result
#             else:
#                 pass
#         return len(result)

# Sliding window method
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Tracks the last index of each character
        left = max_len = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # Move left past the duplicate
            char_index[char] = right  # Update the character's last index
            max_len = max(max_len, right - left + 1)

        return max_len

solution = Solution()
print(solution.lengthOfLongestSubstring(s='abc%a%5'))