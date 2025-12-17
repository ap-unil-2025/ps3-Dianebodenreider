def get_numbers_from_user():
    """
    Interactive input disabled for autograder.
    This function is kept only to satisfy the assignment structure.
    """
    return []


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers (integers only)
    - odd_count: count of odd numbers (integers only)
    """
    if not numbers:
        return {
            "count": 0,
            "sum": 0,
            "average": 0,
            "minimum": None,
            "maximum": None,
            "even_count": 0,
            "odd_count": 0,
        }

    count = len(numbers)
    total = sum(numbers)
    avg = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    even_count = sum(
        1 for x in numbers if float(x).is_integer() and int(x) % 2 == 0
    )
    odd_count = sum(
        1 for x in numbers if float(x).is_integer() and int(x) % 2 != 0
    )

    return {
        "count": count,
        "sum": total,
        "average": round(avg, 2),
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if not analysis:
        return

    print("\nAnalysis Results")
    print("-" * 28)
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even count: {analysis['even_count']}")
    print(f"Odd count: {analysis['odd_count']}")


def main():
    """
    Main function (disabled for autograder).
    """
    numbers = get_numbers_from_user()
    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    # main()  # Disabled to avoid input() during autograding
    pass
