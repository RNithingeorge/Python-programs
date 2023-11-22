
n = int(input())

armstrong_numbers = [num for num in range(1, n+1) if sum([int(digit)**len(str(num)) for digit in str(num)]) == num]

print("Armstrong numbers from 1 to", n, "are:", armstrong_numbers)

