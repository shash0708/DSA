# um of Subarrays:
# You are given an integer array. Print the sum of all possible subarrays.
# A subarray is defined as a contiguous portion of an array.
# Sample Input: 
# 3 7 5
# Sample Output: 
# 52
# Explanation: All the subarrays are:
# 3
# 3,7
# 3,7,5
# 7
# 7,5
# 5
# Sum = 3 + (3+7) + (3+7+5) + 7 + (7+5) + 5 = 52

arr = [3, 7, 5]
total_sum = 0

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        total_sum += current_sum

print(total_sum)  # Output should be 52

