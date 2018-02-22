
"""
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Hamming distance: https://en.wikipedia.org/wiki/Hamming_distance
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:] # turn int to binary and get a str
        y_bin = bin(y)[2:]
        # compare the length of x_bin and y_bin
        # add "0" to make them have the same length
        len_x_bin = len(x_bin)
        len_y_bin = len(y_bin)
        if len_x_bin <= len_y_bin:
            len_diff = len_y_bin-len_x_bin
            x_str = "0" * len_diff + x_bin
            y_str = y_bin
            n = len_y_bin
        if len_x_bin > len_y_bin:
            len_diff = len_x_bin-len_y_bin
            y_str = "0" * len_diff + y_bin
            x_str = x_bin
            n = len_x_bin
        
        # loop to compare corresponding values one by one
        # using count to count different bits
        count = 0
        for i in range(n):
            if x_str[i] != y_str[i]:
                count += 1
        return count        
        