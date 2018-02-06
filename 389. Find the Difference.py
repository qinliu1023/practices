"""
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
# The first thing come to mind is to loop and see which letter in t is not in s, 
# but this will not cover cases like "a", and "aa"
# Then I tried to combine s and t, and then count letter frequency, the letter with odd number of appearance is what we want
# but again, this is not efficient as I need to get a unique set first and then do count
# The finial idea here, is to compare letter frequencey in s and t, when they are not the same, then our letter stands out

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for k in t:
            if s.count(k) != t.count(k):
                return k
            


