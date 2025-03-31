# 1- Numeric

# int → Integer (whole numbers)
integer = 10
print(f"The type of integer is :{type(integer)}")

# float → Floating-point numbers (decimal values)
float = 10.5
print(f"The type of float is :{type(float)}")

# complex → Complex numbers (a + bj)

z = 3 + 4j
print(f"The type of z is :{type(z)}")

# -----------------------------------------
# 2: Boolean Type
value = True
value = False
print(f"The type of value is :{type(value)}")

# ----------------------------------------
# 3 : Sequence Types
# Used for ordered collections of elements.

# str → String (text)
name = "sadam"
print(f"The type of name is :{type(name)}")

# list → Ordered, mutable collection
sections = ["A", "B", "C", "D", ["aa", "bb", "cc", "dd"]]
print(sections)
print(f"The type of sections is :{type(sections)}")

# range → Generates a sequence of numbers
r = range(5)  # range (0,5)
# covert into tuple or list and then it will show all number

print(list(r))
print(tuple(r))
# -------------------------------------
# Set Types

set = {1, 2, 3, 4, 5, 2, 3, 4, 4}
print(set)  # shows unique values

# 5. Mapping Type
# dict → Dictionary (key-value pairs)
import json

person = [
    {"name": "Sadam", "age": 22},
    {"name": "Ali", "age": 22},
    {"name": "Ahmad", "age": 22},
    {"name": "Hasnain", "age": 22},
    {"name": "Hamza", "age": 22},
    {"name": "Mateen", "age": 22},
]

print(json.dumps(person, indent=2))  # Pretty print JSON
