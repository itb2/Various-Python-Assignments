'''
Created on Mar 24, 2015

@author: Ivory
'''
def reversecomp(dna):
    """
    return String that is the reverse
    complement of the String parameter dna 
    """
    # you write code here
    
    complements = {'a':'t', 't':'a','c':'g','g':'c'}
    #turn into a list. change list based on what letter it is. change back to string
    dnalist = []
    ind = 0
    for x in range(len(dna)):
        dnalist.append(dna[ind])
        ind +=1
    ind = 0
    for char in dnalist:
        if char == 'a':
            dnalist[ind]= complements['a']
            ind+=1
        elif char=='t':
            dnalist[ind]= complements['t']
            ind+=1
        elif char=='c':
            dnalist[ind]= complements['c']
            ind+=1 
        else:
            dnalist[ind]= complements['g']
            ind+=1  
    dnalist.reverse()
     
    return ''.join(dnalist)
            
            
            
            