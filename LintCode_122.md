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
            subarr_sum = nums[i]
            j = i-1
            while j >= 0 and subarr_sum != 0:
                subarr_sum += nums[j]
                j -= 1
            return [j+1,i] # Wrong Answer
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
##### LeetCode: 238. Product of Array Except Self
[Youtube](https://www.youtube.com/watch?v=DNE_Gseit9s)

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
        for i in range(n):
            while A[i] > 0 and A[i] <= n and \
              A[i] != i + 1 and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        
        for i in range(n):
            if i + 1 != A[i]:
                return i + 1
        
        return n + 1  
```
##### LeetCode: 41. First Missing Positive, [youtube](https://www.youtube.com/watch?v=jfb72FfxWKU)

#### 59. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Notice
You may assume that each input would have exactly one solution.

Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge 
O(n^2) time, O(1) extra space
```python

```

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

```

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

```

[Difference between sorted() and .sort()](https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort-python)

### 3-Binary Search
### 4-Math & Bit Manipulation
### 5-Greedy
### 6-Linked List
### 7-Binary Tree
### 8-Search & Recursion
### 9-Dynamic Programming
### 10-Data Structure
