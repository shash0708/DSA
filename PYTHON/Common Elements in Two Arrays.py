# Common Elements in Two Arrays:
# You are given an integer n and two integer arrays each of length n. Print all the common elements between these two arrays.
# Print the elements in an order as they appear in the first array. If one common element is repeated multiple times, print it just once. If there are no common elements, print No.
# Sample Input 1: 
# 7
# 4 9 2 5 7 4 3
# 9 6 4 8 6 1 12
# Sample Output 1: 
# 4 9
# Explanation 1: In the given arrays, 4 is repeating multiple times, but you need to print it just once. Also, the order of printing 4 and 9 are as per their appearance in the 1st array.
# Sample Input 2: 
# 7
# 2 7 6 4 7 4 3
# 8 5 9 1 5 8 9
# Sample Output 2: 
# No
# Explanation 2: No elements are common in the two given array.
ar1 = [4, 9, 2, 5, 7, 4, 3]
ar2 = [9, 6, 4, 8, 6, 1, 12]
seen = set()
ce = []

for element in ar2:
    if element in ar1 and element not in seen:
        print(element)
        seen.add(element)

