"""
Write a function that takes an unsigned integer and returns the number of ’1' bits 
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 
00000000000000000000000000001011, so the function should return 3.


Hamming Weight: https://en.wikipedia.org/wiki/Hamming_weight
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bin = bin(n)[2:] # returns a str
        return n_bin.count("1") # acounts frequency of substring 