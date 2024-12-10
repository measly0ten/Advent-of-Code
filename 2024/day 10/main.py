import sys
from collections import deque


def count_trails(r: int, c: int) -> tuple[int]:
    queue = deque([(r, c)])
    summits = set()
    count = 0
    while queue:
        r, c = queue.popleft()
        if grid[r][c] == 9:
            summits.add((r, c))
            count += 1
            continue
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] + 1 == grid[nr][nc]:
                queue.append((nr, nc))
    return len(summits), count


file_path = ("input.txt ".strip()
)

# Open the file and read its contents
with open(file_path, "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])
zeros = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 0]


part1, part2 = 0, 0
for start in zeros:
    trails, paths = count_trails(*start)
    part1 += trails
    part2 += paths

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
