'''
Created on Jan 29, 2015

@author: Ivory
'''
#This program converts rgb values to grayscale

def convert(r,g,b):
    """
    return float value obtained by
    converting integer r,g,b, into grayscale
    """
    # you write code here
    #r, g, and b will each be between 0 and 255 inclusive.
        
    if r <= 255 and r >=0 and g<= 255 and g>=0 and b<=255 and b>=0:
                return 0.21*r + 0.71*g + 0.07*b
                

                
            