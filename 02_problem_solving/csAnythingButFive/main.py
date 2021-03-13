# Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range 
# (except integers that contain the digit 5).

# Examples:
#   csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)

def csAnythingButFive(start, end):
    result =[]

    for n in list(range(start, end + 1)):
        if '5' not in str(n):
            result.append(n)
    return(len(result))

print(csAnythingButFive(1, 5))