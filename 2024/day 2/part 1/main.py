def is_safe_report(report):
    # Calculate differences between consecutive levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if differences are all increasing or all decreasing
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    # Report is safe if it's either entirely increasing or entirely decreasing
    return is_increasing or is_decreasing


def analyze_reports(input_file):
    safe_reports = 0

    # Read reports from input file
    with open(input_file, "r") as file:
        for line in file:
            # Parse the report into a list of integers
            report = list(map(int, line.strip().split()))
            if is_safe_report(report):
                safe_reports += 1

    return safe_reports


# Example usage
input_file = "input.txt"  # Replace with the path to your input file
print("Number of Safe Reports:", analyze_reports(input_file))
