def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
  
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)

    diffs_valid = all(1 <= abs(d) <= 3 for d in diffs)

    return (all_increasing or all_decreasing) and diffs_valid


safe_count = 0

with open("input2.txt") as f:
    for line in f:
        if line.strip():
            levels = list(map(int, line.strip().split()))
            if is_safe(levels):
                safe_count += 1

print("Safe reports count:", safe_count)
