#*****string manipulation*****


# Initial string
s = "   This is Python"

# Strip whitespace from the beginning and end
s_stripped = s.strip()
print("Stripped: ", s_stripped)

# Convert to uppercase
s_upper = s_stripped.upper()
print("Uppercase: ",s_upper)

# Convert to lowercase
s_lower = s_stripped.lower()
print("Lowercase: ",s_lower)

# Replace a word
s_replaced = s_stripped.replace("Python", "Awesome")
print("Replaced: ",s_replaced)

# Split the string into a list of words
s_split = s_stripped.split()
print("Split: ",s_split)

# Find a substring
s_find = s_stripped.find("Python")
print("Find 'Python': ",s_find)

# Check if the string starts with "This"
s_starts = s_stripped.startswith("This")
print("Starts with 'This': ",s_starts)


# Capitalize the first letter of the string
s_capitalize = s.strip().capitalize()
print("Capitalized: ",s_capitalize)

# Title case (capitalize the first letter of each word)
s_title = s.strip().title()
print("Title Case: ",s_title)

# Count occurrences of a substring
s_count = s.strip().count("is")
print("Count of 'is': ",s_count)

# Check if the string is alphanumeric
s_isalnum = s.strip().replace(" ", "").isalnum()  # Remove spaces before checking
print("Is Alphanumeric: ",s_isalnum)

# Check if the string is alphabetic
s_isalpha = s.strip().replace(" ", "").isalpha()  # Remove spaces before checking
print("Is Alphabetic: ",s_isalpha)

# Check if the string is numeric
s_isnumeric = s.strip().isnumeric()
print("Is Numeric: ",s_isnumeric)

# Join a list of strings into one string with a separator
words = ["Python", "is", "fun"]
s_join = " ".join(words)
print("Joined string: ", s_join)

# Check if the string ends with "Python"
s_ends = s.strip().endswith("Python")
print("Ends with 'Python': ", s_ends)

# Swap the case (upper to lower and vice versa)
s_swapcase = s.strip().swapcase()
print("Swap Case: ", s_swapcase)


#*****type conversion******

num = 10

#int to string conversion

num_str = str(num)
print("num_str type is: ",type(num_str))


# string to int conversion
num_str = "20"
num_int = int(num_str)
print("num_int type is : ",type(num_int))

