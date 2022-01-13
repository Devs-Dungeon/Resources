"""
Write a function that accepts an integer and converts the integer into its binary form. 
The function should then swap the two bits at positions 3 and 7 (from left)  in the binary number and return the result (integer).

Example :

input = 40 (binary representation - '00101000' )

Expected output = 10 (binary representation - '00001010')
"""

def swap_bits(num):
    p = 1
    q = 5
    if (((num & (1 << p)) >> p) ^ ((num & (1 << q)) >> q)) == 1:
        num ^= (1 << p)
        num ^= (1 << q)
 
    return num
    
    
                


        