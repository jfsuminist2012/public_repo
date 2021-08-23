
Python Filename: 
	palindrome_functions.py

Functions Inside:

Name:is_palindrome:
	Input: String
	Output: Boolean

Name: get_longest_palindrome
	Input: String
	Output: String

Name: get_palindrome_count
	Input: String
	Output: String

-------------------------------------------------------------------------------------------------

Running the code:

1. Download the code to local directory.

2. Change to the directory where the code is.

3. Run the following at the command prompt:
	python palindrome_functions.py <test string>


--------------------------------------------------------------------------------------------------
Test String #1: "teeterereeeeeeer"

Output:
(zigzag) F:\Learning\zigzag>python palindrome_functions.py teeterereeeeeeer
Palindrome Test 1: False --> Test is a string is a palindrome.
Palindrome Test 2: reeeeeeer --> Return the longest substring that is a palindrome.
Palindrome Test 3: 29//teet|ee|ete|ere|erere|rer|ere|reeeeeeer|ee|eee|eeee|eeeee|eeeeee|eeeeeee|ee|eee|eeee|eeeee|eeeeee|ee|eee|eeee|eeeee|ee|eee|eeee|ee|eee|ee| --> Returns the minimum number of cuts needed
to perform on the string such that each remaining substring is a palindrome.

--------------------------------------------------------------------------------------------------
Test String #2: "noonabbad"

Output:
(zigzag) F:\Learning\zigzag>python palindrome_functions.py noonabbad
Palindrome Test 1: False --> Test is a string is a palindrome.
Palindrome Test 2: noon --> Return the longest substring that is a palindrome.
Palindrome Test 3: 4//noon|oo|abba|bb| --> Returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.


--------------------------------------------------------------------------------------------------
Test String #3: "abaxyzzyxf"

Output:
(zigzag) F:\Learning\zigzag>python palindrome_functions.py abaxyzzyxf
Palindrome Test 1: False --> Test is a string is a palindrome.
Palindrome Test 2: xyzzyx --> Return the longest substring that is a palindrome.
Palindrome Test 3: 4//aba|xyzzyx|yzzy|zz| --> Returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome.

