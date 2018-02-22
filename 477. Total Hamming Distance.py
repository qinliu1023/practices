"""
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
"""
## First solution is to use the function we build for hamming distance of 2 numbers
## loop and find each pair in our nums and add all hamming distances to get the total
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def hammingDistance(x, y):
            """
            :type x: int
            :type y: int
            :rtype: int
            """
            x_bin = bin(x)[2:] # turn int to binary and get a str
            y_bin = bin(y)[2:]
            # compare the length of x_bin and y_bin
            # add "0" to make them have the same length
            len_x_bin = len(x_bin)
            len_y_bin = len(y_bin)
            if len_x_bin <= len_y_bin:
                len_diff = len_y_bin-len_x_bin
                x_str = "0" * len_diff + x_bin
                y_str = y_bin
                n = len_y_bin
            if len_x_bin > len_y_bin:
                len_diff = len_x_bin-len_y_bin
                y_str = "0" * len_diff + y_bin
                x_str = x_bin
                n = len_x_bin        
            # loop to compare corresponding values one by one
            # using count to count different bits
            count = 0
            for i in range(n):
                if x_str[i] != y_str[i]:
                    count += 1
            return count        
        
        total_distance = 0
        for i in range(len(nums)):
            for j in range(i):
                total_distance += hammingDistance(nums[i], nums[j])
        return total_distance
# 26 / 47 test cases passed. Error of Time Limit Exceeded when input is large.


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_pairs = zip(*map('{:032b}'.format, nums))
        total_hamming_distance = 0
        for pair in bit_pairs:
            hamming_distance = pair.count('0') * pair.count('1')
            total_hamming_distance += hamming_distance
        return total_hamming_distance

# using map() apply function to every item in nums and return a list of the results.
# '{:032b}'.format -- Convert an Integer into 32bit Binary
# zip() -- returns a list of tuples, where the i-th tuple contains 
#		   the i-th element from each of the argument sequences or iterables 
# zip() in conjunction with the * operator can be used to unzip a list:
#	>>> x = [1, 2, 3]
#	>>> y = [4, 5, 6]
#	>>> zipped = zip(x, y)
#	>>> zipped
#	[(1, 4), (2, 5), (3, 6)]
#	>>> x2, y2 = zip(*zipped)
#	>>> x == list(x2) and y == list(y2)
#	True
#	>>> zip(['0100','1110','0010'])  --  x = ['0100','1110','0010']， y = []
#	[('0100',), ('1110',), ('0010',)]
#	>>> zip(*['0100','1110','0010']) -- x = '0100', y = '1110', z = '0010'
#	[('0', '1', '0'), ('1', '1', '0'), ('0', '1', '1'), ('0', '0', '0')]
#   b.count('0') * b.count('1') -- calculate hamming distance of corresponding bit
#   ('0', '1', '0'): 2 * 1 = 2, 3 numbers, 3 pairs, (0,1) * 2 + (0,0) -> 2

## one line Solution from discussion
def totalHammingDistance(self, nums):
    return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))