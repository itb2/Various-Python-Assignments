'''
Created on Feb 27, 2015

@author: Ivory
'''
def countall(words):
    firstletters = []
    for wrd in words:
        firstletters.append(wrd[0].lower())      #Putting the first letters in a list
    previous = firstletters[0]
    letters = firstletters[1:]   #Setting the list equal to the letters from the second one on
    count = 1
    tally = 0 
    for char in letters:
        if char != previous:
            if count >1:    
                tally+=1
                count = 1
                previous = char
            else:
                previous= char
        elif char == previous:
            count += 1
            previous = char
    if count >1:
        tally += 1
            
    return tally
                
            