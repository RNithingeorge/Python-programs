def single_number(nums):
  once = 0
  twice = 0
  for num in nums:
    once = (once ^ num) & ~twice
    twice = (twice ^ num) & ~once
  return once

nums = list(map(int,input().split()))
print( single_number(nums))
