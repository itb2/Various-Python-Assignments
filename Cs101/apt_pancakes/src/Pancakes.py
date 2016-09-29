'''
Created on Jan 27, 2015

@author: Ivory
'''


def minutesNeeded (numCakes, capacity):
    if numCakes == 0:
        return 0
    if numCakes <= capacity:
        return 10
    if numCakes % capacity == 0:            #if the cakes were evenly divided in the pan
        return numCakes/capacity * 10
    if numCakes % capacity <= 0.5 * capacity:
        return numCakes/capacity* 10+ 5
    if numCakes % capacity > 0.5 * capacity:
        return numCakes/capacity * 10 + 10
        

   

    