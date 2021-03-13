# Given a string, return a new string with all the vowels removed.

# Examples:
#   csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

def csRemoveTheVowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for c in input_str:
        if c in vowels:
            input_str = input_str.replace(c, '')
    return input_str

print(csRemoveTheVowels("Lambda School is awesome!"))