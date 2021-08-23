"""
Filename: palindrome_functions.py
Requirement: Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
Filename: palindrome_functions.py
"""
import sys


def is_palindrome(test_string):
    """
    FROM: LEVEL 1 Requirement
    This method takes in a sample string, then returning TRUE if this is a palindrome,
    Criteria for string palindromes:
    - String is more than one character
    - String if reversed reads the same as the original value
    FALSE if it is not
    """
    if len(test_string) == 0:
        return 'Argument string is empty.'
    reversed_string = test_string[::-1]
    return True if ((test_string == reversed_string) and (len(test_string) > 1))else False


def get_longest_palindrome(test_string):
    """
    FROM: LEVEL 2 Requirement
    Requirement: Now write a function that, given a string, returns its longest palindromic substring.
    You can assume that there will only be one longest palindromic substring.
    Sample Input
    string = "abaxyzzyxf"
    Sample Output
    "xyzzyx"
    """
    longest_palindrome = ""
    if len(test_string) == 0:
        return 'Argument string is empty.'
    max_length = len(test_string)
    for i in range(max_length):
        for j in range(1, max_length+1):
            sub_string = test_string[i:j]
            if len(sub_string) != 0 and is_palindrome(sub_string):
                longest_palindrome = sub_string if(len(sub_string) > len(longest_palindrome)) else longest_palindrome
    return longest_palindrome


def get_palindrome_count(test_string):
    """
    FROM: LEVEL 3 Requirement
    Requirement: Now write a function that returns the minimum number of cuts needed to perform on the
     string such that each remaining substring is a palindrome.
    Filename: palindrome_level3.py
    Now write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.
    Sample Input
    string = "noonabbad"
    Sample Output
    2 // noon | abba | d
    """
    total_palindrome_count = 0
    result_string = ""
    if len(test_string) == 0:
        return 'Argument string is empty.'
    max_length = len(test_string)
    for i in range(max_length):
        for j in range(1, max_length+1):
            sub_string = test_string[i:j]
            if len(sub_string) == 0 or not is_palindrome(sub_string):
                continue
            result_string += sub_string + "|"
            total_palindrome_count += 1
    result_string = str(total_palindrome_count) + "//" + result_string
    return result_string


if __name__ == '__main__':

    try:
        len(sys.argv[1]) # Test if python script has a test string to work with, otherwise error and exit #
        # LEVEL 1 Test #
        result_test = is_palindrome(sys.argv[1])
        print(f'Palindrome Test 1: {result_test} --> Test is a string is a palindrome.')

        # LEVEL 2 Test #
        result_test = get_longest_palindrome(sys.argv[1])
        print(f'Palindrome Test 2: {result_test} --> Return the longest substring that is a palindrome.')

        # LEVEL 3 Test #
        result_test = get_palindrome_count(sys.argv[1])
        print(f'Palindrome Test 3: {result_test} --> Returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.')
        exit(0)

    except IndexError:
        print('The test parameter is empty, provide a string to test.')
        exit(1)



