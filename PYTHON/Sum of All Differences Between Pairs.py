# # Sum of All Differences Between Pairs
# # You are given an array of integers. Calculate the sum of absolute differences between all pairs of numbers in the array.
# # Sample Input:
# # 7 3 6 4
# # Sample Output:
# # 14
# Absolute difference between 7 and 3 = 4
# Absolute difference between 7 and 6 = 1
# Absolute difference between 7 and 4 = 3
# Absolute difference between 3 and 6 = 3
# Absolute difference between 3 and 4 = 1
# Absolute difference between 6 and 4 = 2
# Sum of absolute differences between all pairs: 4+1+3+3+1+2 = 14

arr=[7,3,6,4]

n=len(arr)

l=[]
for i in range(0,n):
    for j in range(i+1,n):
        l.append(abs(arr[i]-arr[j]))
        # print(abs(arr[0]-arr[1]))
        
print(sum(l))
        
