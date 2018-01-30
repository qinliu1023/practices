def question2(a):
    if a == "":
        return "Error: String is Empty"
    else:     
        palindrome_list = []
        for i in range((len(a)+1)):
            for j in range(i):
                substring = a[j:i]
                n = len(substring)
    # when substring's length is even, we need to check each pair of letters are the same            
                if len(substring) % 2 == 0:
                    is_palindrome = 0
                    for k in range(n/2):
                        if substring[k] == substring[n-k-1]:
                            is_palindrome += 1
                    if is_palindrome == (n/2):
                        palindrome_list.append(substring)
    # when substring's length is odd, we need to check each pair of letters are the same except the middle one 
                if len(substring) % 2 == 1:
                    is_palindrome = 0
                    for k in range((n-1)/2):
                        if substring[k] == substring[n-k-1]:
                            is_palindrome += 1
                    if is_palindrome == ((n-1)/2):
                        palindrome_list.append(substring)

        max_len = len(palindrome_list[0])
        longest_parlin = palindrome_list[0]
        for palindrome_sub in palindrome_list:
            if len(palindrome_sub) <= max_len:
                continue
            else:
                max_len = len(palindrome_sub)
                longest_parlin = palindrome_sub

        return longest_parlin



####### Test Cases ######
print question2("abbaeedc") 
print question2("")
print question2("cdedca") 
"""
should be:    
    abba
    Error: String is Empty
    cdedc

"""