# You are given an integer array. Print all the subarrays.
# A subarray is defined as a contiguous portion of an array.
# Print the subarrays in an order specified in the sample input / output.
# Sample Input: 
# 3 2 1
# Sample Output: 
# 3
# 3 2
# 3 2 1
# 2
# 2 1
# 1


arr=[3,2,1]

for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
          print(arr[i:j])