# Check Array for Palimdrome:
# You are given an array of integers. Check if the given array is a Palindrome. If it is a Palindrome array, print yes, else print no.
# Note: A Palindrome Array is when the reverse of the array is the same as the original array.
# Sample Input 1:
# 11 1 13 21 3 7
# Sample Output 1:
# No
# Sample Input 2:
# 17 1 13 1 17
# Sample Output 2:
# Yes
# Explanation 2: The reverse of the array reads same as the original array.


arr1=[11,1,13,21,3,7]

arr=[17,1,13,1,17]

n1=len(arr)

n2=len(arr)

flag=True
for i in range(0,n2//2):
    if(arr[i]==arr[n1-i-1]):
        flag=True
    else:
        flag=False
        break

print("Yes" if flag else "No")