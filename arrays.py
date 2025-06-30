# Reverse an Array
arr = [1,4,3,3,2,9]
arr = arr[::-1]
# print(arr)

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    # return arr

# Example:
arr = [1, 2, 3, 4, 5]
# print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]
    

# Find the largest/smallest number in an array

arr_2 = [3,45,6,6,5,6]
max_arr = arr[0]
for i in range (len(arr_2)):
    if arr_2[i] > max_arr:
        max_arr = arr_2[i]
# print(max_arr)

min_arr = arr[0]
for i in range (len(arr_2)):
    if arr_2[i] < min_arr:
        min_arr = arr_2[i]
# print(min_arr)


# Remove duplicates from array
arr_3 =[3,45,6,6,5,6]
s = []

for i in arr_3:
    if i not in s:
        s.append(i)
# print(s)

# Given a sorted array, remove the duplicates in-place and return the new length.
# Don't use extra space.
def remove_duplicates(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
remove_duplicates(arr_3)
length = remove_duplicates(arr_3)
print(length)  
print(arr_3[:length])

# Merge nums2 into nums1 as one sorted array.
# Assume nums1 has enough space to hold elements of nums2.

def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
# Merge nums2 into nums1 as one sorted array.
# Assume nums1 has enough space to hold elements of nums2.

def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
# Merge nums2 into nums1 as one sorted array.
# Assume nums1 has enough space to hold elements of nums2.

def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
# Merge nums2 into nums1 as one sorted array.
# Assume nums1 has enough space to hold elements of nums2.

def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
# Merge nums2 into nums1 as one sorted array.
# Assume nums1 has enough space to hold elements of nums2.

# MERGE TWO SORTED ARRAYS
def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Given a sorted array, find if there exists a pair of numbers that sum to a target value.
def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False



# Rotate array (e.g., by 2 steps)
arr = [1, 2, 3, 4, 5, 6]
k = 2  # rotate by 2 steps to the right
# [5, 6, 1, 2, 3, 4]  - output
new_arr = arr[-(k):] + arr[:(len(arr) -k)]
# print(new_arr)

# sliding window questions 
# Problem: Given an array of integers and a number k, find the maximum sum of a subarray of size k.

    # Example: arr = [2, 1, 5, 1, 3, 2], k = 3 → Output: 9
arr = [2, 1, 5, 1, 3, 2]
sum = 0
k = 3
for i in range (k):
    sum += arr[i]
print(sum)
max_sum = sum
for i in range(1,(len(arr)-k)):
    sum = sum - arr[i-1] + arr[i+(k-1)]
    if sum > max_sum:
        max_sum = sum
# print(max_sum)

# First Negative Integer in Every Window of Size K
# Problem: Given an array and a window size k, find the first negative number in every window of size k.
    # Example: arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3 OUTPUT[-1, -1, -7, -15, -15, 0]


arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
l = []
for i in range (k):
    if arr[i] < 0:
        l.append(arr[i])
        min_val = arr[i]
        break
# print(l)
for i in range(1,(len(arr)-k)):
    minn_val = min(min_val, arr[i+(k-1)],arr[i+(k-2)])
    if minn_val <0:
     l.append(minn_val)
    else:
        l.append(0)
# print(l)               #NOT RIGHT







