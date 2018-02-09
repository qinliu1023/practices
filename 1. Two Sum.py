"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    if i <= j:
                        return [i,j]
                    else:
                        return [j,i]

# A faster way from discussion                        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # When a number is read (loop by index), calculate its complementary number
        # if the number is not in our dictionary, then add 
        # (complementary number, number index) to the dictionary
        # when the complementary number is read, return the current index and its value in dictionary
        complementary_num_dict = {}
        for index, num in enumerate(nums):
            complementary_num = target - num
            if complementary_num in complementary_num_dict:
                return [complementary_num_dict[complementary_num], index]
            else:
                complementary_num_dict[num] = index
"""
enumerate(sequence, start=0)
    returns a tuple containing a count (from start which defaults to 0) and 
    the values obtained from iterating over sequence:

>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""
