def is_safe_report(report):
    # Calculate differences between consecutive levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if differences are all increasing or all decreasing
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    # Report is safe if it's either entirely increasing or entirely decreasing
    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    # If the report is already safe, return True
    if is_safe_report(report):
        return True

    # Try removing each level and check if the resulting sub-report is safe
    for i in range(len(report)):
        sub_report = report[:i] + report[i + 1 :]  # Remove one level
        if is_safe_report(sub_report):
            return True

    return False


def analyze_reports_with_dampener(input_file):
    safe_reports = 0

    # Read reports from input file
    with open(input_file, "r") as file:
        for line in file:
            # Parse the report into a list of integers
            report = list(map(int, line.strip().split()))
            if is_safe_with_dampener(report):
                safe_reports += 1

    return safe_reports


# Example usage
input_file = "input.txt"  # Replace with the path to your input file
print(
    "Number of Safe Reports with Dampener:", analyze_reports_with_dampener(input_file)
)
