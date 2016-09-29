'''
Created on Feb 24, 2015

@author: Ivory
'''
def theIndex(carrots,amount):
    carrotsclone = carrots[:]
    carrotsclone = carrotsclone.sort()
    """
    carrots is list of integers representing
    boxes of carrots, amount is int value. 
    return int that is the index/box number
    of the box from which the last of
    amount carrots are eaten
      """  
    p = sumCarrots(carrots) + 1
    l = len(carrotsclone - 1)
    
    for i in range(amount):
        if carrots.count(carrotsclone[l]) == 1 and p>1:
            carrotsclone[l] = carrotsclone[l] - 0
            if l > 0:
                l = l - 1
                p=p- 1
            else:
                l= l +1
                p=p-1
        elif p==1:
            last = carrots.index(carrots[l-1])
        else:
            k = carrots.index(carrots[l])
            carrots[l] = carrots[l]- 1
            p =p-1
            
    return last
               
       
def sumCarrots(carrots):
    g = 0
    for p in carrots:
        g += p
    return g
           
        
 

    
     

    
