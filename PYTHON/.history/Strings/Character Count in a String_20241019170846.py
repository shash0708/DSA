# Character Count in a String
# You are given a String and a Character. Count how many times the Character is present in the given String. If the Character is not present in the String, print "No".
# Sample Input 1: 
# Hello World
# l
# Sample Output 1: 
# 3
# Explanation 1: The Character l is present 3 times in the String "Hello World".
# Sample Input 2: 
# Hello World
# a
# Sample Output 2: 
# No
# Explanation 2: The Character a is not present in the String "Hello Wor

vow = 0
con = 0
flag=True
n = "Hello World"
ch="l"
for char in n:
    if char == " ":
        continue
    
    elif char.lower() == 'l' :
        vow=vow+1
        
    else:
        flag=False
        
       
if(!flag):
    print("No")
        
print(f"Count of {ch}:-", vow)
