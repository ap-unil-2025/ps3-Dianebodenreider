def celsius_to_fahrenheit(celsius):
  
    try:
        c = float(celsius)
    except ValueError:
        raise ValueError("Input must be a number.")
    f = (c * 9 / 5) + 32
    return round(f, 2)


def fahrenheit_to_celsius(fahrenheit):
   
    try:
        f = float(fahrenheit)
    except ValueError:
        raise ValueError("Input must be a number.")
    c = (f - 32) * 5 / 9
    return round(c, 2)


def temperature_converter():
 
    print("Temperature Converter")
    print("-" * 30)

    value = input("Enter temperature value: ")


    try:
        value = float(value)
    except ValueError:
        print("Error: temperature must be a number.")
        return

    unit = input("Enter unit (C/F): ").strip().lower()

    if unit == "c":
        result = celsius_to_fahrenheit(value)
        print(f"{value} °C is {result:.2f} °F")
    elif unit == "f":
        result = fahrenheit_to_celsius(value)
        print(f"{value} °F is {result:.2f} °C")
    else:
        print("Error: unit must be C or F.")



if __name__ == "__main__":
    print("Running tests...")
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    
    temperature_converter()
