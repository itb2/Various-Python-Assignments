'''
Created on Feb 27, 2015

@author: Ivory
'''
def howManyLetters(phrase):
    list = phrase.split(" ")
    list1 = [x[0].lower() for x in list]
    set1= set(list1)
    
    return len(set1)
    