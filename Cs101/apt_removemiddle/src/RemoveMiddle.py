'''
Created on Jan 29, 2015

@author: Ivory
'''
def shorten(name):
    """
    return the name with the middle name(s) removed. 
    name has at least one word. 
    """
      
    # you write code here
    p = name.split()
    y = len(p)
    return p[0] + " " + p[(y-1)]
      
