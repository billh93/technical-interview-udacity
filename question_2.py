"""
Explanation

We first get the length of the string and store it in base_len then store we store that
into another variable called search_len. With this we do a while loop to check
if search_len is greater than 1. The end result we should with the program is
get the reversal of that string if not we should get some omitted characters or
an error message.

Worse case is O(n)
Time complexity is O(n)
Space complexity is O(1)
"""


def question2(a):
    # Gets length of string
    base_len = len(a)
    # Holds length value of string
    search_len = base_len
    while search_len > 1:
        iter = base_len - search_len
        # Will iterate for every character in the string
        for i in range(iter + 1):
            search_substring = a[i:search_len + i]
            # If the reverse character matches the opposite end return it
            if search_substring == search_substring[::-1]:
                return search_substring
        # Keep on iterating through the characters string
        search_len -= 1
    if search_len == 1:
        return "Please pick a string with more letters"


"""
Test Cases

print question2("racecar") -> racecar
print question2("") -> " "
print question2("z") -> Please pick a string with more letters
"""
