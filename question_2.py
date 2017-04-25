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

print question2("z")

"""
Test Cases

Case 1: question2("racecar") -> racecar
Case 2: question2("") -> " "
Case 3: question2("z") -> Please pick a string with more letters
"""
