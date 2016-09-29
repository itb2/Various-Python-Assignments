'''
All possible transform functions.

You need to complete this file.

Those whose name starts with transform_ will appear in the menu option.
You can write as many helper functions as you want to support these primary functions.

Created on Jan 30, 2015



@author: Ivoryanna Brown
'''



def transform_identity (word):
    '''Identity transform (no change).
       Note, this simply serves as an example transform.
    '''
    return word


def transform_uppercase (word):
    '''Transform to UPPERCASE (no decode).
       Note, this simply serves as an example transform.
    '''
    return word.upper()


def transform_pigify (word):
    '''Encode into Pig-latin from English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, this transformation is not unique, 
             some different words may be transformed into the same pig-latin word.
    '''
    # TODO: complete this function so that it returns a new version of the string word,
    #       assuming word is in English, use the rules of pig-latin to encode the word
    vowels = ["a","e","i","o","u","A","E", "I", "O", "U"]
    if word[0] == "q" or word[0]== "Q":
        word = word[2:] + "-" + word[0] +"u" + "ay"
        return word
    mini = len(word)
    for v in vowels:
        x = word.find(v)
        if x >= 0 and x < mini:             #This is an edited version of my apt piglatin that also 
            mini = x                        #accounts for words that have no vowels and treats them as if 
    if mini == 0 or mini == len(word):      #the first letter is a vowel.
        word = word + "-" + "way"
        return word
      
    word = word[mini:] + "-" + word[:mini] + "ay"
    return word


def transform_unpigify (word):
    '''Decode from Pig-latin into English.
       Note, when transforming the string word, 
             do not change its capitalization or punctuation.
       Note, since some words may represent multiple different English words, 
             choose the final English word you think is more common.
    '''
    # TODO: complete this function so that it returns a new version of the string word,
    #       assuming word is in pig-latin, undo the pig-latin rules to decode the word to English
    if word[-1:-4] == "way":
        word = word[-1:-4] + word[:(len(word)-3)]
    elif word[-1:--5]=="Quay" or word[-1:-5]=="quay":
        word = word[-1]+"u" + (word[:len(word)-4])    #makes a word not piglatin anymore.
    else:
        word = word.split("-")
        word = word[1] + word[2]
        
    return word
        


def transform_rot13 (word):
    '''ROT-13 substitution cipher (both encodes and decodes).
       Note, since this transformation is symmetrical, 
       it can serve as encoder and decoder for the same message.
    '''
    # TODO: complete this function so that it returns a new version of the string word, 
    #       with each letter rotated by 13 places.
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    b = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    newWord = ""
    m = len(word)               #Transforms a word to ROT13
    for n in word:
        if n in a:
            m = a.find(n)
            newWord = newWord + b[m]
        else:
            newWord = newWord + n
    return newWord


