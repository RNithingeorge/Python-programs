n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
max_element = max(lst)
min_element = min(lst)
diff = max_element - min_element
print(f"{diff}(max:{max_element},min:{min_element},diff={max_element}-{min_element}={diff})")
