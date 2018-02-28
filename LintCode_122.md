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

### 4-Math & Bit Manipulation
### 5-Greedy
### 6-Linked List
### 7-Binary Tree
### 8-Search & Recursion
### 9-Dynamic Programming
### 10-Data Structure
