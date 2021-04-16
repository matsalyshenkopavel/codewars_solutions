"""Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests."""


def first_non_repeating_letter(string):
    string_with_same_case = string.lower()
    for char in string_with_same_case:
        if string_with_same_case.count(char) == 1:
            return string[string_with_same_case.index(char)]
    return ''


print(first_non_repeating_letter('hello world, eh?'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('abba'))