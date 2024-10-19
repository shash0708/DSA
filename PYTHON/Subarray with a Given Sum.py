# Subarray with a Given Sum:
# You are given an integer array and a target sum. Print a subarray that adds up to the target sum.
# If there are multiple possible subarrays, print the one that appears first and is smallest. And if, no such subarray is possible, print "Not Possible".
# A subarray is defined as a contiguous portion of an array.
# Sample Input 1: 
# 3 6 2 1 7
# 10
# Sample Output 1: 
# 2 1 7
# Explanation 1: 10 = 2+1+7. [2, 1, 7] is a subarray within the given array that adds up to 10.
# Sample Input 2: 
# 3 6 2 1 7
# 14
# Sample Output 2: 
# Not Possible
# Explanation 2: No subarray within the given array adds up to 14.



arr=[3,6,2,1,7]

n=len(arr)
s=0
k=10
st=0
for end in range(0,n):
    s=s+arr[end]
    while s>k and st<=end:
        s=s-arr[st]
        st+=1
    
    if s==k :
        print(arr[st:end+1])
        break