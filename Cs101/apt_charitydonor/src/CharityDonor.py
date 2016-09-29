'''
Created on Mar 31, 2015

@author: Ivory
'''

def nameDonor(contributions):
    for n in contributions:
        n = n.lower()
    contributions.sort()
    print contributions
    

nameDonor([["Zack:800.00", "Gregory:900.00"]])