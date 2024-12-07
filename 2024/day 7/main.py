from itertools import product


def evaluate_expression(nums, ops):
    """Evaluates the expression left-to-right given numbers and operators."""
    result = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            result += nums[i + 1]
        elif op == "*":
            result *= nums[i + 1]
        elif op == "||":
            result = int(str(result) + str(nums[i + 1]))
    return result


def find_calibration_results(input_data):
    """Finds the part 1 and part 2 calibration results from the input equations."""
    p1_result = 0
    p2_result = 0

    for line in input_data:
        # Parse the target value and the list of numbers
        target, numbers = line.split(": ")
        target = int(target)
        nums = list(map(int, numbers.split()))

        # Generate all possible combinations of operators for Part 1 and Part 2
        num_ops = len(nums) - 1
        operator_combinations_p1 = product(["+", "*"], repeat=num_ops)
        operator_combinations_p2 = product(["+", "*", "||"], repeat=num_ops)

        # Check for Part 1
        for ops in operator_combinations_p1:
            if evaluate_expression(nums, ops) == target:
                p1_result += target
                break

        # Check for Part 2
        for ops in operator_combinations_p2:
            if evaluate_expression(nums, ops) == target:
                p2_result += target
                break

    return p1_result, p2_result


# Read input from a file
with open("input.txt", "r") as file:
    input_data = file.read().strip().split("\n")

# Calculate the part 1 and part 2 calibration results
p1_result, p2_result = find_calibration_results(input_data)
print("Part 1 Calibration Result:", p1_result)
print("Part 2 Calibration Result:", p2_result)
