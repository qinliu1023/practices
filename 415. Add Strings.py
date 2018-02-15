415. Add Strings
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str_int(num):
            """
            :type num: str
            """
            n = len(num)
            num_int = 0
            for i in range(n):
                digit1 = num[i]
                for k, digit2 in enumerate("0123456789"): # use enumerate to get the int of str
                    if digit1 == digit2:
                        break
                weight = 10**(n-1-i)
                num_int += k*weight
            return num_int
        
        return str(str_int(num1) + str_int(num2)) # Accepted but poor performance
          