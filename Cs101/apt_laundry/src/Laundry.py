'''
Created on Jan 29, 2015

@author: Ivory
'''
def minutesNeeded(m): 
    """
    Return integer number of minutes to launder m (integer) loads
    """

    # you write code here
    time = 0
    if m == 0:
        return 0
    else:
        for i in range(m):
            time = time + 25
        return time