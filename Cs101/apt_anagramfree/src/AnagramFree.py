'''
Created on Feb 27, 2015

@author: Ivory
'''
def getMaximumSubset(words):
    maxlist = set()
    for i in words:
        b = []
        for c in i:
            b.append(c)
            
        b.sort()
        maxlist.add("".join(b))
    
    return len(maxlist)


#Lists are unhashable, maybe im confused about the instructions??

       
        