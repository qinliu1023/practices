"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
	Input: "USA"
	Output: True
Example 2:
	Input: "FlaG"
	Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count_capitals = 0
        for i in word:
            if i.isupper() == True:
                count_capitals += 1
        
        if count_capitals == 0:
            return True
        elif count_capitals == len(word):
            return True
        elif count_capitals > 1:
            return False
        elif count_capitals == 1 and word[0].isupper() == True:
            return True
        else:
            return False