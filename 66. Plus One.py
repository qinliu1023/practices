"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

# 10 + 1 = 11 -> Output: [1,1]
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ''.join(map(str,digits))
        digits_int = int(digits_str) + 1
        temp_list = list(str(digits_int)) #a list of str
        return map(int,temp_list)      # transfer each ele to int   