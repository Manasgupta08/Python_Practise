# Check if a string is a palindrome
s = 'aba'
if s[::-1] == s:
    print('yes')
else:
    print('NO')

# Count vowels in a string

s = 'aabbcc'
v ={}
count = 0
for i in s:
    if i in v:
        v[i] += 1
    else:
        v[i] = 1
for item,values in v.items():
    print(item,values)

# Longest Substring Without Repeating Characters
# Problem: Given a string, find the length of the longest substring without repeating characters.
# Example: "abcabcbb" → Output: 3
s = 'abcabcbb'
r = set()
l=0
longest = 0
for i in range(len(s)):
    while s[i] in r:
        r.remove(s[l])
        l+=1

    w = (i -l) +1
    longest = max(longest,w)
    r.add(s[i])

print(longest)

# ANAGRAM
s1 = 'listen'
s2 = 'silent'
sorted_S1 = sorted(s1)
sorted_S2 = sorted(s2)
print(sorted_S1 == sorted_S2)
