"""
Given a string and an integer k, you need to reverse the first k characters 
for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Example:
	Input: s = "abcdefg", k = 2
	Output: "bacdfeg"

Restrictions:
	The string consists of lower English letters only.
	Length of the given string and k will in the range [1, 10000]
"""
"""
Consider each 2k substring at one time

n = len(s)
if n <= k: reverse k
if k< n <= 2*k: reverse first k

then we can combine n<= k and k<n<2k, as both of these two situations need only reverse k
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        
        reversed_s = ""
        for i in range(0, n, 2*k):
            # check index is in range
            upper_bound = min(2*k+i, n)
            reversed_k = s[i:k+i][::-1] + s[k+i:upper_bound]
            reversed_s = reversed_s + reversed_k
        return reversed_s