# QUESTION:
# We have a loud talking parrot.
# The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble.

# --------------------------------------------------------------------------------
# given,
# def parrot_trouble(talking, hour):
# --------------------------------------------------------------------------------

def parrot_trouble(talking, hour):
    if talking and (0<=hour<7 or 20<hour<24):
        return True
    else:
        return False
