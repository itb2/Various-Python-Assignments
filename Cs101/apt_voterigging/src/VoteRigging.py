'''
Created on Mar 19, 2015

@author: Ivory
'''

def minimumVotes(votes):
    """
    returns minimum number of votes(int) to change
    using values in votes (integer list)
    """
    othervotes = votes[1:]
    fave = votes[0]
    count = 0
    if len(othervotes) > 0:
        while fave <= max(othervotes):
            ind = 0
            for num in othervotes:
                if num >= fave and num  == max(othervotes):
                    num = num - 1
                    othervotes[ind] = num
                    ind+=1
                    fave +=1
                    count+=1
                else:
                    ind += 1
    return count
    