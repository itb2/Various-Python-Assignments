'''
Created on Feb 5, 2015

@author: Ivory
'''


def convert(s):
    """
    return piglatin-ized string version
     of string parameter s
    """
    """If a word wd begins with a vowel, the piglatin version of the word is wd+"-way"
    , e.g., eager becomes eager-way.
    If a word wd begins with a 'q', assume it begins with 'qu' followed by a vowel, move the 'qu' 
    to the end and add 'ay'. For example quiet becomes iet-quay and quixotic becomes ixotic-quay.
    In all other cases, find the first vowel. Move the characters before the first vowel 
    to the end of the word and add '-ay'. For example big becomes ig-bay and string becomes ing-stray."""

    vowels = ["a","e","i","o","u"]
    s = s.lower()
    if s[0] == "q":
        return s[2:] + "-" + "qu" + "ay"
    mini = len(s)
    for v in vowels:
        x = s.find(v)
        if x >= 0 and x < mini:
            mini = x
    if mini == 0:
        return s + "-" + "way"
    
    return s[mini:] + "-" + s[:mini] + "ay"
    
        