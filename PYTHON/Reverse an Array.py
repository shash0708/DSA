# Reverse an Array:
# You are given an array of integers. Create a new array with elements in reverse order. Print the new array.
# Sample Input:
# 11 1 13 21 3 7
# Sample Output:
# 7 3 21 13 1 11

n = [11, 1, 13, 21, 3, 7]
l = []
k = len(n)

for i in range(k-1, -1, -1):
    l.append(n[i])

for i in range(0, k):
    print(l[i], end=" ")
