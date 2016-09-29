import InputGUI as Input
from Transforms import transform_rot13, transform_unpigify


def write_words(file, words):
    """
    output given words to the file (and also to the console)
     - words is a list of lists,
       where each sublist represents a line to write
     - file is a file open for writing
    write each sublist to the file
    with words on a line separated by whitespace
    and each sublist of words on a line
    """
    # TODO: modify this function to write output to file in addition to printing it
    for line in words:
        for w in line:
            print w + " ",
        print
        
    for line in words:
        for w in line:
            file.write(w +" "),
        file.write("\n")
        
    file.close()


def transform(words, func):
    '''
    apply func each word in words and return the result
     - words is a list of lists,
       where each sublist represents a line from the original file
     - the result is a list of lists, 
       where in each sublist each word has been 
       transformed by applying func to the word
    '''
    # TODO: change each word in the list of lists, using func to accomplish the change
    # FOR EXAMPLE:
    newWords = words[:]                 # copy list
    
    for l in range(len(newWords)):

        for b in range(len(newWords[l])):
            newWords[l][b]= func(words[l][b]) # change first word by calling func on it  
    
    return newWords
    


def get_words (file):
    '''
    returns all words in file as a list of lists, 
    where each nested list is one line from file, 
    words in line as elements of nested list
    '''
    
    returnlist = [ ]
    for line in file.readlines():
        returnlist += [line.split()]
    return returnlist


def transform_file ():
    """
    do the work for this program: 
      - prompt user for file
      - prompt user for transform function
      - apply transform to each word
      - write transformed data to a file specified by user
    """
    file = Input.choose_file_to_open()
    if file == None:
        return
    words = get_words(file)
    file.close()
    commonWords = ["the","The","A","a","to","their","and","you","for","he","she","it","than","because","of","is","did","do","write","this","how","that","with","but","when","no","yes"]
    y = 0
    func = ""
    for n in words:
        for p in n:
            if p in commonWords:
                y += 1
    if y == 0:
        
        twords = transform(words, transform_rot13())
        file = Input.choose_file_to_save()
        if file == None:
            return
        write_words(file, twords)
        file.close();
        func = "rot13"
    if func != "rot13":
        '''Check for piglatin AND WRITE FUNCTION TO TRANSLATE BACK'''
        '''call unpigify function (YOU GOTTA MAKE IT.. MIGHT HAVE BEEN AN APT'''
        '''INDICATE WHAT HAPPENED'''
        mm= 0
        for l in words:
            if  l[-1:-3] == "ay" and "-" in l:
                mm+=1
        if mm == len(words):
    
            twords = transform(words, transform_unpigify())   
            file = Input.choose_file_to_save()
            if file == None:
                return
            write_words(file, twords)
            file.close();
        else:
            '''if its not equal to either, then SAY SO AND call write words?? '''
            file = Input.choose_file_to_save()
            if file == None:
                return
            write_words(file,"The file has not been encoded.")
            write_words(file, words)
            file.close();
            
                
                
    


# the main function
transform_file()