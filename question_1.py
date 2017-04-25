"""
Explanation

We can check whether two strings are anagram by comparing the characters from both strings and
if length of both strings are the same, then the two strings are anagram. We can first initialize a list
to store the original string in that list and then check with every possible consecutive substring in t.
If any set is an anagram of t, then we return True, else False.
Comparing counts of all characters will can be done in constant time since there are only limited amount of characters to check.

Worst case is O(len(s)
Time complexity is O(len(s))
Space complexity is O(1).
"""


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