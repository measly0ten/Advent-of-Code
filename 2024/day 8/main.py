def parse_map(input_map):
    """Parse the input map into a list of antenna locations grouped by frequency."""
    antennas = {}
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas


def find_antinodes(antennas, width, height):
    """Find all unique antinode locations within the map boundaries."""
    antinodes = set()

    for freq, positions in antennas.items():
        print(f"Processing frequency: {freq} with positions: {positions}")
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate X-Y distance
                dx = x2 - x1
                dy = y2 - y1

                # New points in opposite directions
                new_point_a = (x1 - dx, y1 - dy)
                new_point_b = (x2 + dx, y2 + dy)

                # Check if points are within grid boundaries
                if 0 <= new_point_a[0] < width and 0 <= new_point_a[1] < height:
                    antinodes.add(new_point_a)
                    print(f"Antinode added at: {new_point_a}")
                if 0 <= new_point_b[0] < width and 0 <= new_point_b[1] < height:
                    antinodes.add(new_point_b)
                    print(f"Antinode added at: {new_point_b}")

    return antinodes


# Rest of the code remains unchanged


# Read input from a file
with open(
    "/Users/bwbblegum/Documents/GitHub/Advent-of-Code/2024/day 8/input.txt", "r"
) as file:
    input_map = file.read().strip().split("\n")

# Map dimensions
height = len(input_map)
width = len(input_map[0])

# Parse the map and find antennas
antennas = parse_map(input_map)

# Find unique antinodes
unique_antinodes = find_antinodes(antennas, width, height)

# Count and output the result
print("Total Unique Antinode Locations:", len(unique_antinodes))
