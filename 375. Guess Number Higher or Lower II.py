"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
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
