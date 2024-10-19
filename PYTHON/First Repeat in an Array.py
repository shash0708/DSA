# First Repeat in an Array:
# You are given an integer array. Print the first number that repeats itself. If no number repeats in the array, print No. 
# Sample Input 1:
# 5 11 4 7 8 4 6 11 7
# Sample Output 1:
# 11
# Explanation 1: In the given array, 11 is the first number that repeats itself.
# Sample Input 2:
# 11 1 13 21 3 7
# Sample Output 2:
# No
# Explanation 2: The given array doesn't contain any duplicate element, hence we print No.
 # Add the element to the set
n = [5, 11, 4, 7, 8, 4, 6, 11, 7]

seen = set()  # Set to track seen elements

first_repeated = None  # Variable to store the first repeated element

# Traverse the list from the start
for element in n:
    if element in seen:
        first_repeated = element  # Store the first repeated element
        break  # Stop after finding the first repeated element
    seen.add(element)  # Add the element to the set

# Print the result
if first_repeated is not None:
    print("First repeated element:", first_repeated)
else:
    print("No repeated elements found")
