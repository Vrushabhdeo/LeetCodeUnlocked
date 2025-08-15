"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#
#         found_char = ''
#         node = wordDict.root
#         for index, char in enumerate(s):
#             if char in node.children:
#                 node = node.children[char]
#                 found_char += char
#                 if node.is_end:
#                     node = wordDict.root
#             print(found_char)
#
#         return True if s == found_char else False
#
#     """
#     The solution will fail for below case:
#     s = "aaaaaaa" and wordDict = ["aaaa","aa"]
#     """

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is valid

        for i in range(n + 1):
            if dp[i]:
                node = trie.root
                for j in range(i, n):
                    char = s[j]
                    if char not in node.children:
                        break
                    node = node.children[char]
                    if node.is_end:
                        dp[j + 1] = True
        return dp[-1]

trie = Trie()
for word in ["leet","code"]:
    trie.insert(word)

s = 'leetcodeleet'
solution = Solution()
# solution.wordBreak(s=s, wordDict=trie)
print(solution.wordBreak(s=s, wordDict=trie))
