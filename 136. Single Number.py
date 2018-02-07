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


# A similar question can be solved using Math
# 268. Missing Number
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?    
"""
    
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # number starts from 0 to n, and missing one of them
        # if number not missing the sum should be sum(range(n))
        # the difference between sum(range(n)) and sum(nums) is the number missing
        n = len(nums) + 1
        return sum(range(n)) - sum(nums)

# 137. Single Number II
"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""



# 260. Single Number III
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
