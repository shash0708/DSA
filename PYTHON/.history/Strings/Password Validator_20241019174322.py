# Password Validator
# Write a program that takes a string S as input and checks if the string S satisfies all the following conditions to be a strong password:
# Contains at least 8 characters.
# Contains at least one lowercase character.
# Contains at least one uppercase character.
# Contains at least one number.
# Contains at least one special character.
# If the string S satisfies all conditions, print yes, else print no.
# Sample Input 1: 
# Abcd@123
# Sample Output 1: 
# Yes
# Sample Input 2: 
# Xyz123
# Sample Output 2: 
# No

import re  # Import the regex module

n = "Abcd@123"
flag = True
pattern = r'[^a-zA-Z0-9 ]'

# Check the length of the string
if len(n) != 8:
    flag = False  # Set flag to False if the length is not 8

for char in n:
    if char.islower():
        flag = True  # Found a lowercase character
    elif char.isupper():
        flag = True  # Found an uppercase character
    elif char.isdigit():  # Check if character is a digit
        flag = True
    elif re.search(pattern, char):  # Check for special characters
        flag = True
    else:
        flag = False  # If it doesn't match any conditions, set flag to False
        break  # Exit the loop

# Final check for the flag
if flag and len(n) == 8:  # Ensure the length condition is also checked
    print("Yes")
else:
    print("No")
