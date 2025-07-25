"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""



from typing import List

# from math import *
# Early Solution
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#
#         raw_euclidean_distances = {}
#
#         # calculate Euclidean distance
#         for each_point in points:
#             distances =  sqrt(pow(each_point[0], 2) + pow(each_point[1], 2))
#             if not distances in raw_euclidean_distances.keys():
#                 raw_euclidean_distances[distances] = (each_point)
#             else:
#                 duplicate_distance = raw_euclidean_distances[distances]
#                 new_distance = [duplicate_distance, each_point]
#                 raw_euclidean_distances[distances] = new_distance
#
#         result_list = []
#         for each_element in sorted(raw_euclidean_distances.keys())[:k]:
#             result_list.append(raw_euclidean_distances[each_element])
#
#         return result_list

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate squared distances (avoid sqrt for efficiency)
        distance_points = [(x ** 2 + y ** 2, [x, y]) for x, y in points]

        # Sort by distance and extract first k points
        distance_points.sort()
        return [point for (_, point) in distance_points[:k]]

solution = Solution()
print(solution.kClosest(points=[[3,3],[5,-1],[-2,4]], k= 2))