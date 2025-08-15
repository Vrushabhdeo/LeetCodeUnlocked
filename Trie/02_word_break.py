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
