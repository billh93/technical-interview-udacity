"""
Explanation

We can check whether two strings are a possible anagram by comparing the characters from both strings
We do this by converting them into a list and then sorting them and comparing them to each other
We then run a for loop to compare if the anagram is truly an anagram by reiterating
every character in the list and compare it to the other list. By using the amount of space
with the algorithm it's uses is independent of the input parameters thus making use
of constant space.

Worst case is O(len(s))
Time complexity is O(len(s))
Space complexity is O(1).
"""


def is_anagram(s1, s2):
    # Converts s1 and s2 arguments into lists
    s1 = list(s1)
    s2 = list(s2)
    # Sorts both arguments alphabetically
    s1.sort()
    s2.sort()
    # Checks if both arguments are the same and returns true or false
    return s1 == s2


def question1(s, t):
    # Gets length of substring
    match_length = len(t)
    # Gets length of word
    pattern_length = len(s)
    # Checks to see if it's an anagram by running a for loop
    for i in range(pattern_length - match_length + 1):
        if is_anagram(s[i: i+match_length], t):
            return True
    return False


"""
Test Cases

print question1("udacity", "ad") -> True
print question1("udacity", "") -> True
print question1("ad", "udacity") -> False
"""