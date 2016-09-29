'''
Created on Jan 22, 2015

@author: Ivory
'''
def total(width,length):
    """
    return float indicating 
    the perimeter of the rectangle that 
    is specified by the float parameters 
    width and length. All measurements are in inches.
    """
      
    # you write code here
    if width>0 and length>0:
        perimeter=(2*width)+(2*length)
        return perimeter
    else:
        print "Both width and length must be greater than zero"
    