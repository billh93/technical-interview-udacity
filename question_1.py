def question1(s, t):
    # If substring is longer than the word return false
    if len(t) > len(s):
        return False
    # Initializes a list to hold the characters
    char_list = []
    # Iterates through every character of the string
    for char_s in s:
        # Adds the character into our newly created char_list
        char_list.append(char_s)
    #  Iterates through every character of the substring
    for char1 in t:
        found = False
        for index, char2 in enumerate(char_list):
            # Compares the character from char_list to the substring
            if char1 == char2:
                found = True
        if not found:
            return False
    return True


"""
Test Cases

print question1("udacity", "ad") -> True
print question1("udacity", "") -> True
print question1("ad", "udacity") -> False
"""