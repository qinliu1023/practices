"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object): ## Wrong Answer
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor or dividend == 0:
            return 0

        sums = divisor
        multiple = 1
        while sums + sums <= dividend:
            sums += sums
            multiple += multiple 
        
        if sign == 1:
            return multiple+divide(dividend-sums,divisor)
        else:
            return (0-multiple-divide(dividend-sums,divisor)) #Line 27: NameError: global name 'divide' is not defined


## Corrected but not Accepted
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor or dividend == 0:
            return 0
        
        multiple = 0
        while dividend >= divisor:
            sums = divisor
            count = 1
            while sums + sums <= dividend:
                sums += sums
                count += count
            dividend -= sums
            multiple += count

        if sign == 1:
            return multiple
        else:
            return (0-multiple)
"""
987 / 988 test cases passed.
Input: -2147483648, -1
Output: 2147483648
Expected: 2147483647
Though with Python the result is exactly 2147483648 (no overflow issue), MAX_INT is 2147483647
"""
## Accepted Answer
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor or dividend == 0:
            return 0
        
        multiple = 0
        while dividend >= divisor:
            sums = divisor
            count = 1
            while sums + sums <= dividend:
                sums += sums
                count += count
            dividend -= sums
            multiple += count
        
        
        if sign == 1:
            return min(max(-2147483648, multiple), 2147483647)
        else:
            return min(max(-2147483648, -multiple), 2147483647)