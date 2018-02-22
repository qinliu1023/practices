"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
	Input: "aba"
	Output: True

Example 2:
	Input: "abca"
	Output: True
	Explanation: You could delete the character 'c'.

Note:
	The string will only contain lowercase characters a-z. 
	The maximum length of the string is 50000.
"""



## Solution 
"""
Intuition

If the beginning and end characters of a string are the same (ie. s[0] == s[s.length - 1]), 
then whether the inner characters are a palindrome (s[1], s[2], ..., s[s.length - 2]) 
uniquely determines whether the entire string is a palindrome.

Algorithm

Suppose we want to know whether s[i], s[i+1], ..., s[j] form a palindrome. 
If i >= j then we are done. If s[i] == s[j] then we may take i++; j--. 
Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], 
and we should check both cases.
"""
class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in xrange(len(s) / 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True