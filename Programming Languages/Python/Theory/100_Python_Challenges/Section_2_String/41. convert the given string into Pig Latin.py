"""
Pig Latin is a language game formed from English by transferring the initial 
consonant or consonant cluster of each word to the end of the word 
and adding a vocalic syllable ('ay') to create a suffix.

Write a function that converts the given input string into Pig Latin.

input_string = 'scream'

Expected output = 'eamscray'
"""

def char_isVowel(c): 
    vowel = ['A', 'E', 'I', 'O', 'U','a','e','i','o','u']
    if c in vowel:
        return True
    else:
        return False
  
def pig_latin(input_string): 
    flag = False;
    vow_index = 0
    for i in range(len(input_string)): 
        if (char_isVowel(input_string[i])):
            vow_index = i
            flag = True; 
            break; 
    if (not flag): 
        return input_string
    pigLatin = input_string[vow_index:] + input_string[0:vow_index] + "ay"
    return pigLatin 

