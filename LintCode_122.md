## LintCode 122 Problems


### 1-String

#### 158. Two Strings Are Anagrams 
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Clarification
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.

Example
Given s = "abcd", t = "dcab", return true.
Given s = "ab", t = "ab", return true.
Given s = "ab", t = "ac", return false.
```python
class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        return sorted(s) == sorted(t)
```

#### 55. Compare Strings
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Notice
The characters of B in A are not necessary continuous or ordered.

Example
For A = "ABCD", B = "ACD", return true.

For A = "ABCD", B = "AABC", return false.
```python
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        # For A = "AABCD", B = "ABCC", return false.
        # set up a dictionary, iterate in A and then in B
        # Letter in A add 1, letter in B minus 1
        dict_a = {}
        for letter in A:
            if letter not in dict_a.keys():
                dict_a[letter] = 1
            else:
                dict_a[letter] += 1
            
        for i in B:
            if i not in dict_a:
                return False
            else:
                if dict_a[i] <= 0:
                    return False
                else:    
                    dict_a[i] -= 1
        
        return True    
```

#### 171. Anagrams 
Given an array of strings, return all groups of strings that are anagrams.

Notice
All inputs will be in lower-case

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].
Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

What is Anagram? - Two strings are anagram if they can be the same after change the order of characters.
```python
class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        import collections
        anagrams_dic = collections.defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagrams_dic[key].append(word)
        
        output = []
        values = anagrams_dic.values()
        for i in range(len(values)):
            if len(values[i]) > 1:
                output.extend(values[i])
        
        return output  
```

#### 78. Longest Common Prefix 
Given k strings, find the longest common prefix (LCP).

Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
```python
class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        k = len(strs)
        
        # Change str to a list of lists
        strs_list = []
        for string in strs:
        	string_list = []
        	for i in range(len(string)):
        		string_list.extend(string[i])
        	strs_list.append(string_list)	
        
        # Zip lists so that letters at the same position are in one list
        # e.g. "ABC" and "ABD" -> [(A,A),(B,B],(C,D)]
        zipped = zip(*strs_list)
        
        # Check common prefix
        common_prefix = ""
        for i in range(len(zipped)):
        	if zipped[i].count(zipped[i][0]) == k:
        		common_prefix += zipped[i][0]
        	else:
        		return common_prefix
        return common_prefix		
```

#### 13. strStr 
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Clarification
Do I need to implement KMP Algorithm in a real interview?

- Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge 
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
```python
class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        
        for i in range(len(source) - len(target) + 1):
            if source[i:i+len(target)] == target:
                return i
        return -1 
```
##### LeetCode: 28. Implement strStr()
Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
	Input: haystack = "hello", needle = "ll"
	Output: 2

Example 2:
	Input: haystack = "aaaaa", needle = "bba"
	Output: -1
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```
[KMP](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)

Here is another solution using nested loop [link](https://algorithm.yuanbin.me/en/string/strstr.html#python)

#### 79. Longest Common Substring
Given two strings, find the longest common substring.

Return the length of it.

Notice
The characters in substring should occur continuously in original string. This is different with subsequence.

Example
Given A = "ABCD", B = "CBCE", return 2.

Challenge 
O(n x m) time and memory.
```python

```
[Algorithm Implementation/Strings/Longest common substring](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring)

[jiuzhang.com](https://www.jiuzhang.com/solution/longest-common-substring/#tag-highlight-lang-python)

[Telling the length of the highest common substring](https://codereview.stackexchange.com/questions/179668/telling-the-length-of-the-highest-common-substring-between-2-words)




### 2-Integer Array

#### 172. Remove Element 
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        try:
            while True:
                A.remove(elem)
        except:
            return len(A)
            
```
##### LeetCode: 27. Remove Element

#### 138. Subarray Sum
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Notice
There is at least one subarray that it's sum equals to zero.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
```python
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        for i in range(len(nums)):
            if nums[i] == 0:
                return [i,i]
                
            subarr_sum = nums[i]
            right = i+1
            while right < len(nums):
                subarr_sum += nums[right]
                if subarr_sum == 0:
                    return [i,right]
                else:
                    right += 1
```

#### 100. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        # Examples: [1,1,2] -> [1,2]
        # [1,2,3,3,4,5,5,7] -> [1,2,3,4,5,7,x,x]
        # loop from begin to end, each time a new num is encountered, then move it to front
        
        if len(nums) == 0:
            return 0
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1        
```
##### LeetCode: 26. Remove Duplicates from Sorted Array

#### 64. Merge Sorted Array
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Notice
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
```python
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # add B to A
        A[m:] = B[:n]
        return A.sort()
```
##### LeetCode: 88. Merge Sorted Array

#### 56. Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

Notice
You may assume that each input would have exactly one solution

Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

Challenge 
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
```python
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)):
            for j in range(i):
                if numbers[i] + numbers[j] == target:
                    return [j,i]
```

#### 50. Product of Array Exclude Itself 
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A = [1, 2, 3], return [6, 3, 2]
```python
class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
       
        n = len(nums)
        
        # consider left side first, get a list of array
        # in which each value is the product of its left numbers
        # for example: [1,2,3,4] -> [1,1,2,6] name as left_product
        # left_product[2] = nums[0]*nums[1]
        # left_product[3] = nums[0]*nums[1]*nums[2]
        multipler = 1
        left_product = []
        for i in range(0,n):
            left_product.append(multipler)
            multipler = multipler * nums[i]
        
        # Then take right into consideration
        # right is a integer and records the product of all elements at i's right
        product = left_product
        right = 1
        for i in range(n-1,-1,-1):
            product[i] = product[i] * right
            right = right * nums[i]
        
        return product
```
##### LeetCode: 238. Product of Array Except Self, [YouTube](https://www.youtube.com/watch?v=DNE_Gseit9s)

#### 189. First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

Example
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Challenge 
Your algorithm should run in O(n) time and uses constant space.
```python
class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)
        
        # [98,99,100] -> return 1
        # 0 is not positive
        # n = len(A) then should contain 1,2,3,...,n
        # if A = [1,2,3,...,n], then return n+1
        # index [0,1,2,3,4]
        # number should be [1,2,3,4,5]
        # the first missing positive is the position where the number != index + 1
        if not A:
            return 1
            
        # move all nums to the position where index = nums - 1
	# A[i] > 0 and A[i] <= n -> make sure A[i] is in range
	# A[i] != i + 1 -> check whether it is at right place
	# A[i] != A[A[i] - 1] -> make sure the num on A[i]'s right position is not 
	#                        the same as A[i], otherwise, there is no meaning to switch
        for i in range(n):
            while A[i] > 0 and A[i] <= n and \
              A[i] != i + 1 and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        
        for i in range(n):
            if i + 1 != A[i]:
                return i + 1
        
        return n + 1  
```
##### LeetCode: 41. First Missing Positive, [YouTube](https://www.youtube.com/watch?v=jfb72FfxWKU)

#### 59. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Notice
You may assume that each input would have exactly one solution.

Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge 
O(n^2) time, O(1) extra space
```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        
        closest = numbers[0] + numbers[1] + numbers[2]
        
        for i in range(len(numbers)-2):
            low = i+1
            high = len(numbers)-1
            
            while low < high:
                sums = numbers[i] + numbers[low] + numbers[high]
                if sums > target:
                    high -= 1
                else:
                    low += 1
                if abs(closest-target) > abs(sums-target):
                    closest = sums
        
        return closest
```
##### LeetCode: 16. 3Sum Closest, [YouTube](https://www.youtube.com/watch?v=nk6DuCxb8zI)

#### 57. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
```python
class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        # fix one number and find another two equals 0-number
        # as elements in a triplet must be in non-descending order
        # sort numbers first
        numbers.sort()
        
        output = []
        for i in range(len(numbers)-2):
            # duplicat triplet should not be contained
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            
            low = i + 1
            high = len(numbers)-1
            two_sums = 0- numbers[i]
            
            while low < high:
                if numbers[low] + numbers[high] == two_sums:
                    output.append((numbers[i],numbers[low], numbers[high]))
                    while low < high and numbers[low] == numbers[low+1]:
                        low += 1
                    while low < high and numbers[high] == numbers[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif numbers[low] + numbers[high] < two_sums:
                    low += 1
                else:
                    high -= 1
        
        return output        
```
##### LeetCode: 15.3Sum, [YouTube](https://www.youtube.com/watch?v=mNzUMPBiRX4)

#### 31. Partition Array
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Notice
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge 
Can you partition the array in-place and in O(n)?
```python
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here

        # need to return first index i nums[i] >= k.
        # final nums could be [1,2,3,6,5,7], k = 5
        # no need to be [1,2,3,5,6,7], k = 5
        # no need for i > k locates at right of i
        # and for i < k locates at left of i
        low = 0
        high = len(nums)-1
        
        while low <= high:
            # once find the first low where nums[low] >=  k 
            # goes to second inner while and find the first high where nums[high] < k
            # if low < high, swith their values, and update low and high by +/- 1
            # then goes to outer while check whether low <= high or not
            # if true, goes to inner whiles to find the 2nd, 3rd,... pair of low and high
            # and do number switch
            while low <= high and nums[low] < k: 
                low += 1
            while low <= high and nums[high] >= k:
                high -= 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        
        return low
```

[Difference between sorted() and .sort()](https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort-python)

### 3-Binary Search

#### 141. Sqrt(x) 
Implement int sqrt(int x).

Compute and return the square root of x.

Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

Challenge 
O(log(x))
```python
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        
        low, high = 1, x
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        if high * high < x:
            return high
        else:
            return low
        
```
##### LeetCode: 69. Sqrt(x), [YouTube](https://www.youtube.com/watch?v=RR0Af3CTNhE)


#### 60. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

Challenge 
O(log(n)) time

```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        
        n = len(A)
        if A[n-1] < target:
            return n
        elif A[0] >= target:
            return 0
        else:
            for i in range(len(A)):
                if A[i] < target and A[i+1] >= target:
                    return i+1
```                    
##### LeetCode: 35. Search Insert Position


#### 28. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge 
O(log(n) + log(m)) time
```python
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        # rows = len(matrix)
        # cols = len(matrix[0])
        
        if not matrix or len(matrix) == 0:
            return False
            
        matrix_to_list = []
        rows = len(matrix)
        for i in range(rows):
            matrix_to_list.extend(matrix[i])
        
        cols = len(matrix[0])
        
        left, right = 0, rows * cols - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if matrix_to_list[mid] == target:
                return True
            elif matrix_to_list[mid] < target:
                left = mid
            else:
                right = mid
        
        if matrix_to_list[left] == target:
            return True
        elif matrix_to_list[right] == target:
            return True
        else:
            return False
```
##### LeetCode: 74. Search a 2D Matrix, [YouTube](https://www.youtube.com/watch?v=F8nwWNRCVkE)
Above Code has a RunTime Error in LeetCode.
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        begin, end = 0, rows*cols-1
        while begin <= end:
            mid = (begin + end) / 2
            i, j = mid / cols, mid % cols
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                begin = mid + 1
            else:
                end = mid - 1
        
        return False
"""
rows = 3, cols = 4
begin, end = 0, 11
mid = 5 --> i, j = 5/4, 5%4 = 1, 1
			mid = i * cols + j
"""        
```

#### 14. First Position of Target 
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge 
If the count of numbers is bigger than 2^32, can your code work properly?
```python
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        low, high = 0, len(nums)-1
        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        
        if nums[low] == target :
            return low
        elif nums[high] == target :
            return high
        return -1;
```
#### 159. Find Minimum in Rotated Sorted Array 
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Notice
You may assume no duplicate exists in the array.

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
        return nums[0]

### Using Binary Search
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left, right = 0, len(nums)-1
        
        # Only need to consider right "half" of the array
        while left + 1 < right:
            mid = (left + right) / 2              
            if nums[mid] < nums[right]:
                right = mid
            else:
            	left = mid + 1    


        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
```
##### Leetcode: 153 Find Minimum in Rotated Sorted Array

#### 62. Search in Rotated Sorted Array 
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge 
O(logN) time
```python
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return -1
        
        left, right = 0, len(A)-1
        
        while left + 1 < right:
            mid = (left + right) / 2
            if A[mid] == target:
                return mid
            if A[left] < A[mid]:# left to mid is in ascending order
                if A[left] <= target and target <= A[mid]:
                    right = mid
                else:    
                    left = mid
            else: # mid to right is in ascending order
                if A[mid] <= target and target <= A[right]:
                    left = mid
                else:    
                    right = mid
 
        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        else:
            return -1    
```
##### LeetCode: 33. Search in Rotated Sorted Array

#### 61. Search for a Range 
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Challenge 
O(log n) time.
```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0 or A[0] > target or A[len(A)-1] < target:
            return [-1,-1]
            
        left, right = 0, len(A)-1
        while left + 1 < right:
            mid = (left+ right)/2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
        if A[left] == target:
            low = left
        elif A[right] == target:
            low = right
        else:
            low = -1
        
        left, right = 0, len(A)-1
        while left + 1 < right:
            mid = (left+ right)/2
            if A[mid] <= target:
                left = mid
            else:
                right = mid
        if A[right] == target:
            high = right
        elif A[left] == target:
            high = left
        else:
            high = -1
            
        return [low, high]
```
##### LeetCode: 34. Search for a Range

#### 74. First Bad Version 
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Notice
Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)

Example
Given n = 5:

isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
Here we are 100% sure that the 4th version is the first bad version.

Challenge 
You should call isBadVersion as few as possible.
```python
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""

class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        left = 1
        right = n
        while left + 1 < right:
            mid = (right+left)/2
            if SVNRepo.isBadVersion(mid) == True:
                right = mid 
            else:
                left = mid
                
        if SVNRepo.isBadVersion(left) == True:
            return left
        else:
            return right 
```
##### LeetCode: 278. First Bad Version

#### 75. Find Peak Element 
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Notice
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.

Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)

Challenge 
Time complexity O(logN)
```python
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 0, len(A)-1
        while left + 1 < right:
            mid = (left + right) / 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid + 1  

        if A[left] > A[right]:
            return left
        else:
            return right
```
##### LeetCode: 162. Find Peak Element


#### 183. Wood Cut 
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Notice
You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Example
For L=[232, 124, 456], k=7, return 114.

Challenge 
O(n log Len), where Len is the longest length of the wood.
```python
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        
        # if the total length of given wood is less than k
        # we could not get >= k pieces
        if sum(L) < k:
            return 0
            
        maxLen = max(L)
        low, high = 1, max(L)
        
        # find number of pieces we can get for a possible small piece
        # for length x in range(low, high), we add up L[i]/x, i in range(len(L))
        # get sum[x], if sum[x] >= k, the x is one candicate
        # after tranverse all possible x, we choose the largest one
        # using binary search, to reduce complexity
        while low + 1 < high:
            mid = (low + high) / 2
            
            small_piece_nums = 0
            for length in L:
                small_piece_nums += (length/mid)
           
            if small_piece_nums >= k:
                low = mid
            else:
                high = mid
                
        if sum([length / high for length in L]) >= k:
            return high
        return low
```

### 4-Math & Bit Manipulation
#### 181. Flip Bits 
Determine the number of bits required to flip if you want to convert integer n to integer m.

Notice
Both n and m are 32-bit integers.

Example
Given n = 31 (11111), m = 14 (01110), return 2.
```python
class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        c = a ^ b 
        cnt = 0   
        for i in xrange(32):
            if c & (1 << i) != 0: 
                cnt += 1		  
        return cnt
# copies the bit if it is set in only a or only b.
# &: copies a bit to the result if it exists in both operands        
# <<: The left value is moved left by the number of bits specified by the right value. 
"""
e.g. 
a = 60            # 60 = 0... 0011 1100 
b = 13            # 13 = 0... 0000 1101 
c = a ^ b;        # 49 = 0... 0011 0001

index 			  0            31 					
i = 0 --> 1 << i: 0... 0000 0001 --> c & i != 0 checks whether bit at c[31], 
									 if returns 0, c[31] == 0, means a and b are the same at this postion
i = 1 --> 1 << i: 0... 0000 0010 --> 
i = 2 --> 1 << i: 0... 0000 0100 --> 
"""
```
##### [jiuzhang.com](http://www.jiuzhang.com/solution/flip-bits/#tag-highlight-lang-python)
##### [Bitwose Operation Examples](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)
##### [Python Basic Operators]（https://www.tutorialspoint.com/python/python_basic_operators.htm）


#### 142. O(1) Check Power of 2 
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;

For n=5, return false;

Challenge 
O(1) time
```python
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        # power of two: 0001, 0010, 0100, 1000
        # 2^(i+1) is 2^i move left by 1 position
        # set value equal to 1 and move left by 1 each time
        # compare input n with value
        # 32 bits, max 2^31 − 1
        value = 1
        for i in xrange(31):
            if value == n:
                return True
            value = value << 1
 
        return False 
```


#### 2. Trailing Zeros 
Write an algorithm which computes the number of trailing zeros in n factorial.

Example
11! = 39916800, so the out should be 2

Challenge 
O(log N) time
```python

```
##### [jiuzhang](http://www.jiuzhang.com/solution/trailing-zeros/#tag-highlight-lang-python)
##### [Blog](http://blog.csdn.net/surp2011/article/details/51168272)


#### 179. Update Bits 
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N located at i and starting at j)

Notice
In the function, the numbers N and M will given in decimal, you should also return a decimal number.

Clarification
You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2

Challenge 
Minimum number of operations?
```python
```
##### [jiuzhang](http://www.jiuzhang.com/solution/update-bits/#tag-highlight-lang-python)


#### 163. Unique Binary Search Trees 
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
```python
```
##### [jiuzhang](http://www.jiuzhang.com/solution/unique-binary-search-trees/#tag-highlight-lang-python)

#### 140. Fast Power 
Calculate the a^n % b where a, b and n are all 32bit integers.

Example
For 2^31 % 3 = 2

For 100^1000 % 1000 = 0

Challenge 
O(logn)
```python
```
##### [jiuzhang](http://www.jiuzhang.com/solution/fast-power/#tag-highlight-lang-python)


#### 180. Binary Representation 
Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string. If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.

Example
For n = "3.72", return "ERROR".

For n = "3.5", return "11.1".
```python

```
##### [jiuzhang](http://www.jiuzhang.com/solution/binary-representation/#tag-highlight-lang-python)

### 5-Greedy
#### 82. Single Number
Given 2\*n + 1 numbers, every numbers occurs twice except one, find it.

Example
Given [1,2,2,1,3,4,3], return 4

Challenge 
One-pass, constant extra space.
```python
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        return 2 * sum(set(A)) - sum(A)
```
##### LeetCode: 136. Single Number


#### 46. Majority Number 
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

Notice
You may assume that the array is non-empty and the majority number always exist in the array.

Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

Challenge 
O(n) time and O(1) extra space
```python
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        # use a dictionary to store num and its frequency
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict.keys():
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        
        values = sorted(nums_dict.values()) 
        
        max_freq = values[len(values)-1]
        
        for key in nums_dict.keys():
            if nums_dict[key] == max_freq:
                return key

# Solution 2
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        # using count
        max_freq = 1
        output = nums[0]
        for num in nums:
            if max_freq < nums.count(num):
                max_freq = nums.count(num)
                output = num
        return output        

```

#### 187. Gas Station 
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Notice
The solution is guaranteed to be unique.

Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.

Challenge 
O(n) time and O(1) extra space
```python


```
##### LeetCode: 134. Gas Station

#### 184. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Notice
The result may be very large, so you need to return a string instead of an integer.

Example
Given \[1, 20, 23, 4, 8], the largest formed number is 8423201.

Challenge 
Do it in O(nlogn) time complexity.
```python
```
##### LeetCode: 179. Largest Number
####### [Sort() using cmp](https://stackoverflow.com/questions/34159437/sort-in-python-using-cmp)
####### [How to Sorting](https://wiki.python.org/moin/HowTo/Sorting)
####### [cmp()](https://docs.python.org/2/reference/datamodel.html#object.__cmp__)
####### [lambda](https://docs.python.org/3.5/tutorial/controlflow.html#lambda-expressions)

#### 182. Delete Digits 
Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.

N <= 240 and k <= N,

Example
Given an integer A = "178542", k = 4

return a string "12"
```python
class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, l):
        # write your code here
        # if numbers in string A is in ascending order
        # remove last k digits will lead to the samllest integer
        # if numbers in string A is i n random order
        # remove A[i] if A[i] > A[i+1]

        A = list(A)
        while l > 0:
            f = True
            for i in xrange(len(A)-1):
                if A[i] > A[i+1]:
                    del A[i]
                    f = False
                    break     
            if f and len(A)>1:
                A.pop()
            l -= 1
        while len(A)>1 and A[0]=='0':
            del A[0]
        return ''.join(A)
```

#### 116. Jump Game 
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Notice
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

Example
A = \[2,3,1,1,4], return true.

A = \[3,2,1,0,4], return false.
```python
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # find out the maximum jump at current position
        
        max_pos = 0

        for i in range(len(A)):
            if i > max_pos:
                return False
            max_pos = max(A[i] + i, max_pos)

        return True  
```
##### LeetCode: Leetcode 55 Jump Game, [YouTube](https://www.youtube.com/watch?v=C8Cydo3NfgM)


#### 52. Next Permutation 
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

Notice
The list may contains duplicate integers.

Example
For \[1,3,2,3], the next permutation is \[1,3,3,2]

For \[4,3,2,1], the next permutation is \[1,2,3,4]
```python

```
##### LeetCode: 31 Next Permutation, [YouTube](https://www.youtube.com/watch?v=9mdoM2dVid8)




### 6-Linked List
### 7-Binary Tree
### 8-Search & Recursion
### 9-Dynamic Programming
### 10-Data Structure
