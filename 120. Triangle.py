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


# 64. Minimum Path Sum
"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]

Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
"""


# 62. Unique Paths
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
# Math combination: C
"""
[1,1,1,1,1]
[1,2,3,4,5]
[1,3,6,10,1]
"""


## 300. Longest Increasing Subsequence
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(nlogn) time complexity?
"""

"""
dp = [1,1,1,1,1]
nums = [5,4,1,2,3]
curr, val in enumerate(nums)
(curr,val): [(0,5),(1,4),(2,1),(3,2),(4,3)]

(curr,val) == (1,4)
	prev [0]:
		nums[0] == 5 < val == 4 X
		[1,1,1,1,1]

(curr,val) == (2,1)
	prev [0,1]:
		nums[0] == 5 < val == 1 X
		nums[1] == 4 < val == 1 X
		[1,1,1,1,1]

(curr,val) == (3,2)
	prev [0,1,2]:
		nums[0] == 5 < val == 2 X
		nums[1] == 4 < val == 2 X	
		nums[2] == 1 < val == 2 
		[1,1,1,2,1]

(curr,val) == (4,3)
	prev [0,1,2,3]:
		nums[0] == 5 < val == 3 X
		nums[1] == 4 < val == 3 X
		nums[2] == 1 < val == 3 
		nums[3] == 2 < val == 3 		
		[1,1,1,2,3]
"""
