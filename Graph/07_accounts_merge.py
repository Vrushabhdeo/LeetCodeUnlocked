"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

# from typing import List
#
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         n = len(accounts)
#         if n == 0 or n == 1:
#             return accounts
#
#         account_name_email_map = dict()
#
#         for _ in range(n):
#             name, emails = accounts[_][0], accounts[_][1:]
#             print(name)
#             print(emails)
#
#             if (name, 0) not in account_name_email_map:
#                 if emails[0] in account_name_email_map[name]:
#                     account_name_email_map[(name, 0)] = emails
#             else:
#                 for i in range(1, n):
#                     if (name, i) in account_name_email_map:
#                         continue
#                 account_name_email_map[name, i] = emails

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph = defaultdict(set)
        email_to_name = dict()

        # Step 1: Build graph (CORRECTED)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            # Connect ALL emails in this account to each other
            for email in emails:
                email_graph[email].update(emails)  # Connect to all others
                email_graph[email].remove(email)   # Remove self-loop
                email_to_name[email] = name

        # Step 2: DFS remains correct
        visited = set()
        merged_accounts = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_graph:
            if email not in visited:
                component = []
                dfs(email, component)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts

solution = Solution()
print(solution.accountsMerge(accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],
                                       ["John","johnsmith@mail.com","john00@mail.com"],
                                       ["Mary","mary@mail.com"],
                                       ["John","johnnybravo@mail.com"]]))