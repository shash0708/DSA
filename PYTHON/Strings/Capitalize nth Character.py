# Capitalize nth Character
# You are given a String and and an index. Capitalize the character at the nth position in the given String.
# Note: You can consider the index to start from 0.
# Sample Input: 
# programming
# 6
# Sample Output: 
# prograMming


n="programming"

k=6

print(n[:k]+n[k].upper()+n[k+1:])  