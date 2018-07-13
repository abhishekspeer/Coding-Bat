# QUESTION:
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.



# --------------------------------------------------------------------------------
# given,
# def makes10(a, b):
# --------------------------------------------------------------------------------

# Solution 1
def makes10(a, b):
    return (a+b == 10 or a==10 or b==10)



#Solution 2
def makes10(a, b):
    if (a+b == 10) or (a == 10) or (b == 10):
        return True
    else:
        return False
