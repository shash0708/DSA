# Function to find the minimum and maximum difference in an array
def find_min_max_difference(arr):
    # Sort the array
    arr.sort()
    
    # Minimum difference initialized to a large number
    min_diff = float('inf')
    
    # Maximum difference is the difference between the largest and smallest element
    max_diff = arr[-1] - arr[0]
    
    # Loop through the sorted array to find the minimum difference between adjacent elements
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
    
    # Return both the minimum and maximum differences
    return min_diff, max_diff

# Sample Input
arr = [5, 4, 7, 8, 4, 6, 11, 9]

# Find the minimum and maximum difference
min_diff, max_diff = find_min_max_difference(arr)

# Print the result
print(min_diff, max_diff)
