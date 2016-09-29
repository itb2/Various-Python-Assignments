'''
Created on Mar 31, 2015

@author: Ivory
'''
def emailsLargest(courses):
    coursess = []
    for strng in courses:
        coursess.append(strng.split(":"))
    num = []
    for course in coursess:
        occur = coursess.count(course)
        num.append(occur)
    maxx = max(num)
    countmax = 0
    maxind = 0
    num = num.sort()
    final = []
    for int in num:
        maxind = 0
        if int == maxx:
            countmax += 1
            for t in coursess:
                maxind = coursess.find[t,2]
                final.append(coursess[maxind])
                
                
    return final
        
            
        
        