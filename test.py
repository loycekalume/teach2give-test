'''
1. Below is a database diagram(diagram image)
Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points.
'''
'''
SELECT
    d.driverName AS driver_name,
    r.raceName AS race_name,
    c.location,
    rs.grid,
    rs.position,
    rs.fastestLap AS fastest_lap,
    rs.points,
    r.time,
    r.year,
    r.date,
    cn.name AS team_name
FROM
    results rs
JOIN
    drivers d ON rs.driverId = d.driverId
JOIN
    races r ON rs.raceId = r.raceId
JOIN
    constructors cn ON rs.constructorId = cn.constructorId
JOIN
    circuits c ON r.circuitId = c.circuitId
WHERE
    r.year = 2020
ORDER BY
    rs.points DESC;

'''






'''
2. Write a Python function that checks whether a word or phrase is palindrome or
not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

'''


def is_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(string.lower().split())

    # Check if the string is the same when reversed
    return cleaned_string == cleaned_string[::-1]


# Test cases
print(is_palindrome("madam"))  # True
print(is_palindrome("kayak"))  # True
print(is_palindrome("nurses run"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("mom"))     # True
print(is_palindrome("peace"))   # False



'''
3. Write a Python function to check whether a string is pangram or not. (Assume
the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the
alphabet at least once. For example: "The quick brown fox jumps over the
lazy dog"
'''

def is_pangram(sentence):
    # Define the alphabet
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # Convert the sentence to lowercase and create a set of characters
    sentence_set = set(sentence.lower())

    # Checks if all alphabet letters are in the sentence
    return alphabet.issubset(sentence_set)

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("We have a meeting"))  # False


'''
4. Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19
'''

def reverse_integer(num):
    # Convert the number to a string, reverse the digits, and handle negative numbers
    if num < 0:
        reversed_num = int("-" + str(num)[:0:-1])
    else:
        reversed_num = int(str(num)[::-1])
    return reversed_num


print(reverse_integer(500))  # Output: 5
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))   # Output: 19


'''
5. Write a program that accepts a string as input, capitalizes the first letter of each
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"

'''

def capitalize_word(input_string):
    return input_string.title()

print(capitalize_word("hi")) # Hi
print(capitalize_word("my name is john smith")) # My Name Is John Smith
print(capitalize_word("hello i love coding"))  # Hello I Love Coding