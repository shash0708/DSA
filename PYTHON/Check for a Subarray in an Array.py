# Check for a Subarray in an Array
# You are given two arrays. Check if the second array is a subarray of the first array. Print yes if it is, else print no.
# A subarray is defined as a contiguous portion of an array.
# Sample Input 1: 
# 3 6 2 1 7 6 4 9 7
# 7 6 4 9 7
# Sample Output 1: 
# Yes
# Sample Input 2: 
# 3 6 2 1 7 6 4 9 7
# 7 6 4 9 6
# Sample Output 2: 
# No




def is_subarray(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)

    # If the second array is longer, it can't be a subarray
    if len2 > len1:
        return "No"

    # Slide the window across the first array
    for i in range(len1 - len2 + 1):
        # Check if the current window matches the second array
        if arr1[i:i+len2] == arr2:
            return "Yes"

    return "No"

# Example usage
arr1 = [3,6,2,1,7,6,4,9,7]
arr2 = [7,6,4,9,6]
result = is_subarray(arr1, arr2)
print(result)  # Output: Yes
