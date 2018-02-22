"""
Given a string, you need to reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.

Example 1:
	Input: "Let's take LeetCode contest"
	Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space 
and there will not be any extra space in the string.
"""

"""
Split up the given string based on whitespaces and get a list of individual words
Then, reverse each individual string using string[::-1] and add them up. 
Finally, remove leading and trailing whitespaces
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ") # split into word list
        reversed_s = ""
        for word in word_list:
            reversed_word = word[::-1] # reverse each word
            reversed_s = reversed_s + reversed_word + " " # Add reversed word up
        return reversed_s.strip() # remove leading and trailing whitespaces
            
        
# One line Solution from Discussion
return ' '.join([i[::-1] for i in s.split(' ')])