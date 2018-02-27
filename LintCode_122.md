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

Challenge 
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.
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





### 2-Integer Array
### 3-Binary Search
### 4-Math & Bit Manipulation
### 5-Greedy
### 6-Linked List
### 7-Binary Tree
### 8-Search & Recursion
### 9-Dynamic Programming
### 10-Data Structure
