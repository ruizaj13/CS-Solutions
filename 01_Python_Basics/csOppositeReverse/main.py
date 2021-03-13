# Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.
# example:
#     -csOppositeReverse("Hello World") ➞ "DLROw OLLEh"

def csOppositeReverse(txt):
    return txt.swapcase() [::-1]
 
print(csOppositeReverse('Hello World'))
 
    #alt solution

    # rvrsd = ''
    
    # for c in txt[::-1]:
        
    #     if c.isupper() == False and c.islower() == False:
    #         rvrsd += c
            
    #     elif c.isupper():
    #         rvrsd += c.lower()    
                 
    #     elif c.islower():
    #         rvrsd += c.upper()
    
    # return rvrsd

    
    
    
        
    
    
    
