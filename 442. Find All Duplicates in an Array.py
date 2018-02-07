"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        cur = 0
        dup_nums = []
        while cur < (len(nums)-1):
            if nums[cur] != nums[cur + 1]:
                cur += 1
            else:
                dup_nums.append(nums[cur])
                cur += 2
        return list(dup_nums)
