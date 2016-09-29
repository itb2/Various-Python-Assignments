'''
Created on Oct 5, 2011, Modified Oct 20, 2014

@author: rodger
'''
import os
import tkFileDialog
import random

    
def choose_file_to_open():
    """
    prompt for existing file, return the file (open for reading)
    """
    file = tkFileDialog.askopenfile(title="choose a file", initialdir=os.getcwd())
    return file

def processFile(file):
    '''
    process the lines in a file (which has one name per line),
    return a list of names
    '''
    #TODO:
    alist = []
    alist = [line.strip() for line in file]

    
    
    
    
    
    return 
    
def randomize(students):
    '''
    shuffle the students in the list and return this new list
    '''
    #TODO:
    alist = processFile(file)
    list2 = []
    while len(students) >0:
        m = ""
        m = alist[(random.randint(len(alist)-1))]
        list2.append(m)
        alist.pop(m)   
        
        """THIS DOESN'T WORK BECAUSE EACH TIME WE POP SOMETHING, WE SKIP AN ELEMENT"""
        """change from a for loop to a while loop. while the length of students is greater than 0.
        """For I in range(len(studs)):
ranPos= random.randint(0,len(studs)-1)
studs[i] = studs[ranPos]
studs[ranPos]=temp
'''
    return list2
        





    return students'''

def printGroups(students):
    ''' print the students 3 per group with Group number starting w/1 '''
    count = 1
    print "Group 1:"
    for stud in students:
        print stud
        #TODO: add code to print 3 per group
    #use a for loop to go through and randomly and pick three students from the list. then 

        if count%3 ==0
            print
            print"Group" + str(count/3 +1)
        count += 1

    

students = processFile(choose_file_to_open()) 
print students
randomize(students)       
print students
print
printGroups(students)
