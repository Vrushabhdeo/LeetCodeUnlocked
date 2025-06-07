"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         if not grid or not grid[0]:
#             return 0
#
#         rows = len(grid)
#         columns = len(grid[0])
#
#         visited_mat = [[0 for _ in range(columns)] for _ in range(rows)]
#         attached_land = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         count_of_island = 0
#         island_map = {}
#
#         for di in range(rows):
#             for dj in range(columns):
#
#                 if not visited_mat[di][dj] and grid[di][dj] == '1':
#                     visited_mat[di][dj] = 1
#                     count_of_island +=1
#                     island_map[count_of_island] = [(di, dj)]
#
#                     for i, j in attached_land:
#                         ni = di + i
#                         nj = dj + j
#                         if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == '1':
#                             visited_mat[ni][nj] = 1
#                             island_map[count_of_island].append((ni, nj))
#
#         return list(sorted(island_map))[-1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '0'  # Mark as visited

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                                queue.append((nx, ny))
                                grid[nx][ny] = '0'  # Mark as visited
        return islands

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
print(solution.numIslands(grid=grid))