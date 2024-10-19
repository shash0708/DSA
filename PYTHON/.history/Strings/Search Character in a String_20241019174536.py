# Search Character in a String:
# You are given a string S. You are also given a character c. Check if the character c is present in the string S. If present print yes, else print no.
# Sample Input 1:
# abcdefgh
# f
# Sample Output 1:
# Yes
# Sample Input 2:
# abcdefgh
# r
# Sample Output 2:
# No

n="abcdefgh"

k="f"
flag=True
for char in n:
    if char==k:
        flag=True
    else:
        
