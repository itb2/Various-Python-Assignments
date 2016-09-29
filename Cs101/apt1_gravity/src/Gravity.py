'''
Created on Jan 22, 2015

@author: Ivory
HUNTER STARK
'''

def falling(time,velo):
    """
    return float indicating 
    number of meters an object has 
    fallen after being dropped/thrown
    with initial velocity given by 
    float parameter velo
    (given in meters/second)
    and after falling for float parameter 
    time seconds
    """
      
    # you write code here

    d = (velo*time) + 0.5*(9.8)*(time**2)
    
    return d