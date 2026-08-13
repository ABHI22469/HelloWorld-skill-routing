# package: com.staymind

"""Temperature conversion calculator.

Supports conversions between Celsius, Fahrenheit, and Kelvin.
"""

ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    """Convert a Celsius temperature to Kelvin."""
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("Temperature below absolute zero is not physically possible.")
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert a Kelvin temperature to Celsius."""
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not physically possible.")
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert a Fahrenheit temperature to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin):
    """Convert a Kelvin temperature to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def _run_cli():
    """Simple interactive calculator for the command line."""
    conversions = {
        "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit),
        "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius),
        "3": ("Celsius to Kelvin", celsius_to_kelvin),
        "4": ("Kelvin to Celsius", kelvin_to_celsius),
        "5": ("Fahrenheit to Kelvin", fahrenheit_to_kelvin),
        "6": ("Kelvin to Fahrenheit", kelvin_to_fahrenheit),
    }
    print("Temperature Conversion Calculator")
    for key, (label, _) in conversions.items():
        print(f"  {key}. {label}")
    choice = input("Choose a conversion (1-6): ").strip()
    if choice not in conversions:
        print("Invalid choice.")
        return
    label, func = conversions[choice]
    value = float(input(f"Enter the temperature to convert ({label}): "))
    try:
        result = func(value)
        print(f"{value} -> {result:.2f}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    _run_cli()
