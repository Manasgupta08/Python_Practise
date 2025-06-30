# BUBBLE sort     NO EXTRA STORAGE 
arr = [4,2,5,66,33]
def bubble_sort(arr):
    for i in range (len(arr)-1):
        for j in range (len(arr)-1-i):
            if arr[j] >arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] ,arr[j] 
    print(arr)
print(bubble_sort(arr))

# MERGE SORT  FOR MERGING TWO SORTED ARRAYS
def merge_sorted(arr1,arr2):
    i = j = 0
    merged = []
    while i <len(arr1) and j <len(arr2):
        if arr1[i] > arr2[j]:
            merged.append[i]
            i+=1
        else:
            merged.append[j]
            j+=1
        while i <= len(arr1):
            merged.append[i]
            i+=1

        while j<= len(arr2):
            merged.append[j]
            j+=1
    return arr

def merge_sort(arr):                   #TIME COMPLEXITY NLOGN
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted(left,right)

# QUICK SORT Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. It is one of the most commonly used and fastest general-purpose sorting techniques.  FASTEST SORTING IN PLACE
# FOR SORTINS A ARRAY

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


arr1 = [3,4,5,1,2]
print(quick_sort(arr1))