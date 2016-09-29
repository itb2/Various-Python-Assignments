'''
Created on Jan 22, 2015

@author: Ivory
Netid:itb2

This program will return the users score given the word that the input.
The longer the word, the higher their score. The score is the square of the length
of the word.
'''


def score(word):

    wordlength = len(word)
    
    thescore = pow(wordlength, 2)
    
    return thescore
