with open("input.txt") as f:
    lines = f.read().strip().split('\n')

left = []
right = []

for line in lines:
    if line.strip():  
        l, r = map(int, line.strip().split())
        left.append(l)
        right.append(r)


left.sort()
right.sort()

total_distance = sum(abs(l - r) for l, r in zip(left, right))

print("Total distance:", total_distance)
