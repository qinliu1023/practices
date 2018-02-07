"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # when nums has more than 1 integers
        # sort the nums and check integers adjcent to see the differece
        # if the difference is 2, then a[i]+1 is missing
        # if the difference is 3, then a[i]+1 and a[i]+2 are missing
        # if the difference is k, then a[i]+1, ... , a[i]+k-1 are missing
        # k should be less than n-2
        # possible arrays are [], [1,...,n], [2,...,n], [1,...,n-1], [2,...,n-1]
        n = len(nums)
        nums.sort()
        if len(nums) == 0:
            missing_values = []
        elif len(nums) == 1:
            if nums[0] == 1:
                missing_values = range(2,n+1)
            elif nums[0] == n:
                missing_values = range(1,n)
            else:
                missing_vaues = range(1,nums[0]) + range(nums[0]+1,n+1)
        elif len(nums) > 1 and nums[0] == 1 and nums[n-1] == n:
            cur = 0
            missing_values = []
            while cur < len(nums)-1:
                k = nums[cur+1] - nums[cur]
                if k > 1:
                    for i in range(1,k):
                        missing_values.append(nums[cur]+i)
                cur += 1    
        elif len(nums) > 1 and nums[0] == 1 and nums[n-1] != n:
            nums.append(n)
            nums.sort()
            cur = 0
            missing_values = [n]
            while cur < len(nums)-1:
                k = nums[cur+1] - nums[cur]
                if k > 1:
                    for i in range(1,k):
                        missing_values.append(nums[cur]+i)
                cur += 1 
        elif len(nums) > 1 and nums[0] != 1 and nums[n-1] == n:
            nums.append(1)
            nums.sort()
            cur = 0
            missing_values = [1]
            while cur < len(nums)-1:
                k = nums[cur+1] - nums[cur]
                if k > 1:
                    for i in range(1,k):
                        missing_values.append(nums[cur]+i)
                cur += 1       
        elif len(nums) > 1 and nums[0] != 1 and nums[n-1] != n:
            nums.extend([1,n])
            nums.sort()
            cur = 0
            missing_values = [1,n]
            while cur < len(nums)-1:
                k = nums[cur+1] - nums[cur]
                if k > 1:
                    for i in range(1,k):
                        missing_values.append(nums[cur]+i)
                cur += 1                  
        return missing_values                

# The idea here is when 1 and n is not in the array, we can add them to make it a array contains from 1 to n
# After doing this, all possible situation could be dealt with using the same method
# then a function is created as following to make the give array a standard one, say from 1 to n

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def missing_values(nums):
        # This nums is a standard one containing both 1 and n    
            cur = 0
            nums.sort()
            missing_values = []
            while cur < len(nums)-1:
                k = nums[cur+1] - nums[cur]
                if k > 1:
                    for i in range(1,k):
                        missing_values.append(nums[cur]+i)
                cur += 1
            return missing_values
            
        n = len(nums)
        nums.sort()
        if len(nums) == 0:
            missing_values = []
        elif len(nums) == 1:
            if nums[0] == 1:
                missing_values = range(2,n+1)
            elif nums[0] == n:
                missing_values = range(1,n)
            else:
                missing_vaues = range(1,nums[0]) + range(nums[0]+1,n+1)
        elif len(nums) > 1 and nums[0] == 1 and nums[n-1] == n:
            missing_values = missing_values(nums)
        elif len(nums) > 1 and nums[0] == 1 and nums[n-1] != n:
            nums.append(n)
            missing_values = missing_values(nums)
            missing_values.append(n)
        elif len(nums) > 1 and nums[0] != 1 and nums[n-1] == n:
            nums.append(1)
            missing_values = missing_values(nums)
            missing_values.append(1)    
        elif len(nums) > 1 and nums[0] != 1 and nums[n-1] != n:
            nums.extend([1,n])
            missing_values = missing_values(nums)
            missing_values.extend([1,n])                  
        return missing_values                       
