# Create a function that given an integer, returns an integer where every digit in the input integer is squared.
#example:
#    -csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81

def csSquareAllDigits(n):
    
    string = str(n)
    squared = ''
    
    for c in string:
        squared += (str(int(c) ** 2))
    return int(squared)

print(csSquareAllDigits(9119))