def print_elements(n, arr, interval):
   
    elements = arr[interval[0]:interval[1]+1]
   
    elements.sort(reverse=True)
   
    arr[interval[0]:interval[1]+1] = elements
    return arr

n = 8  
arr = [12, 45, 85, 96, 2, 0, 4, 9] 
interval = [3, 6] 

print(print_elements(n, arr, interval))
