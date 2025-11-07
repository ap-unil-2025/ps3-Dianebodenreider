def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []
    while True:
        raw = input("Enter a number (or 'done' to finish): ").strip()
        if raw.lower() == "done":
            break
        try:
            num = float(raw)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers


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
        return None

    count = len(numbers)
    total = sum(numbers)
    avg = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    # Compter pairs/impairs uniquement pour les valeurs entières
    even_count = sum(1 for x in numbers if float(x).is_integer() and int(x) % 2 == 0)
    odd_count = sum(1 for x in numbers if float(x).is_integer() and int(x) % 2 != 0)

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
    print(f"Sum: {analysis['sum']:.2f}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even count: {analysis['even_count']}")
    print(f"Odd count: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.\n")

    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered.")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
