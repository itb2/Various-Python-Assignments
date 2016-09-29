'''
Created on Feb 27, 2015

@author: Ivory
'''

def getFortunate(a,b,c):
    set1 = set()  
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                sum = a[i] + b[j] + c[k]
                sum = str(sum)    
                l= 0
                strn = '58'
                for thing in sum:
                    if thing in strn:
                        l += 1
                if l == len(sum):
                    set1.add(sum)
    return len(set1)