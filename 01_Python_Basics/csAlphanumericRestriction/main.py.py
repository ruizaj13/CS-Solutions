# Create a function that returns True if the given string has any of the following:

# -Only letters and no numbers.
# -Only numbers and no letters.

# If a string has both numbers and letters or contains characters that don't fit into any category, return False.

def csAlphanumericRestriction(input_str):

    if input_str.isdigit() or input_str.isalpha():
        return True
        
    return False

input_str1 = "Bold"
input_str2 = "123456"
input_str3 = "H3LLO"
print(csAlphanumericRestriction(input_str1))
print(csAlphanumericRestriction(input_str2))
print(csAlphanumericRestriction(input_str3))