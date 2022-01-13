"""
Write a function that finds the elements in a list whose sum is equal to 10. 
The function should return the output in the form of a list.

input_list = [5,7,1,2,8,4,3]

Expected output = [[7, 3], [2, 8]]
"""

def sum_of_elements(input_list):
    
    lst = []
    
    for i in range(len(input_list) - 1):
        
        for j in range(i+1, len(input_list)):
            
            if input_list[i] + input_list[j] == 10:
                
                lst.append([input_list[i], input_list[j]])
            
    return lst