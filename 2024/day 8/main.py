def day8_1(input_data):
    lines = input_data.strip().split("\n")
    grid = [list(line) for line in lines]

    antennas = {}
    anti_nodes = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != ".":
                if grid[row][col] not in antennas:
                    antennas[grid[row][col]] = []
                antennas[grid[row][col]].append((row, col))

    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1 = positions[i]
                pos2 = positions[j]

                delta_row = pos2[0] - pos1[0]
                delta_col = pos2[1] - pos1[1]

                anti_node1 = (pos1[0] - delta_row, pos1[1] - delta_col)
                anti_node2 = (pos2[0] + delta_row, pos2[1] + delta_col)

                if 0 <= anti_node1[0] < len(grid) and 0 <= anti_node1[1] < len(grid[0]):
                    anti_nodes.add(anti_node1)

                if 0 <= anti_node2[0] < len(grid) and 0 <= anti_node2[1] < len(grid[0]):
                    anti_nodes.add(anti_node2)

    output = len(anti_nodes)
    print("Output Day 8 Part 1:", output)


def day8_2(input_data):
    lines = input_data.strip().split("\n")
    grid = [list(line) for line in lines]

    antennas = {}
    anti_nodes = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != ".":
                if grid[row][col] not in antennas:
                    antennas[grid[row][col]] = []
                antennas[grid[row][col]].append((row, col))

    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1 = positions[i]
                pos2 = positions[j]

                delta_row = pos2[0] - pos1[0]
                delta_col = pos2[1] - pos1[1]

                anti_node1_row, anti_node1_col = pos1[0], pos1[1]
                while 0 <= anti_node1_row < len(grid) and 0 <= anti_node1_col < len(
                    grid[0]
                ):
                    anti_nodes.add((anti_node1_row, anti_node1_col))
                    anti_node1_row -= delta_row
                    anti_node1_col -= delta_col

                anti_node2_row, anti_node2_col = pos2[0], pos2[1]
                while 0 <= anti_node2_row < len(grid) and 0 <= anti_node2_col < len(
                    grid[0]
                ):
                    anti_nodes.add((anti_node2_row, anti_node2_col))
                    anti_node2_row += delta_row
                    anti_node2_col += delta_col

    output = len(anti_nodes)
    print("Output Day 8 Part 2:", output)


# Reading from input.txt file
with open(
    "/Users/bwbblegum/Documents/GitHub/Advent-of-Code/2024/day 8/input.txt", "r"
) as file:
    input_data = file.read()

# Call the functions with the input data
day8_1(input_data)
day8_2(input_data)
