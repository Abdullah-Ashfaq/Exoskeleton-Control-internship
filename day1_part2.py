from collections import Counter

# Read file and split into left/right again
with open("input.txt") as f:
    lines = f.read().strip().split('\n')

left = []
right = []

for line in lines:
    if line.strip():
        l, r = map(int, line.strip().split())
        left.append(l)
        right.append(r)

# Count how many times each number appears in the right list
right_counts = Counter(right)

# Calculate the similarity score
similarity_score = sum(x * right_counts[x] for x in left)

print("Similarity score:", similarity_score)
