"""
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


from collections import deque
from pprint import pprint
from turtledemo.penrose import start
from typing import List

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return 0
#
#         if (len(grid)) < 2:
#             if 2 in grid[0] or 0 in grid[0]:
#                 return 0
#             else:
#                 return -1
#
#         r = len(grid)
#         c = len(grid[0])
#
#         visited_grid = [[0 for _ in range(c)] for _ in range(r)]
#
#         directions = [(0,1), (1,0), (0, -1), (-1, 0)]
#
#         rotten_time = dict()
#
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 2 and not visited_grid[i][j]:
#                     visited_grid[i][j] = 1
#                     start_rotting = 0
#                     queue = deque([(i, j, start_rotting)])
#
#                     while queue:
#                         x, y, start_rotting = queue.popleft()
#                         rotten_time[(x,y)] = start_rotting
#
#                         for di, dj in directions:
#                             ni ,nj = di+x, dj+y
#                             if 0<= ni < r and 0<= nj < c and grid[ni][nj] == 1:
#                                 grid[ni][nj] = 2
#                                 rotten_time[(ni,nj)] = start_rotting+1
#                                 visited_grid[ni][nj] = 1
#                                 queue.append((ni, nj, start_rotting+1))
#
#         # Check for complete rotten grid
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 1:
#                     return -1
#
#         return list(sorted(rotten_time.values()))[-1]

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize: Enqueue all rotten oranges, count fresh ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (i, j, time)
                elif grid[i][j] == 1:
                    fresh_count += 1

        # Edge Case: No fresh oranges initially
        if fresh_count == 0:
            return 0

        max_time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            x, y, time = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # Rot the orange
                    fresh_count -= 1
                    queue.append((nx, ny, time + 1))
                    max_time = max(max_time, time + 1)  # Track latest time

        return max_time if fresh_count == 0 else -1

solution = Solution()
assert solution.orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]]) == 4

assert solution.orangesRotting(grid=[[2,1,1],[0,1,1],[1,0,1]]) == -1

assert solution.orangesRotting(grid=[[0,2]]) == 0