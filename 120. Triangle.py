"""
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
"""
# 2 to 3 and 4
# 3 to 6 and 5 but not to 7
# 4 to 5 and 7 but not to 6
# Similar to Binary Tree
# Traverse: Try all possible path, Time Complexity O(2^n)
# DivideConquer: Time Complexity O(2^n)
