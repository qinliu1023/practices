"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
	Input: "Hello World"
	Output: 5
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == "" or s == " ":
            return 0
        elif s[n-1] == " " and s[n-2] == " ":
            return 0 
        else:
            s_word_list = s.split()
            return len(s_word_list[len(s_word_list)-1])
# test failed when s = "b   a    " (expected 1, returned 0)
# Confused about the "If the last word does not exist, return 0." 
# And take strings ending with more than 2 spaces as the situation when the last word does not exist

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # remove all spaces before or ending
        s_removed_space = s.strip()
        s_word_list = s_removed_space.split()
        if len(s_word_list) == 0:
            return 0
        else:
            return len(s_word_list[len(s_word_list)-1])       