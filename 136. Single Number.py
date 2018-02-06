"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# The following code is using a dict to store the (num, freq) 
# but it got an error of Time Limit Exceeded.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_freq = {}
        for num in nums:
            if num not in nums_freq.keys():
                nums_freq[num] = 1
            else:
                nums_freq[num] = nums_freq[num] + 1
        
        for num in nums_freq.keys():
            if nums_freq[num] == 1:
                return num

# Solutions:
# https://leetcode.com/problems/single-number/solution/
# 2∗(a+b+c)−(a+a+b+b+c)=c

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
