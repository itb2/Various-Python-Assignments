'''
Created on Mar 16, 2015

@author: Ivory
'''
import random
import math


"""COMMENTS!!!!"""

def play():
    #print everything: look @ what I wrote down.... Decide when game should be over.(maybe a for loop)
    """picking letters, updating word-displays, determining if the game should 
    continue, validating input, and so on. 
    In principle, each of these will be a different function, though 
    in practice that's often not possible"""
    lengthchoice = inpt_numberofletters()
    
    if str(lengthchoice).isdigit():
        misseshad = input_MissesAllowed()
        for n in range(misseshad):
            wordchosen = rand_word(lengthchoice)
            print "You guessed: ",wordchosen
            l = compare_correctorno()
            inpt_letterorword()
            misseshad = misseshad-1
    
    else:
        print "Incorrect Input"

def rand_word(length):
    #call input guesses
    thefile = file.open("lowerwords.txt")
    randword = random.randint(thefile) #HOW TO MAKE SURE ITS THE RIGHT LENGTH
        
    return randword   
    
def inpt_numberofletters():
    """def inpt_themes():"""
    letternum = input("How many letter would you like?")
    return letternum
    
def input_MissesAllowed():
    #ask how many misses they want to be allowed
    missesallowed = input("How many guesses would you like?")
    if missesallowed.isdigit():
        return missesallowed
    else:
        print "Incorrect Input"

    
def input_guesses(x):
    #dont forget to add to the number of misses and words/letters that have been guessed.
    
    if x == "letter":
        letterchosen = input("Guess a letter:") 
        if len(letterchosen) == 1:
            compare_correctorno(letterchosen)
        else:
            return "Invalid Input"
    elif x == "word":
        wordchosen = input("Guess a word")
        if len(wordchosen) > 1:
            compare_correctorno(wordchosen)
        else:
            return "Invalid Input" 
    

def inpt_letterorword():
    b = input("Do you want to input a letter or a word?")
    input_guesses(b)
  
    
def recreate_WordAndBlanks(word,ifcorrect,choice):
    letterlist = [n for n in word]
    choicelist = []
    originalchoice = [n for n in word]
    blanklist = ["_" for n in word]
    k = input_MissesAllowed()
    if ifcorrect == "no":
        indlist = []
        for x in range(len(letterlist)):
            ind = word.find(choice)
            if ind != -1:
                letterlist.remove(choice)
                indlist.append(ind)
                word = str(letterlist)
                k = k-1
            else:
                k= k-1
        y = 0
        for b in range(len(indlist)):
            blanklist[y] = choice
            y += 1
            choicelist.append(choice)
        if k >0:
            print blanklist
            print "you guessed: ", str(originalchoice)
            print "so far you have guessed: ",choicelist
            print "Misses left: ", x
        else:
            print "You lose"
            
    else:
        print blanklist
        print "your guesses were: ",choicelist
        print "You win"
    


def compare_correctorno(x):
    #ifcorrect and word
    rand = rand_word()
    if x == rand:
        
        correctornah = "yes"
    else:
        correctornah = "no"
        
    recreate_WordAndBlanks(rand,correctornah,x)
  

play()    