"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.


Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""


# from typing import List
#
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         def find_min_dist(pos_i, pos_j, row_size, column_size):
#             for i in range(row_size):
#                 for j in range(column_size):
#                     if mat[i][j] == 0:
#                         dist_i = min(pos_i, abs(pos_i - i))
#                         dist_j = min(pos_j, abs(pos_j - j))
#             return dist_i, dist_j
#
#         row_size = int(len(mat))
#         column_size = int(len(mat[0]))
#
#         for each_row in range(row_size):
#             for each_column in range (column_size):
#                 if mat[each_row][each_column] ==1:
#                     min_row, min_column = find_min_dist(each_row, each_column, row_size, column_size)
#                     dist = abs(min_row - each_row) + abs(min_column - each_column)
#         return mat

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        # Step 1: Initialize queue with all 0s and mark 1s as -1 (unprocessed)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1  # Placeholder for unprocessed 1s

        # Step 2: BFS to update distances
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))
        return mat

solution = Solution()
print(solution.updateMatrix(mat=[[0,0,0],[0,1,0],[1,1,1]]))