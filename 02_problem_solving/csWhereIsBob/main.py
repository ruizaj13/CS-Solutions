# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

# Examples:
#     csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2

def csWhereIsBob(names):
    for i, v in enumerate(names):
        if v == 'Bob':
            return i
    return -1

print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))