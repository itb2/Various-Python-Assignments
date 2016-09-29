'''
Created on Jan 21, 2015
@author: Ivory
NetID: itb2
'''

''' This program is supposed to calculate body mass index of a person whose weight
and height, in pounds and inches respectively, are parameters to the function
calculate.'''

def calculate(weight,height):
    '''return float indicating body mass index'''
    if weight==0 or weight<0:
        return "Invalid input for weight"
    if height==0 or height<0:
        return "Invalid input for height."
    else:
        BMI = 703.0695 * (float(weight))/((float(height))**2)
    return BMI
    return float(weight)
    return float(height)
    