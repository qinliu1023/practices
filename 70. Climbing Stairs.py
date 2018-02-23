"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
	Input: 2
	Output:  2
	Explanation:  There are two ways to climb to the top.
  				  1. 1 step + 1 step
				  2. 2 steps
Example 2:
    Input: 3
    Output:  3
    Explanation:  There are three ways to climb to the top.
				  1. 1 step + 1 step + 1 step
				  2. 1 step + 2 steps
				  3. 2 steps + 1 step
"""
"""
n = x * 1 + y * 2, x, y are int
for each pair of (x,y) using combination to get distinct ways: x+yCx  choosing x from (x+y) 
add all combination values together to get the total distinct ways to climb to the top
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def combination(n,r):
            """
            choosing x from r
            n!/(k!(n-k)!)
            """
            import math
            f = math.factorial
            return f(n) / f(r) / f(n-r)

        # x is number taking 1 step
        # y is number taking 2 steps
        # cur_num_ways is the combiantion values of current (x,y) pair
        sum_num_ways = 0
        for x in range(n+1):
            if (n-x) % 2 == 0:
                y = (n-x)/2
                cur_num_ways = combination(x+y,x)
                sum_num_ways = sum_num_ways + cur_num_ways
        return sum_num_ways
