"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        user_input = input("Enter a number (or 'done' to finish): ").strip().lower() #ask to the user to enter an input
        if user_input =="done":
            break #if user enters "done", it breaks
        try:
            number=float(user_input) #convert the input into a float
            numbers.append(number) #adds to the list if it's done
        except ValueError: #if it can not, return the sentence below
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
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {"count": len(numbers), #calculate how many numbers there are in the list
    "sum": sum(numbers), #calculate the sum of all the numbers
    "average": sum(numbers) / len(numbers), #give an average of all the numbers by dividing the sum by the number of numbers
    "minimum": min(numbers), #gives the smallest number of the list
    "maximum": max(numbers), #gives the biggest number of the list
    "even_count": sum(1 for n in numbers if n.is_integer() and int(n) % 2 == 0), #count even numbers with the modulo that shows that the number is divisible by 2
    "odd_count": sum(1 for n in numbers if n.is_integer() and int(n) % 2 != 0),} #count odd numbers with the modulo that shows that these numbers are not divisible by 2 (into an int)

    # TODO: Calculate count 
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Count: {analysis['count']}") #print all the results analyzed before
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()