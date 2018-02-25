"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int -- 'int' object is not iterable
        :rtype: int
        """
        versions = range(1,n+1) -- get a list for iteration
        for version in versions:
            if isBadVersion(version) == True:
                return version
# Runtime Error Message: Line 12: MemoryError
# Last executed input: 2126753390 versions, 1702766719 is the first bad version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Using Binary Search
# define left, right, mid, if isBadVersion(mid) is True, assign mid to right, otherwise, assign mid to left
# set left + 1 < right so that there is no need to consider mid+1 situations 
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search
        left = 1
        right = n
        while left + 1 < right:
            mid = (right+left)/2
            if isBadVersion(mid) == True:
                right = mid 
            else:
                left = mid
                
        if isBadVersion(left) == True:
            return left
        else:
            return right       
