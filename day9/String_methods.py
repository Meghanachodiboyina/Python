text = "   python Programming 123   "

print("Original string:", text)

# strip methods
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# case conversion
print("lower():", text.lower())
print("upper():", text.upper())
print("title():", text.title())
print("capitalize():", text.capitalize())

# replace
print("replace():", text.replace("python", "Java"))

# split and join
words = text.split()
print("split():", words)
print("join():", "-".join(words))

# find and count
print("find():", text.find("Pro"))
print("count():", text.count("o"))

# checking methods
print("startswith():", text.startswith("python"))
print("endswith():", text.endswith("123"))

# type checking
print("isdigit():", "123".isdigit())
print("isalpha():", "hello".isalpha())
print("isalnum():", "abc123".isalnum())

# length
print("length:", len(text))