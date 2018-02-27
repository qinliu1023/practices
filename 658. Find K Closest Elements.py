"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The 
result should also be sorted in ascending order. If there is a tie, the smaller elements are 
always preferred.

Example 1:
	Input: [1,2,3,4,5], k=4, x=3
	Output: [1,2,3,4]

Example 2:
	Input: [1,2,3,4,5], k=4, x=-1
	Output: [1,2,3,4]

Note:
	The value k is positive and will always be smaller than the length of the sorted array.
	Length of the given array is positive and will not exceed 10**4
	Absolute value of elements in the array and x will not exceed 10**4

UPDATE (2017/9/19):
	The arr parameter had been changed to an array of integers (instead of a list of integers). 
	Please reload the code definition to get the latest changes.
"""
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        distance = {}
        for num in arr:
            distance[num] = abs(num-x)
        
        # sort dictionary by its values and then by its keys
		# https://stackoverflow.com/questions/7742752/sorting-a-dictionary-by-value-then-by-key
        # distance_sorted is a list
        distance_sorted = sorted(distance.items(), key=lambda x: (x[1],x[0])) 
        
        output = []
        for pair in distance_sorted[:k]:
            output.append(pair[0])
        
        return sorted(output)
"""
Above function fails when there are duplicate nums in arr, as python dictionary doesn't support duplicate keys
Wrong Answer: Last executed input: [0,1,1,1,2,3,6,7,8,9], 9, 4
# https://stackoverflow.com/questions/10664856/make-dictionary-with-duplicate-keys-in-python
# http://docs.python.org/library/collections.html#collections.defaultdict
"""
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
	import collections
        distance = collections.defaultdict(list)
        for num in arr:
            distance[abs(num-x)].append(num)
        
        distance_sorted_keys = sorted(distance.keys()) 
        
        output = []
        for i in distance_sorted_keys:
            output.extend(distance[i])
        
        return sorted(output[:k])
