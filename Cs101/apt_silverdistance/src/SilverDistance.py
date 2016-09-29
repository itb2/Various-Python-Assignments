'''
Created on Feb 22, 2015

@author: Ivory
'''
import math
def minSteps(sx,sy,gx,gy):
    """
    return integer number of steps as described below
    based on integer parameters
    """
    nx = (gx - sx)
    ny = (gy - sy)
    if  nx ==0 and ny>=0:
        straight_up(nx,ny)
        
    elif nx==0 and ny<0:
        straight_down(nx,ny)
    
    elif nx!=0 and ny!=0 and nx==ny:
        true_Diagonal(nx,ny)
        
    elif ny==0:
        sideways(nx, ny)
        
    elif nx!=ny and nx!=0 and ny!=0:
        if ny>0:
            falseDiagonal_up(nx, ny)
        else:
            falseDiagonal_down(nx, ny)
    else:
        return "Missed a spot."
    
def straight_up(x,y):
    ans = math.fabs(y)
    return ans
       
def straight_down(x,y):
    b= math.fabs(y)
    if b %2 == 0:
        ans = b
    else:
        ans = b+2
        
    return ans
    
def true_Diagonal(x,y):
    ans = math.sqrt(x**2 + y**2)
    return ans
    
def falseDiagonal_down(x,y):
    q = math.fabs(x)
    ans = straight_down(x,y) + q
    return ans
     
def falseDiagonal_up(x,y):
    q = math.fabs(x)
    ans = straight_up(x,y) + q
    return ans
    
def sideways(x,y):
    b = math.fabs(x)
    if b%2==0:
        return  b
    else:
        return b+1
   

    
    
    
    

    
    
    
    
    