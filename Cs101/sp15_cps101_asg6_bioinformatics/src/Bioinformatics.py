'''
Mar 18, 2015

@author: rodger
'''

# Use the following items to help you get started. 

# use these variables to make your code more readable
START_CODON = 'atg'
STOP_CODONS = [ 'taa', 'tag', 'tga' ]

# these next two lists are meant to be used together,
#   i.e., the index of a codon in the first list matches
#         its corresponding amino acid in the second list
# they are taken from this web site:
#   http://en.wikipedia.org/wiki/DNA_codon_table
# and are intended to help you with the problem, 
# so you do not have to hand code the translation yourself
CODONS = [
  'gct', 'gcc', 'gca', 'gcg',
  'tgt', 'tgc', 
  'gat', 'gac',
  'gaa', 'gag', 
  'ttt', 'ttc', 
  'ggt', 'ggc', 'gga', 'ggg',
  'cat', 'cac',
  'att', 'atc', 'ata',
  'aaa', 'aag',
  'ctt', 'ctc', 'cta', 'ctg', 'tta', 'ttg',
  'atg',
  'aat', 'aac',
  'cct', 'ccc', 'cca', 'ccg',
  'caa', 'cag',
  'cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg',
  'agt', 'agc', 'tct', 'tcc', 'tca', 'tcg', 
  'act', 'acc', 'aca', 'acg',
  'gtt', 'gtc', 'gta', 'gtg',
  'tgg',
  'tat', 'tac',
]
AMINO_ACIDS = [ 
  'A', 'A', 'A', 'A', 
  'C', 'C',
  'D', 'D', 
  'E', 'E', 
  'F', 'F',
  'G', 'G', 'G', 'G',
  'H', 'H',
  'I', 'I', 'I',
  'K', 'K', 
  'L', 'L', 'L', 'L', 'L', 'L',
  'M', 
  'N', 'N', 
  'P', 'P', 'P', 'P',
  'Q', 'Q',
  'R', 'R', 'R', 'R', 'R', 'R',
  'S', 'S',  'S', 'S', 'S', 'S',
  'T', 'T', 'T', 'T', 
  'V', 'V', 'V', 'V', 
  'W',
  'Y', 'Y', 
]


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

def findRegion(dna):
    """
    dna is a string of dna. 
    Return the first valid protein-coding region.
    """
      
    # you write code here
    dna = str(dna)
    b = dna.find('atg') #Finds where the first atg starts
    new = dna[b+3:]
    final=""
    if b != -1:
        c = new.find('taa')
        d = new.find('tag')
        e = new.find('tga')
        indlist = []
        if c!= -1:
            indlist.append(c)
        if d!= -1:
            indlist.append(d)
        if e!= -1:
            indlist.append(e)
        indlist.sort()
        x = 0
        for n in indlist:
            if len(new[:n])%3==0 and x==0:
                final = new[:n]
                x+=1
                
    return final

def codonToamino(codon):
    
    '''codonlist= []
    for i in range(len(region)/3):
        codonlist.append(region[0:3])
        region = region[3:]
    ind = 0   
    for char in codonlist: '''
        
    loc = CODONS.find(codon)   
    


def translateDNAtoProtein (dna):
    """
    given a string composed only of lowercase letters 'gcta', 
    return a string of uppercase letters that represents the 
    longest protein found first within that string or its 
    reverse complement, or the empty string if no protein can
    be found
    """
    # TODO: complete this function
    
    dnav2 = reversecomp(dna)
    choice = len(findRegion(dna)) > len((findRegion(dnav2)))
    if choice:
        chosen = findRegion(dna)
    else:
        chosen = findRegion(dnav2)
        
    
        
    return ""
   
