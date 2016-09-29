'''
Created on Mar 17, 2015

@author: Ivory
'''
def namesForYear(courses, year):
    b = set()
    for i in courses:
        i.split(":")
        for x in i:
            if x == year:
                n = i.index(x)
                b.add(i[n-1])
    strng = ""
    for p in b:
        strng = strng + p + " "
        
    return strng