'''
Created on Apr 12, 2015

@author: Ivory
'''

def aulist(parents,target):
    """
    return list of strings based on
    parents, a list of strings, and
    target, a string
    """
      
    # you write code here
    
    "Figure out all of target's aunts and uncles"
    setauntsuncles = set()
    auntsuncles = []
    n = 0
    for item in parents:
        parents[n] = item.split()
        n +=1
        if item[-1] == target:
            parent1 = item[0]
            parent2 = item[1]
            parentsparents = []
            for item in parents:
                if item[-1] == parent1 or item[-1] == parent2:
                    parentsparents.append(item[0])
                    parentsparents.append(item[1])
                for prnt in parentsparents:
                    if item[0]==prnt or item[1]==prnt:
                        setauntsuncles.add(item[-1])
    for things in setauntsuncles:
        auntsuncles.append(things)
    return auntsuncles
                    
                       
                    
                    
                    
                    
                    