'''
Created on Feb 27, 2015

@author: Ivory
'''
def howMany(meals,restaurant):
    set1 = set(meals)      #make meals into a set to get rid of all repetition
    count = 0
    for x in set1:          #For every element in the set, split it into its own list.. so we have nested lists
        x = x.split(":")   
        if x[1] == restaurant:   #if the second element in the nested list is the restaurant add one 2 count
            count +=1 
            
    return count