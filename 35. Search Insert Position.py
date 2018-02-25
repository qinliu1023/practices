"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
	Input: [1,3,5,6], 5
	Output: 2
	
Example 2:
	Input: [1,3,5,6], 2
	Output: 1
	
Example 3:
	Input: [1,3,5,6], 7
	Output: 4
	
Example 1:
    Input: [1,3,5,6], 0
    Output: 0
"""
# intuition: compare given target value and each element in given sorted array, 
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums[n-1] < target:
            return n
        elif nums[0] >= target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] < target and nums[i+1] >= target:
                    return i+1        
"""
Got some error at first time for cases whose target is equal nums[0] or nums[n-1]
[1],1
And tried to check whether target is in nums or not, but later found whether it is in or not
need to loop all of them, then combined these two situation together
"""
