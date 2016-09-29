'''
Created on Feb 5, 2015

@author: Ivory
'''

'''
Created on Feb 5, 2015

@author: Ivory
'''

def lovely(ingredients,inedible):
    """
    return int, number of items in 
    ingrediants, a string that are edible 
    using informaion from  inedible, a string
    """
      
    # you write code here
    ingredients1 = ingredients.split()
    number = 0
    for i in ingredients1:
        if inedible.find(i) == -1:
            number += 1
       
    return number
      
        
        
        
        