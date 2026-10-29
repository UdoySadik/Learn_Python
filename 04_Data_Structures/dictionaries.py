# ============================================================
# Python Dictionaries (dict) - Complete Beginner Friendly Guide
# ============================================================
# A dictionary is a built-in Python data structure that stores
# data in key:value pairs.
#
# Key Characteristics:
# 1. Ordered (from Python 3.7+)
# 2. Changeable / Mutable (you can add, change, or remove items)
# 3. Keys must be UNIQUE (no duplicate keys allowed)
# 4. Keys must be IMMUTABLE types (string, number, tuple)
# 5. Values can be ANY data type and CAN be duplicated
#
# Real-life analogy:
# - Phonebook: Name -> Phone Number
# - Student Card: Roll -> Student Information
# - Word Dictionary: Word -> Meaning
# ============================================================


# ------------------------------------------------------------
# 1. Creating a Dictionary
# ------------------------------------------------------------
print("--- 1. Creating a Dictionary ---")

# An empty dictionary
empty_dict = {}
# or: empty_dict = dict()

# A simple dictionary representing a student
student = {
    "name": "Udoy",
    "age": 21,
    "department": "CSE",
    "cgpa": 3.85,
    "is_enrolled": True
}

print("Student dictionary:", student)
print("Type:", type(student))
print("Total number of items (len):", len(student))


# ------------------------------------------------------------
# 2. Accessing Values
# ------------------------------------------------------------
print("\n--- 2. Accessing Values ---")

# Method 1: Using square brackets [key]
# Note: If the key is not found, Python will raise a KeyError!
print("Name:", student["name"])
print("Department:", student["department"])

# Method 2: Using .get(key)  -> (Safer method!)
# If the key is not found, it returns None instead of crashing.
print("Age using .get():", student.get("age"))
print("Email (key does not exist):", student.get("email"))

# You can also set a default value if the key does not exist:
print("Email with default:", student.get("email", "Not Available"))


# ------------------------------------------------------------
# 3. Adding and Modifying Items
# ------------------------------------------------------------
print("\n--- 3. Adding and Modifying Items ---")

# Adding a new key-value pair
student["email"] = "udoy@example.com"
print("After adding email:", student)

# Modifying / Updating an existing value
student["age"] = 22
print("After updating age:", student)

# Using .update() method to add or update multiple items at once
student.update({
    "city": "Dhaka",
    "cgpa": 3.90
})
print("After .update():", student)


# ------------------------------------------------------------
# 4. Removing Items from a Dictionary
# ------------------------------------------------------------
print("\n--- 4. Removing Items ---")

# Method 1: .pop(key) - Removes specified key and returns its value
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After .pop('city'):", student)

# Method 2: .popitem() - Removes and returns the LAST inserted item
last_item = student.popitem()
print("Removed last item (key, value):", last_item)
print("After .popitem():", student)

# Method 3: del keyword - Deletes a specific key
del student["is_enrolled"]
print("After del student['is_enrolled']:", student)

# Method 4: .clear() - Empties the entire dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("After temp.clear():", temp)  # prints: {}


# ------------------------------------------------------------
# 5. Checking if a Key Exists
# ------------------------------------------------------------
print("\n--- 5. Checking if Key Exists ---")

# Use the 'in' operator to check keys:
if "name" in student:
    print("Yes, 'name' exists in student!")

if "phone" not in student:
    print("No, 'phone' does not exist in student.")


# ------------------------------------------------------------
# 6. Dictionary Keys, Values, and Items
# ------------------------------------------------------------
print("\n--- 6. Keys, Values, and Items ---")

# .keys() -> returns all keys
print("All keys:", list(student.keys()))

# .values() -> returns all values
print("All values:", list(student.values()))

# .items() -> returns (key, value) pairs as tuples
print("All items:", list(student.items()))


# ------------------------------------------------------------
# 7. Looping Through a Dictionary
# ------------------------------------------------------------
print("\n--- 7. Looping Through Dictionary ---")

print("1. Looping through keys:")
for key in student:
    print(f"   {key} -> {student[key]}")

print("\n2. Looping through values directly:")
for val in student.values():
    print(f"   Value: {val}")

print("\n3. Looping through key and value together (Most Common & Recommended):")
for key, value in student.items():
    print(f"   {key}: {value}")


# ------------------------------------------------------------
# 8. Copying a Dictionary
# ------------------------------------------------------------
print("\n--- 8. Copying a Dictionary ---")

# WARNING: dict2 = dict1 does NOT create a copy!
# Both variables will point to the same memory reference.
# Changing dict2 will also change dict1.

# Correct way: use .copy() or dict()
student_copy = student.copy()
student_copy["name"] = "Rahim"

print("Original student name:", student["name"])      # Still 'Udoy'
print("Copied student name:", student_copy["name"])   # 'Rahim'


# ------------------------------------------------------------
# 9. Nested Dictionaries (Dictionary inside a Dictionary)
# ------------------------------------------------------------
print("\n--- 9. Nested Dictionaries ---")

# Storing information for multiple students
classroom = {
    "student_1": {
        "name": "Udoy",
        "roll": 101,
        "marks": {"math": 90, "physics": 85}
    },
    "student_2": {
        "name": "Rahim",
        "roll": 102,
        "marks": {"math": 78, "physics": 82}
    }
}

# Accessing nested values
print("Student 1 Name:", classroom["student_1"]["name"])
print("Student 1 Math Marks:", classroom["student_1"]["marks"]["math"])

# Looping through nested dictionary
print("\nClassroom details:")
for s_id, s_info in classroom.items():
    print(f"ID: {s_id}")
    print(f"  Name: {s_info['name']}")
    print(f"  Roll: {s_info['roll']}")
    print(f"  Math Mark: {s_info['marks']['math']}")


# ------------------------------------------------------------
# 10. Dictionary Comprehension (Quick Way to Build Dicts)
# ------------------------------------------------------------
print("\n--- 10. Dictionary Comprehension ---")

# Syntax: {key: value for item in iterable}

# Example 1: Create a dictionary of squares for numbers 1 to 5
squares = {num: num ** 2 for num in range(1, 6)}
print("Squares (1 to 5):", squares)

# Example 2: Filtering with condition (only even numbers)
even_squares = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print("Even numbers squared:", even_squares)


# ------------------------------------------------------------
# 11. Practical Real-World Example: Word Frequency Counter
# ------------------------------------------------------------
print("\n--- 11. Real-World Practical Example ---")

# Counting how many times each word appears in a sentence
sentence = "python is fun and python is powerful"
words = sentence.split()

word_counts = {}
for word in words:
    # If word is in dict, increment count, else start with 0 + 1
    word_counts[word] = word_counts.get(word, 0) + 1

print("Sentence:", sentence)
print("Word Frequency:", word_counts)


# ============================================================
# Summary / Cheat Sheet
# ============================================================
# - Create:        my_dict = {"key": "value"}
# - Access:        my_dict["key"]  or  my_dict.get("key", default)
# - Add/Update:    my_dict["new_key"] = value  or  my_dict.update({...})
# - Remove:        my_dict.pop("key")  or  del my_dict["key"]
# - Keys/Values:   my_dict.keys(), my_dict.values(), my_dict.items()
# - Check exists:  "key" in my_dict
# - Loop:          for k, v in my_dict.items():
# ============================================================

