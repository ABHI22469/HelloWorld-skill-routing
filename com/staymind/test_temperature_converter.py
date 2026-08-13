# package: com.staymind

import unittest
from com.staymind.temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)


class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit_freezing(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_boiling(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius_freezing(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_fahrenheit_to_celsius_boiling(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_celsius_fahrenheit_crossover_point(self):
        # -40 degrees is the one point where Celsius and Fahrenheit agree.
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_celsius_to_kelvin_at_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)

    def test_celsius_to_kelvin_below_absolute_zero_raises(self):
        with self.assertRaises(ValueError):
            celsius_to_kelvin(-300)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

    def test_kelvin_to_celsius_negative_kelvin_raises(self):
        with self.assertRaises(ValueError):
            kelvin_to_celsius(-5)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)

    def test_round_trip_celsius_to_fahrenheit_and_back(self):
        original = 37.0
        converted_back = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        self.assertAlmostEqual(converted_back, original)


if __name__ == "__main__":
    unittest.main()
