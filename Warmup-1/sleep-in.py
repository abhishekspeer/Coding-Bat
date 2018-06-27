# QUESTION:
# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.
# sleep_in(False, False) → True | sleep_in(True, False) → False | sleep_in(False, True) → True
# --------------------------------------------------------------------------------

# given,
# def sleep_in(weekday, vacation):
# --------------------------------------------------------------------------------

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    # accounts for 3 cases
    else:
        return False
    # account for 1 case(True, False) returning False as the Output.

# NOTE: not weekday = False and vacation = True; if any one of the conditions
# are satisfied we will get True. so we need (false , true), where at least one
# should be valid.
