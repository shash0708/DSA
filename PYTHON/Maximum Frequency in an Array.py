# Maximum Frequency in an Array:
# You are given an array of integers. Find the element that appears the maximum number of times in an array. If multiple elements appear maximum number of times, you can print any.
# Sample Input:
# 5 4 7 11 8 4 6 11 9
# Sample Output:
# 4
# Explanation: Both 4 and 11 appear 2 times. We can print any of 4 and 11, so we print 4.



arr=[5,4,7,11,8,4,6,11,9]

arr.sort()

k=len(arr)
a=[]
m=1
c=1

for i in range(1,k):
    if arr[i]==arr[i-1]:

         c=c+1
    else:
        if c>m:
            m=c
            c=1
         
            a.append(arr[i-1])
            
            
l=len(a)

for i  in range(0,l):
    print(a[i],end=" ")