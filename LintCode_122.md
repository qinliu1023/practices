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
### 3-Binary Search
### 4-Math & Bit Manipulation
### 5-Greedy
### 6-Linked List
### 7-Binary Tree
### 8-Search & Recursion
### 9-Dynamic Programming
### 10-Data Structure
