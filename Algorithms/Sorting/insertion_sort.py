def insertion_sort(array):
  for i in range(1,len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j+1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array
    
x = [37, 19, 80, 52, 53, 89, 48, 57, 15, 50, 39, 68, 97, 3, 51, 86, 56 , 1, 98, 38, 79, 16, 13]
print("Un-sorted array:",x)
x_sorted = insertion_sort(x)
print("Sorted array:",x_sorted)
