def question1(s,t):
# if s is empty, then we should always get a False
# if s is shorter than t, then we should always get a False
# if t is empty, then we should always get a True
    if len(s) == 0:
        return False
    if len(s) < len(t):
        return False 
    if len(t) == 0:
        return True
# divide string s into consecutive letters with length len(t), for example
# when s = "udacity" and t = "adc", we will divide s into ["uda", "dac", "aci", "cit", "ity"]
# if length s is n and length t is m, we will get (n-m+1) substrings
# And each of this string will be turned into lists for comparison
# Also we will use a count function to find out the frequency of each letter in a string
# And all the data will be stored into a dictionary
    t_letter_dict = letter_count(t)
    s_list = list(s)
    is_substring = 0
    for i in range(len(s)-len(t)+1):
        new_sub = s_list[i:i+len(t)]
        i += 1 
        new_sub_letter_dict = letter_count(new_sub)
# Here a function to compare two dictionaries are applied
# if these two are the same, and the True is returned, Otherwise, a False is returned
        if dict_compare(t_letter_dict, new_sub_letter_dict) == True:
            is_substring += 1
    if is_substring > 0:
        return True
    else:
        return False
        

####### help functions ######
def letter_count(letter_list):
    letter_dict = {}
    for k in letter_list:
        if k not in letter_dict.keys():
            letter_dict[k] = 1
        else:
            letter_dict[k] += 1  
    return letter_dict

    
def dict_compare(dict1, dict2):
    matched_letters = 0
    if len(dict1.keys()) != len(dict2.keys()):
        return False
    else:     
        for letter in dict1.keys():
            if letter not in dict2.keys():
                return False
            elif dict1[letter] == dict2[letter]:
                matched_letters += 1
        if matched_letters == len(dict1.keys()):
            return True

####### Test Cases ######
print question1("udacity", "ad")
print question1("udacity", "adc")
print question1("udacity", "aui")
print question1("udacity", "xyz")
"""
should be:
    True
    True
    False
    False
"""