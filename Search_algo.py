# LINEAR SEARCH     NO SORTING NEEEDEED  T.C- O(N)   NOT FOR LARGE DATASET

def linear_search(arr,item):
    for i in range (len(arr)):
        if arr[i] == item:
            return i
    return -1
    
arr = [1,2,3,4,5,56,6]
print(linear_search(arr,4))

# BINARY SEARCH     SORTING NEEEDEED  T.C- O(N)   FOR LARGE DATASET -- AMORTIZED COST

def binary_search(arr,low,high,item):
    if low <= high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
        
    return -1

binary_search(arr,0 ,len(arr)-1,4) 

 # INTERPOLATION SEARCH  is an improved variant of Binary Search.It works best on uniformly distributed, sorted data.Instead of always picking the middle index like binary search, it estimates the position of the key using the interpolation formula.
# pos = low + ((key-arr[low])(high-low))//(arr[high]-arr[low])

def interpolation_search(arr,low,high,key):
    while arr[low] <= arr[high] and arr[low] != arr[high]:
        pos = low + ((key-arr[low]) * (high-low))//(arr[high]-arr[low])
        if pos < 0 or pos > len(arr):
            return -1
        elif arr[pos] == key:
            return pos
        elif arr[pos] > key:
            high = pos -1
        else:
            low = pos +1
    return -1

ids = list(range(1000, 2000))  # uniform
print(interpolation_search(ids,0,len(ids)-1 , 1540))  # Output: Index of 1540