'''
Created on Jan 29, 2015

@author: Ivory
'''
"""
return the word with the first part of it repeated 
if it is a valid part to repeat. The part to be 
repeated must be repeated "number" times.
If the first letter is not a vowel, and the third 
letter is a vowel, then the part to repeat is the 
first three letters.
If the first and third letters are not vowels, but 
the second letter is, then the part to repeat is 
the first two letters. 
Otherwise there is nothing to repeat. 
Only the first letter of the returned word may be 
a capital letter, if the original word started with 
a capital letter. 
"""

#BE SURE TO ADD COMMENTS FOR EACH FUNCTION AND CONFUSING PARTS

def isVowel(ch):
    #precondition: ch is a string of length 1
    #postcondition: returns true if ch is a vowel, returns false if not a vowel
    #could make a string with vowels and compare 1st letter of ch to vowels, and return true
    ch = ch.lower()
    if ch == "e":
        return True
    elif ch == "a":
        return True
    elif ch == "o":
        return True
    elif ch == "u":
        return True
    elif ch == "i":
        return True
    else:
        return False
    

def repeat(word,number):
    #This function does...
    if len(word)== 1:
        return word
    
    if isVowel(word[0])== True:
        return word
    if len(word) == 2:
        if isVowel(word[1]) == True:
            return word + word.lower() * (number-1)
        else:   # no vowels return
            return word
    #second case, if none of the three letters are vowels.
    #we know first letter is not a vowelisVowel(word[0]) == True
    if isVowel(word[1]) == False and isVowel(word[2]) == False:
        return word
    #Third case, third letter vowel, repeat first three letters
    if isVowel(word[2])== True:
        return word[0:3] + word[0:3].lower() *(number-1) + word[3:]
    if isVowel(word[0])==False and isVowel(word[1])==True and isVowel(word[2])==False:
        return word[0:2] + word[0:2].lower()*(number-1)+ word[2:]
    
    
    
    
    
   