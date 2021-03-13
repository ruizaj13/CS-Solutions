# Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

# Examples:
#     csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

def csMakeItJazzy(chords):
    res = []
    for i in chords:
        if i.endswith('7') == False:
            i += '7'
            res.append(i)
        else: 
            res.append(i)
    return res

print(csMakeItJazzy(["G", "F", "C"]))