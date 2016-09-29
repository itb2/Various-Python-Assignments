'''
Created on Mar 17, 2015

@author: Ivory
'''

def maxLength(letters):
    
    """
    return int based on String letters
    """
    # you write code here
    letterlist = []
    ind = 0
    for n in range(len(letters)):
        letterlist.append(letters[ind])
        ind+=1
    letterlist2 = letterlist[:]
    for i in letterlist:
        occur = letterlist.count(i)
        dist = len(letterlist)
        for num in range(occur):
            m = letterlist.index(i)
            q = (len(letterlist)-1)- m
            if q < dist:
                dist = q
            letterlist[m] = "1"
        for b in range(occur):
            if dist > (len(letterlist)/2):
                letterlist2.remove(letterlist2[0:m])
                final = ""
                for char in letterlist2:
                    final = final + char
                return final
                   
            else:
                letterlist2.remove(letterlist2[m:0])
                final = ""
                for char in letterlist2:
                    final = final + char
                return final
        
        