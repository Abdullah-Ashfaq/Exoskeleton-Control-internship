import re

with open("input3.txt") as f:
    memory = f.read()

# Pattern to match all: do(), don't(), mul(X,Y)
pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
tokens = re.finditer(pattern, memory)

enabled = True
total = 0

for match in tokens:
    full = match.group(1)
    x = match.group(2)
    y = match.group(3)

    if full == "do()":
        enabled = True
    elif full == "don't()":
        enabled = False
    elif x and y and enabled:
        total += int(x) * int(y)

print("Total from enabled multiplications:", total)
