
name = 'farhan'

# Length
print("length =", len(name))

# Starts with
print("Start with =", name.startswith("far"))

# Ends with
print("End with =", name.endswith("han"))

# First letter capital
print("First letter capital =", name.capitalize())

# All letters capital
print("All capital =", name.upper())

# All letters small
print("All small =", name.lower())

# Swap uppercase and lowercase
print("Swap case =", name.swapcase())

# Title case
print("Title case =", name.title())

# Count a letter
print("Count of a =", name.count("a"))

# Find position of a letter
print("Find a =", name.find("a"))

# Find from right side
print("Find from right =", name.rfind("a"))

# Find position (error if not found)
print("Index of r =", name.index("r"))

# Check whether all characters are letters
print("Is alphabet =", name.isalpha())

# Check whether all characters are numbers
print("Is digit =", name.isdigit())

# Check whether all characters are letters or numbers
print("Is alphanumeric =", name.isalnum())

# Check whether all characters are lowercase
print("Is lowercase =", name.islower())

# Check whether all letters are uppercase
print("Is uppercase =", name.isupper())

# Check whether the string contains only spaces
print("Is whitespace =", name.isspace())

# Replace a part of the string
print("Replace =", name.replace("far", "sar"))

# Remove spaces from both sides
print("Strip =", name.strip())

# Remove spaces from left side
print("Left strip =", name.lstrip())

# Remove spaces from right side
print("Right strip =", name.rstrip())

# Split string into a list
print("Split =", name.split("a"))

# Join strings
print("Join =", "-".join(["far", "han"]))

# Check whether string is title case
print("Is title =", name.istitle())

# Check whether string is printable
print("Is printable =", name.isprintable())

# Check whether string is ASCII
print("Is ASCII =", name.isascii())

# Check whether string is a valid identifier
print("Is identifier =", name.isidentifier())

# Center the string
print("Center =", name.center(12, "-"))

# Left align
print("Left align =", name.ljust(12, "-"))

# Right align
print("Right align =", name.rjust(12, "-"))

# Add zeros at the beginning
print("Zero fill =", name.zfill(10))

# Partition at a specific character
print("Partition =", name.partition("r"))

# Partition from the right
print("Right partition =", name.rpartition("a"))

# Remove a prefix
print("Remove prefix =", name.removeprefix("far"))

# Remove a suffix
print("Remove suffix =", name.removesuffix("han"))



# First character
print("First character =", name[0])

# Last character
print("Last character =", name[-1])

# First three characters
print("First three =", name[:3])

# Characters from index 2 to 4
print("Slicing =", name[2:5])

# Reverse string
print("Reverse =", name[::-1])

# Check whether a string is contained
print("Contains far =", "far" in name)

# Concatenation
print("Add strings =", name + " sadik")

# Repeat string
print("Repeat =", name * 3)