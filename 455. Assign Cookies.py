"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. Each child i has a greed factor gi, 
which is the minimum size of a cookie that the child will be content with; and 
each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, 
and the child i will be content. Your goal is to maximize the number of your content children 
and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

Example 1:
	Input: [1,2,3], [1,1]
	Output: 1
	Explanation: 
		You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
		And even though you have 2 cookies, since their size is both 1, you could only make the child 
		whose greed factor is 1 content.
		You need to output 1.

Example 2:
	Input: [1,2], [1,2,3]
	Output: 2
	Explanation: 
		You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
		You have 3 cookies and their sizes are big enough to gratify all of the children, 
		You need to output 2.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # to max nums of children content, order children by their greed factor
        # and then order cookies by their size
        # assign cookies to children from left to right, and inner loop stops when a cookie is assigned 
        # outer loop stops when all cookies has been checked, or when all children get a cookie
        # children greed factor: [1,2,3,4,5,6], cookies size [1,7,8,9], assign 1->1, 7->2, 8->3 and 9->4
        # children greed factor: [1,2,3,4,5,6], cookies size [1,5,5,5], assign 1->1, 5->2, 5->3, and 5->4
        # children greed factor: [2,2,3,4,5,6], cookies size [1,1,5,5], assign 5->2, and 5->2
        # children greed factor: [1,2,3], cookies size [1,7,8,9], assign 1->1, 7->2, 8->3 and break & return
        # children greed factor: [2,2,3], cookies size [1,1,1,1]
        num_children = len(g)
        num_cookies = len(s)
        num_content_children = 0
        
        g.sort()
        s.sort()
        child_start = 0
        for i in range(num_cookies):
            for j in range(child_start, num_children):
                if s[i] >= g[j]:
                    num_content_children += 1
                    child_start += 1
                    break
            if num_content_children == num_children:
                break
        return  num_content_children     

# Simplified to following 
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        num_content_children = 0
        
        g.sort()
        s.sort()

        for i in range(len(s)):
            for j in range(num_content_children, len(g)):
                if s[i] >= g[j]:
                    num_content_children += 1
                    break
            if num_content_children == len(g):
                break
        return  num_content_children            

# Got an error: Time Limit Exceeded for test case 
# After checking the loop, I found I am trying to assign a cookie to a child instead of getting a child a cookie
# This caused a problem that when a cookie is too small to meet the smallest greed factor of g, 
# the loop will still check each element of g, this will lead to a waste of time
# to avoid this time wasting problem, I changed the code, so that for a given child c, I will loop cookie size
# until position k where g[c] == s[k], then I move the pointer of cookie to position k
# as g and s are both sorted, cookies before k will not make children behind c content
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        num_content_children = 0
        num_cookies_pointer = 0
        
        g.sort()
        s.sort()

        for j in range(len(g)):
            for i in range(num_cookies_pointer, len(s)+1):
                if s[i] >= g[j]:
                    num_content_children += 1
                    num_cookies_pointer = i + 1
                    break
            if num_cookies_pointer > len(s):
            	break
        return  num_content_children     


""" Another simple solusion from discussion        
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i    
"""
