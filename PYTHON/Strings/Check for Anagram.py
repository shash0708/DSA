# Check for Anagram
# You are given two String S1 and S2. Determine if the two strings are anagrams of each other.
# Anagrams are words or phrases formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of "silent".
# Note: You will have to ignore case and white spaces.
# Sample Input 1: 
# Silent
# Listen
# Sample Output 1: 
# Yes
# Explanation 1: Silent and Listen has the same letters. If we ignore case, they are anagrams.
# Sample Input 2: 
# New York Times
# monkeys write
# Sample Output 2: 
# Yes
# Explanation 2: If we don't consider white space and case-sensitive, "New York Times" and "monkeys write" are anagrams. They have same characters repeating same number of times.


def check_anagram(str1, str2):
    # Step 1: Remove spaces and convert strings to lowercase (for case insensitivity)
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Step 2: Check if the lengths are the same (if not, they can't be anagrams)
    if len(str1) != len(str2):
        return False

    # Step 3: Sort both strings and compare them
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Example usage
str1 = "listen"
str2 = "silent"

if check_anagram(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')
