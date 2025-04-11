import re

with open("input3.txt") as f:
    memory = f.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, memory)

total = sum(int(x) * int(y) for x, y in matches)

print("Total sum of multiplications:", total)
