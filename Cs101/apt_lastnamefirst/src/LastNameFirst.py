'''
Created on Jan 29, 2015

@author: Ivory
'''
def modify(name):
    """
    return the name with the last name first, followed by a comma,
    followed by the first name (if any), followed by the first letter of
    each remaining name with a period after each letter. 
    name has at least one word. 
    """
      
    # you write code heref 
    p = name.split()
    
    if len(p) == 1:
        return str(p)
    else:
        
        t= p[len(p)-1] + ", "  + p[0]
        t = str(t)
        return t
    