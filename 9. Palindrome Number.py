"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # change x to str to use index
        # 'int' object has no attribute '__getitem__', x[k] will get a TypeError
        # 'int' object is not iterable, list(x) will return a TypeError
        n = len(str(x))
        # x can ben classified into 3 types, negative, Multiples of 2, Not Multiples of 2
        # Negative Integer is not a Palindome
        # Other integers can be classified by checing the paired number, x[k] and x[n-1-k]
        # if all are the same, then its palindorme, otherwise, not palindorme
        if x >= 0 and n % 2 == 0:
            for i in range(n/2):
                if str(x)[i] != str(x)[n-1-i]:
                    return False
        elif x >= 0 and n % 2 == 1:
            for i in range((n-1)/2):
                if str(x)[i] != str(x)[n-1-i]:
                    return False
        else:
            return False
            
        return True

# Simplified to the below one, when x is non-negative,
# for example, if n is 4, we check (a[0], a[3]) and (a[1], a[2]), 
# if n is 3, we check (a[0], a[2]), and (a[1], a[1]), then we can combine 
# situations when n is an odd and an even, the limit is floor(n/2)        
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        n = len(str(x))
        i = 0
        while i <= (n/2):
            if str(x)[i] != str(x)[n-1-i]:
                return False
            i += 1
        return True
        
# 234. Palindrome Linked List
"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        
        val_list = []
        curr_node = head
        while curr_node != None:
            val_list.append(curr_node.val)
            curr_node = head.next

        
        n = len(val_list)  
        i = 0
        while i <= (n/2):
            if val_list[i] != val_list[n-1-i]:
                return False
            i += 1
            
        return True
    # This got a warning of Run Out of Time. And also doens't meet the reqirement of O(1) Space   


# 125. Valid Palindrome
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # first we create a set containing all lower case valid alphanumeric characters
        valid_letters = list("abcdefghijklmnopqrstuvwxyz0123456789")
        valid_letters = set(valid_letters)
        # As we ignore cases, we can use upper() or lower() to make letters in consistent format
        s_cleaned = ""
        for x in s:
            if x.lower() in valid_letters:
                s_cleaned = s_cleaned + x.lower() # assign updated
            
        n = len(s_cleaned)
        if n == 0:
            return True
        
        i = 0
        while i <= (n/2):
            if s_cleaned[i] != s_cleaned[n-1-i]:
                return False
            i += 1    
        return True          
        # This got a warning of Run Out of Time. And also doens't meet the reqirement of O(1) Space   

# There is a method isalnum() can check whether the string consists of alphanumeric characters.
# From discussion part one accepted is listed below
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front, end = 0, len(s)-1
        while front < end:
            while front < end and s[front].isalnum() == False:
                front += 1
            while front < end and s[end].isalnum() == False:
                end -= 1
            if s[front].lower() != s[end].lower():
                return False
            front +=1; end -= 1
        return True         
