# Given a string of words, return the length of the shortest word(s).

def csShortestWord(input_str):
    input_str = input_str.split()

    lengths = [len(w) for w in input_str]
    
    return min(lengths)

inputstr= "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"

print(csShortestWord(inputstr))