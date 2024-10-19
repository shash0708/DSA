# Find All Pairs with a Given Sum:
# You are given an integer array and a target sum. Find all pairs of elements in the array that add up to the given sum.
# Sample Input: 
# 4 6 7 2 8 9 3 10
# 10
# Sample Output: 
# 4 6
# 7 3
# 2 8
# Explanation: The target sum here is 10. 10=4+6. 10=7+3. 10=2+8. Also, if you have printed the pair 4,6 once, you do not need to print it again as 6,4.


def find_pairs_with_sum(arr, k):
    seen = {}
    
    pairs = []
    
    for num in arr:
        complement = k - num
        
        if complement in seen:
            pairs.append((complement, num))
        else:
            seen[num] = True
    
    return pairs

arr = [3, 6, 2, 1, 7, 3, 7, 4, 1, 7, 4]
k = 10

result = find_pairs_with_sum(arr, k)

print("Pairs with sum", k, ":", result)
