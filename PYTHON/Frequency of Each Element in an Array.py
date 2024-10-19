# You are given an array of integers. Print the frequency of each element in the array.
# Sample Input: 
# 3 6 2 1 7 3 7 4 1 7 4
# Sample Output: 
# 3 2
# 6 1
# 2 1
# 1 2
# 7 3
# 4 2
# Explanation: 3 appears twice, but we have to print its frequency only once. Same is with other numbers.

arr = [3, 6, 2, 1, 7, 3, 7, 4, 1, 7, 4]

# Sort the array
arr.sort()

n = len(arr)
m = 1
c = 1

for i in range(1, n):
    if arr[i] == arr[i-1]:
        c += 1  
    else:
        print(arr[i-1], "-->", c)
        c = 1  
print(arr[n-1], "-->", c)

    
    
        