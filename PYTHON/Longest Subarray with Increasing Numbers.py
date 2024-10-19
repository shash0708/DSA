# Longest Subarray with Increasing Numbers:
# You are given an integer array. Print the length of the longest subarray with increasing numbers.
# A subarray is defined as a contiguous portion of an array.
# Try not to use nested loop.
# Sample Input: 
# 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
# Sample Output: 
# 4


n=[5, 4, 4 ,7, 6, 3 ,2 ,4 ,6, 8 ,6, 3 ,6, 8, 5]

k=len(n)

max=1
c=1

for i in range(1,k):

    if(n[i]>n[i-1]):
        c=c+1

        
    else:
        if(max<c):
            max=c
        c=1     

print(max)