# QUESTION:
#Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# ------------------------------------------------------------------------------
# given,
# def front_back(str):
# ------------------------------------------------------------------------------

def front_back(str):
    # check if the string length in less than 2
    if len(str) <= 1:
        return str

     mid = str[1:len(str)-1]
     # can be written as str[1:-1]
     return str[len(str)-1] + mid + str[0]
