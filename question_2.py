"""
Explanation

When checking the palindrome you can expect that the worst case will be O(n)
Since there are only O(n) locations in any palindromic substring that can
be rooted, we can also easily check all the possible combinations that will
take a order time of O(n^2). If we ignore the space that is used to load a, we
only need to store left and right indexes of the longest palindromic substring.
Therefore, the space complexity of this algorithm is O(1).

Worse case is O(n)
Time complexity is O(n^2)
Space complexity is O(1)
"""


def longest_palindrome(a, left_index, right_index):
    # Left_index and right_index are the left and the right element of index
    l = left_index
    r = right_index
    while l >= 0 and r < len(a):
        if a[l] == a[r]:
            l -= 1
            r += 1
        else:
            return l, r
    return l, r


def question2(a):
    # Make sure a is a string
    if not isinstance(a, str):
        return "Error: not a string"

    # Make sure a has at least 2 characters
    if len(a) < 2:
        return "Error: please pick a string with more letters"

    # Check all possible centers of palindrome
    p_left = 0
    p_right = 1
    for i in xrange(len(a) - 1):
        # Check palindrome is centered at i
        l, r = longest_palindrome(a, i, i)
        if r - l - 1 > p_right - p_left:
            p_right = r
            p_left = l + 1

        # Check palindrome centered is between i and i+1
        l, r = longest_palindrome(a, i, i + 1)
        if r - l - 1 > p_right - p_left:
            p_right = r
            p_left = l + 1
    return a[p_left:p_right]


"""
Test Cases

print question2("racecar") -> racecar
print question2(1) -> Error: not a string
print question2("z") -> Error: please pick a string with more letters
"""
