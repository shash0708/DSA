# Count Vowels and Consonants
# You are given a String. Count the number of vowels and consonants the string has. Print the number of vowels followed by the number of consonants.
# Note: The string may contain other character like space and full stop.
# Vowels are alphabets belonging to the following group - {a, e, i, o u}. Consonants are rest of the alphabets that do not belong to the group - {a, e, i, o u}.
# Sample Input: 
# Hello World
# Sample Output: 
# 3 7
# Explanation: The string has 3 vowels and 7 consonants.

vow=0
con=0

n="Hello World"

for char in n:
    if char==" ":
        continue
    
    if char.lower() == 'a' || char.lower() == 'e' || char.lower() == 'i' || char.lower() == 'o' || char.lower() == 'u'