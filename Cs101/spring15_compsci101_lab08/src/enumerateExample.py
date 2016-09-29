'''
Created on Mar 16, 2015

@author: Susan
'''
def listOfTuples(alist):
# returns a list of the enumerated tuples of (index,item)
    returnList = []
    for (index,item) in enumerate(alist):
        returnList.append((index,item))
    return returnList

names = ['Fred', 'John', 'Sue']
print listOfTuples(names)