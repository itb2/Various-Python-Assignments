'''
Created on Feb 14,2011
@author: ola
'''

import random

def toCardString(card):
    rankStrings = ["ace","two","three","four","five","six","seven",
                   "eight","nine","ten","jack","queen","king"]
    suitStrings = ["spades", "hearts", "diamonds","clubs"]
    return rankStrings[card[0]] + " of " + suitStrings[card[1]]

def get_rank_counts(hand):
    '''
    returns list of how often each rank 1-13 occurs in a hand
    e.g., list[3] = # occurrences of a 3, list[11] = # occurrences of jack
    '''
    counts = [0]*13
    for card in hand:
        rank = card[0]
        counts[rank] += 1
    return counts

def is_pair(hand):

    ranks = get_rank_counts(hand)
    if ranks.count(2) == 1 and ranks.count(1) == 3:
        return True
    return False
    
def get_deck():
    '''
    create and return an unshuffled deck of cards
    '''
    d = []
    for rank in range(0,13):
        for suit in range(0,4):
            d.append([rank,suit])
    return d

def get_hand(deck):
    random.shuffle(deck)
    return deck[0:5]

def print_hand(hand):
    print '[',
    for card in hand:
        print toCardString(card),',',
    print ']'
    

def deal_demo():
    deck = get_deck()
    print_hand(deck)
    print_hand(get_hand(deck))
    print_hand(get_hand(deck))

def simulate(n):
    '''
    Simulate dealing n poker hands
    '''
    deck = get_deck()
    pc = 0
    for i in range(0,n):
        hand = get_hand(deck)
        if is_pair(hand):
            pc += 1
    print "# hands = %d, # pairs = %d, prob = %.3f" % (n,pc, 1.0*pc/n)
    
if __name__ == "__main__":
    deal_demo()
    simulate(500)
