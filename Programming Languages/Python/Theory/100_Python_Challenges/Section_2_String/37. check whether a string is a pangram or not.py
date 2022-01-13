"""
Given a string determine whether it is a pangram in the English alphabet.

sample_string = "The quick brown fox jumps over the lazy dog"
expected output = True
"""

def pangram(sample_string): 
    List = [] 
    # create list of 26 charecters and set false each entry 
    for i in range(26): 
        List.append(False) 
          
    # converting the sentence to lowercase and iterating 
    # over the sentence  
    for c in sample_string.lower():  
        if not c == " ": 
  
            # make the corresponding entry True 
            List[ord(c) -ord('a')]= True 
              
    # check if any charecter is missing then return False 
    for ch in List: 
        if ch == False: 
            return False
    return True
  
    if (pangram(sample_string)): 
        return True
    else:
        return False