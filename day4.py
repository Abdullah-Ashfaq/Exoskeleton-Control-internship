with open("input4.txt") as f:
    grid = [line.strip() for line in f if line.strip()]

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Directions: right, down, diag ↘, diag ↙
    directions = [
        (0, 1),    
        (1, 0),    
        (1, 1),    
        (1, -1),   
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                positions = []
                for i in range(word_len):
                    nr = r + dr * i
                    nc = c + dc * i
                    if 0 <= nr < rows and 0 <= nc < cols:
                        positions.append(grid[nr][nc])
                    else:
                        break

                if "".join(positions) == word:
                    count += 1

    return count


print("Total XMAS appearances:", count_xmas(grid))
