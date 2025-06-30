# bit manipulation mini-project
# Create a basic filtering engine (like those in databases) using bitmaps and bit manipulation to:
# Represent filters as bitmaps
# Combine filters using AND (&)
# Decode the result into matching rows

data = [
    {"id": 0, "gender": "Male",   "age": 34, "country": "India"},
    {"id": 1, "gender": "Female", "age": 28, "country": "USA"},
    {"id": 2, "gender": "Female", "age": 42, "country": "India"},
    {"id": 3, "gender": "Male",   "age": 25, "country": "India"},
    {"id": 4, "gender": "Male",   "age": 45, "country": "USA"},
    {"id": 5, "gender": "Female", "age": 38, "country": "India"},
]

# Initialize bitmaps
gender_male = 0
age_gt_30 = 0
country_india = 0

# Build bitmaps using bitwise OR (|) and shifts
for user in data:
    idx = user["id"]
    if user["gender"] == "Male":
        gender_male |= (1 << idx)
    if user["age"] > 30:
        age_gt_30 |= (1 << idx)
    if user["country"] == "India":
        country_india |= (1 << idx)

#  Combine Filters with AND
result = gender_male & age_gt_30 & country_india

gender_male     = 0b00011001  
age_gt_30       = 0b00110101  j
country_india   = 0b00110101  
result          = 0b00010001  \

# Decode Result

for i in range(len(data)):
    if (result >> i) & 1:
        print(f"User ID {i} matches: {data[i]}")




