from collections import Counter


def calculate_similarity_score(input_file):
    left_list = []
    right_list = []

    # Read input file and split the pairs into separate lists
    with open(input_file, "r") as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counts[num] for num in left_list)

    return similarity_score


# Example usage
input_file = "input.txt"  # Replace with the path to your input file
print("Total Similarity Score:", calculate_similarity_score(input_file))
