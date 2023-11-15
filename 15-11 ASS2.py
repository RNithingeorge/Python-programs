n = int(input())

# Get the list elements
lst = list(map(int, input().split()))

# Find the largest element using the reduce() function
from functools import reduce
largest = reduce(lambda x, y: x if x > y else y, lst)

# Print the largest element
print(largest)
