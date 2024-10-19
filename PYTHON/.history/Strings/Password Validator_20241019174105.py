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

n="Abcd@123"
flag=True
pattern = r'[^a-zA-Z0-9 ]'

if len(n) == 8:
    flag=True

for char in n:
    if char.islower():
        flag =True
    
    elif  char.isupper():
        flag=True
        
    elif char>0 and char<9 :
        flag=True
        
    
    # Search for special characters in the string using the pattern
    elif char.search(pattern, n):
        
        
    
