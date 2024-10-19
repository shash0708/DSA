# Sum of Array Except Self
# You are given an array of integers. Print an array where each index has the sum of all numbers in the original array except the number at that index. 
# Avoid using subtraction, and handle this with nested loops.
# Sample Input:
# 7 3 6 7 5
# Sample Output:
# 21 25 22 21 23
#

arr=[7,3,6,7,5]

k=sum(arr)

print(k)
n=len(arr)

l=[]
for i in range(0,n):
    l.append(k-arr[i])
 
f=len(l)
for i in range(0,f):
    print(l[i],end=" ")  # prints each element in a new line