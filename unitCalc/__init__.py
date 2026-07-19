"""
Package Name : unitCalc

A lightweight units conversion package for converting units without letting import the actual values or importing them again and again or checking the values again and again.

Features or values available for Conversion :
--------------------------------------------
- Length Conversion
- Weight Conversion
- Temperature Conversion
- Volume Conversion
- Data Storage Conversion
- Time Conversion
- BMI Conversion
- Discount Conversion

Author
------
Abhay Chaudhary

Version
-------
0.1.0
"""

__version__ = "0.1.0"
__author__ = "Abhay Chaudhary"

# import the required modules and classes for their actuall usage
from .bmi import BMI
from .data import Bit, Byte, kilobyte, megabyte, gigabyt, picobyt, terabyt, exabyt, zetabyte, yotabyte
from .discount import Discount
from .length import kilometer, meter, micrometer, millimeter, mile, decimeter, centimeter, nanometer, picometer, yard, Foot, Inch
from .temperature import celsius, Fahrenheit, Kelvin, Rankine, Reaumur
from .time import year, week, days, hour, minute, second, microsec, millisec, picosec, month

# including all classes at once for user side API experience
__all__ = [
    "BMI", "Discount",
    "Bit", "Byte", "kilobyte", "megabyte", "gigabyt", "picobyt", "terabyt", "exabyt", "zetabyte", "yotabyte",
    "kilometer", "meter", "micrometer", "millimeter", "mile", "decimeter", "centimeter", "nanometer", "picometer", "yard", "Foot", "Inch",
    "celsius", "Fahrenheit", "Kelvin", "Rankine", "Reaumur",
    "year", "week", "days", "hour", "minute", "second", "microsec", "millisec", "picosec", "month"
]