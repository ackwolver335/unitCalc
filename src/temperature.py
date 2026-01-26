# Here is another conversion units of temperature related
# Following units are envolved here
# Celsius, Fahrenheit, Kelvin, Rankine, reaumur

# It contains different methods regariding the calculation of temperature in different available units
# further description is been given below regarding the code and method's explanation

"""---- Main File contains the Methods or Functions that are mentioned below ! -----"""

celsius_methods = [
    '__init__(self)',
    'c2F(self,value)',
    'c2k(self,value)',
    'c2rrankine(self,value)',
    'c2reaumur'
]

class celsius:
    celsius = 0

    # ------------ Initial Methods for initiating objects and their overview on different available methods ------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This Module together with the intial one have its overall proper data over to the Github : @ackwolver335 ---------------

    def __init__(self):
        """
            :: Temperature Module ::

            Class : celsius
            Function : __init__(self) it don't contains different arguments at its initial phase
            We are getting the data at the runtime of the Program.

            Also the available data members of this one is explained below :
            1. celsius : This is generally used in order to store the value after getting converted in the required unit in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # Here we have a general use of pass keyword as we don't have further code in __init__() method.
        pass

    def c2F(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2F(self,value) in general for conversion of one unit into another, we uses this value.

            Arguments :
            value : It stands for the value of celsius to be converted into Fahrenheit Temperature Unit.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius into Fahrenheit Unit

        celsius = (value * 1.8) + 32
        return celsius

    def c2k(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2k(self,value) in general for conversion of celsius into kelvin temperature with the use of this value.

            Arguments :
            1. value : It is the main source value regarding the conversion.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius into kelvin unit

        celsius = value + 273.15
        return celsius

    def c2rrankine(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2rrankine(self,value), it contains value argument and self for conversion of temperature into rankine unit.

            Arguments :
            1. value : It is the value of celsius used for conversion into kelvin unit.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius unit into rankine unit

        celsius = ((value * 1.8) + 32) + 459.67
        return celsius

    def c2reaumur(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2reaumur(self,value) its main purpose is to convert the celsius temperature unit into reaumur unit.

            Arguments :
            1. value : It is the value of celsius used for conversion into reaumur units.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius unit into reaumur unit

        celsius = value * 0.8
        return celsius

class Fahrenheit:
    fahrenheit = 0

    # ------------------------------------------ Initial Methods of Fahrenhiet Class -----------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This class and its methods has its original phase with its overall data on Github Repository : @ackwolver335 -----------

    def __init__(self):

        """
            :: Temperature Module ::
            
            Class : Fahrenheit
            Function : __init__(self) this is a general initiating function or method that is used in order to initiate the class
            Further data is over to the runtime of the class's method.

            Also below we have the variable available and used in this class :
            1. fahrenheit : It is used for storing and then returning the data after getting its final unit value in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # General pass keyword or statement added for simple __init__() method.
        pass

    def f2c(self,value):

        """
            :: Temperature Module ::

            Class : Fahrenheit
            Function : f2c(self,value) it is structured and is been defined in a way in order to convert the fahrenheit into celsius

            Arguments :
            1. value : Used for conversion from initial fahrenheit unit to final celsius unit

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below
        # also we have the formula if someone visit the module and want to know how to code works
    
        fahrenheit = (value - 32) / 1.8
        return fahrenheit

    def f2k(self,value):

        """
            :: Temperature Module  ::

            Class : Fahrenheit
            Function : f2k(self,value) is used for conversion of fahrenheit unit of temperature to kelvin unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        fahrenheit = (value + 459) / 1.8
        return fahrenheit

    def f2rankine(self,value):
        
        """
            :: Temperature Module  ::

            Class : Fahrenheit
            Function : f2rankine(self,value) is used for conversion of fahrenheit unit of temperature to rankine unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        fahrenheit = value + 459
        return fahrenheit

    def f2reaumur(self,value):

        """
            :: Temperature Module  ::

            Class : Fahrenheit
            Function : f2reaumur(self,value) is used for conversion of fahrenheit unit of temperature to reaumur unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        fahrenheit = (self.fahrenheit - 32) / 2.25
        return fahrenheit

class Kelvin:
    kelvin = 0

    # ------------------------------------------ Initial Methods of Kelvin Class ---------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This class and its methods has its original phase with its overall data on Github Repository : @ackwolver335 -----------

    def __init__(self):

        """
            :: Temperature Module ::

            Class : Kelvin
            Function : __init__(self) it don't contains different arguments at its initial phase
            We are getting the data at the runtime of the Program.

            Also the available data members of this one is explained below :
            1. celsius : This is generally used in order to store the value after getting converted in the required unit in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # Here we have a general use of pass keyword as we don't have further code in __init__() method.        
        pass

    def k2F(self,value):

        """
            :: Temperature Module  ::

            Class : Kelvin
            Function : k2F(self,value) is used for conversion of kelvin unit of temperature to fahrenheit unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        kelvin = (value * 1.8) - 459
        return kelvin

    def k2c(self,value):

        """
            :: Temperature Module  ::

            Class : Kelvin
            Function : k2c(self,value) is used for conversion of kelvin unit of temperature to celsius unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        kelvin = value - 273.15
        return kelvin

    def k2rankine(self,value):

        """
            :: Temperature Module  ::

            Class : Kelvin
            Function : k2rankine(self,value) is used for conversion of kelvin unit of temperature to rankine unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        kelvin = value * 1.8
        return kelvin

    def k2reaumur(self,value):

        """
            :: Temperature Module  ::

            Class : Kelvin
            Function : k2reaumur(self,value) is used for conversion of kelvin unit of temperature to reaumur unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        kelvin = (value - 273.15) * 0.8
        return kelvin

class Rankine:
    rankine = 0

    # ------------------------------------------ Initial Methods of Rankine Class --------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This class and its methods has its original phase with its overall data on Github Repository : @ackwolver335 -----------

    def __init__(self):

        """
            :: Temperature Module ::

            Class : Rankine
            Function : __init__(self) it don't contains different arguments at its initial phase
            We are getting the data at the runtime of the Program.

            Also the available data members of this one is explained below :
            1. celsius : This is generally used in order to store the value after getting converted in the required unit in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # Here we have a general use of pass keyword as we don't have further code in __init__() method.
        pass

    def rank2F(self,value):

        """
            :: Temperature Module  ::

            Class : Rankine
            Function : rank2F(self,value) is used for conversion of rankine unit of temperature to fahrenheit unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        rankine = value - 459
        return rankine
    
    def rank2C(self,value):

        """
            :: Temperature Module  ::

            Class : Rankine
            Function : rank2c(self,value) is used for conversion of rankine unit of temperature to celsius unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        rankine = ((value - 32) - 459) / 1.8
        return rankine

    def rank2k(self,value):

        """
            :: Temperature Module  ::

            Class : Rankine
            Function : rank2k(self,value) is used for conversion of rankine unit of temperature to kelvin unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        rankine = value / 1.8
        return rankine

    def rank2reaumur(self,value):

        """
            :: Temperature Module  ::

            Class : Rankine
            Function : rank2reaumur(self,value) is used for conversion of rankine unit of temperature to reaumur unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        rankine = ((value - 32) - 459) / 2.25
        return rankine

class Reaumur:
    reaumur = 0

    # ------------------------------------------ Initial Methods of Reaumur Class --------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This class and its methods has its original phase with its overall data on Github Repository : @ackwolver335 -----------

    def __init__(self):

        """
            :: Temperature Module ::

            Class : Reaumur
            Function : __init__(self) it don't contains different arguments at its initial phase
            We are getting the data at the runtime of the Program.

            Also the available data members of this one is explained below :
            1. celsius : This is generally used in order to store the value after getting converted in the required unit in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # Here we have a general use of pass keyword as we don't have further code in __init__() method.
        pass

    def reaum2F(self,value):

        """
            :: Temperature Module  ::

            Class : Reaumur
            Function : reaum2F(self,value) is used for conversion of reaumur unit of temperature to fahrenheit unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        reaumur = (value * 2.25) + 32
        return reaumur

    def reaum2C(self,value):

        """
            :: Temperature Module  ::

            Class : Reaumur
            Function : reaum2C(self,value) is used for conversion of reaumur unit of temperature to celsius unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        reaumur = value * 1.25
        return reaumur

    def reaum2K(self,value):

        """
            :: Temperature Module  ::

            Class : Reaumur
            Function : reaum2K(self,value) is used for conversion of reaumur unit of temperature to kelvin unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        reaumur = (value * 1.25) + 273.15
        return reaumur

    def reaum2rank(self,value):

        """
            :: Temperature Module  ::

            Class : Reaumur
            Function : reaum2rank(self,value) is used for conversion of reaumur unit of temperature to rankine unit.

            Arguments :
            1. value : Used for storing the values in which is converted or to be convered into different units.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main code data and structure below 
        # Also contains the formular regarding unit conversion

        reaumur = ((value * 2.25) + 32) + 459
        return reaumur