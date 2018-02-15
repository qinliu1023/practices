# 67. Add Binary
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
# bin(x): Convert an integer number to a binary string.        
# class int(x, base=10): 
# 	Return an integer object constructed from a number or string x, 
#	or return 0 if no arguments are given.
#	The default base is 10. The allowed values are 0 and 2–36. 
#	Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O/0, or 0x/0X, 
#	as with integer literals in code. Base 0 means to interpret the string exactly 
#	as an integer literal, so that the actual base is 2, 8, 10, or 16.