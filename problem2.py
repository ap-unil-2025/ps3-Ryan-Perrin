"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32 

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    return (celsius * 9/5) + 32 #implementation of the formula above for the conversion celsius to fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    return (fahrenheit - 32) * 5/9 #implementation of the formula above for the conversion fahrenheit to celsius


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    try : #if the input is correct, it will run the code below. Otherwise, it will go to except ValueError
        temp = float(input("Enter the termperature value : ")) #converts the string into a float
        unit = input("Enter the unit (C for celsius and F for fahrenheit) : ").strip().upper() #removes spaces and converts the input into an uppercase if it wasn't one
        if unit == "C" : #if unit is celsius, we convert to fahrenheit
            result = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {result:.2f}°F") #.2f : formats the output with 2 decimal places
        elif unit == "F": #if unit is fahrenheit, we convert to celsius
            result = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F is {result:.2f}°C")
        else:
            print ("Please enter C or F.") #prevents if something else than c or f is typed
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value") 


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()