'''
Created on Jan 29, 2015

@author: Ivory
'''



def ratio(dna):
    """
    return float that's the cg ratio of the 
    nucleotides in the string parameter dna
    """
    
    # write code here
    
    '''Your method should return the percentage (between 0.0 and 1.0) of 'c' 
    (cytosine) and 'g' (guanine) in the genome. For example, if half of the nucleotides 
    are either 'c' or 'g' your method should return 0.5 --- 
    see the examples for more detail.'''
    cnum = 0
    gnum = 0
    fullLength = len(dna)
    for i in dna:
        if i == "c":
            cnum = cnum +1
    for i in dna:
        if i == "g":
            gnum = gnum + 1
            
    return float(fullLength/(cnum+gnum))
   


    