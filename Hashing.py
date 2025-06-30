# Using hash() Function
print(hash("apple"))  # Generates a unique hash value
print(hash(12345))    # Hash of an integer

# Hash Set for Deduplication
def remove_duplicates(data):
    return list(set(data))

data = ["a@x.com", "b@y.com", "a@x.com"]
print(remove_duplicates(data))  # ['a@x.com', 'b@y.com']

# Hash Map (Dictionary) for Frequency Count
def freq_count(items):
    freq = dict()
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

print(freq_count(['a', 'b', 'a']))

# Hash Map for Two Sum Problem
def two_sum(nums,target):
    values = {}
    for i ,nums in enumerate(nums):
        compliment = target - nums
        if compliment in values:
            return (values[compliment],i)
        values[nums] = i
    return None
print(two_sum([2, 7, 11, 15], 9))

# IMPLEMENTING A HASH TABLE
class hashtable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
        self.table[index].append([key,value])

    def get_element(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    
ht = hashtable()
ht.insert("apple", 5)
ht.insert("banana", 10)
print(ht.get_element("apple"))  # 5


