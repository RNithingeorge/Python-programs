def find_duplicates(array):
  freq = {}
  for num in array:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
  duplicates = []
  for key, value in freq.items():
    if value > 1:
      duplicates.append(key)
  return duplicates

array = list(map(int,input().split()))
print( find_duplicates(array))
