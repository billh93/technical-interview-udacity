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
        pop_index = None
        for index, char2 in enumerate(char_list):
            # Compares the character from char_list to the substring
            if char1 == char2:
                found = True
                pop_index = index
        if not found:
            return False
        popped = char_list.pop(pop_index)
    return True

"""
Test Cases

Case 1: question1("udacity", "ad") -> True
String with 2 characters reversed from order in S
Case 2: question1("udacity", "") -> True
Empty string.
Case 3: question1("ad", "udacity") -> False
String t's length is greater than string S.
"""