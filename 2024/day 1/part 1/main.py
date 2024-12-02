def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


# Read the input file and populate the lists
left_list = []
right_list = []

with open("input.txt", "r") as file:
    for line in file:
        # Split the line into two numbers and convert them to integers
        l, r = map(int, line.split())
        left_list.append(l)
        right_list.append(r)

# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print("Total Distance:", total_distance)
