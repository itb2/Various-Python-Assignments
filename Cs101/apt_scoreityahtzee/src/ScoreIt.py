'''
Created on Feb 6, 2015

@author: Ivory
'''

def maxPoints(toss):
    """
    return int representing the maximal Yahtzee
    score based on rolls in integer list toss
    """
    max= 0
    for n in range(1,7):
        p = toss.count(n)
        if p*n > max: 
            max = p*n
    return max