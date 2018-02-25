"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
	Given [5, 7, 7, 8, 8, 10] and target value 8,
	return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
        
        if len(indices) == 0:
            return [-1,-1]
        else:
            left = indices[0]
            right = indices[len(indices)-1]
            return [left, right]
            
# using binary search
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1    # right = len(nums)-1 to void index being out of range 
    
        if len(nums) == 0 or nums[left] > target or nums[right] < target:
            return [-1,-1]
        
        while left + 1 < right:
            mid = (left+ right)/2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            low = left
        elif nums[right] == target:
            low = right
        else:
            low = -1
        
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left+ right)/2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            high = right
        elif nums[left] == target:
            high = left
        else:
            high = -1
            
        return [low, high]
