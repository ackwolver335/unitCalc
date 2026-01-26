# here is a Module related to the Outcomes of your BMI ensuring your health status
# This contains only a single class in which you have to enter the data once and get the data in that contain default functions

# it contains different methods in order to find the BMI of any particular method available in it
# further description is been given below with the methods and inside them

"""------- Main File contains the Methods or Functions that are mentioned below ! -------"""

methods = [
    '__init__(self)',
    'heightinch(self,h,w)',
    'heightmtr(self,h,w)',
    'heightcm(self,h,w)',
    'heightfoot(self,h,w)'
]

class BMI:
    weight = 0
    height_in_cm = 0
    height_in_m = 0
    height_in_foot = 0
    height_in_inch = 0

    # ----------- Initial Method for initiating objects and their overview on different available methods ------------------
    # ----------------------------------------------------------------------------------------------------------------------
    # This Module together with the initial one have its overall proper data over to the Github : @ackwolver335 ------------

    def __init__(self):
        """
            :: BMI Module ::
        
            Class : BMI
            Function : __init__(self) don't contains different argument at initialization phase
            At initial phase we're not taking different methods in order to take any argument at once.
            We are getting the data at the run time of the program 

            Below we have different of its data members :
            1. weight : Generally taken in KG as its default unit
            2. Height in cm : First initialisation of height regarding cm unit
            3. Height in m : Second initialization if the user wants to give the height in mtr unit
            4. Height in Foot : Third initialization for the user, if he/she wants to give height in Foots
            5. Height in inches : Last one regarding the height in inches unit.

            BMI Module -> Designed by Abhay Chaudhary.
        """

        # General Overview of the BMI Program method in it
        # Here we have used the pass methods for initiating from it
        # Normal use of pass keyword

        pass

    def heightinch(self,h,w):

        # Basic Overview of Height in Inches
        # General Overview of this method regarding this Module

        """
            :: BMI Module ::

            Class : BMI
            Function : heightinch(self,h,w) at initial phase it contains two arguments to be passed

            Arguments : 
            h : It stands for Height in unit inches.
            w : It is a general weight in kilogram's units.
            Note : At the end it would return the BMI after proper calculation.

            BMI Module -> Designed by Abhay Chaudhary
        """

        # Basic and General Code Method Initialization
        # Contain the main raw code for getting BMI of that particular User

        height = h * 0.0254
        weight = w
        self.height_in_inch = weight / (height ** 2)
        return self.height_in_inch

    def heightmtr(self,h,w):

        # Generally contains the conversion of given details in a BMI Program
        # Conversion of details in BMI to get and feel better

        """
            :: BMI Module ::

            Class : BMI
            Function :  heightmtr(self,h,w) at initial phase it contains two argument to be passed

            Arguments : 
            h : It stands for height in unit meter.
            w : It is a general weight in kilogram's units.
            Note : At the end it would return the BMI Value after calculating it as per the given value.

            BMI Module -> Designed by Abhay Chaudhary
        """

        # General source code before interpretation
        # main code of the method

        height = h
        weight = w
        self.height_in_m = weight / (height ** 2)
        return self.height_in_m

    def heightcm(self,h,w):

        # At the first phase it contains simple calculation for BMI Calculation
        # Calculation of BMI regarding unit which is cms.

        """
            :: BMI Module ::

            Class : BMI
            Function : heightcm(self,h,w) at starting point it takes two necessary argument for getting BMI

            Arguments :
            h : It stands for height in unit centimtr.
            w : It is a general weight in kilogram's units.
            Note : At the end of the function or method it returns the value of BMI after proper calculation.

            BMI Module -> Desigend by Abhay Chaudhary
        """

        # General code for quantity work
        # main source code

        height = h / 100
        weight = w
        self.height_in_cm = weight / (height ** 2)
        return self.height_in_cm

    def heightfoot(self,h,w):

        # General Code regarding intro at initial stage of method
        # Main source code this is after explanation

        """
            :: BMI Module ::

            Class : BMI
            Function : heightfoot(self,h,w) at initial it requires 2 argument for calculating the BMI

            Arguments :
            h : It stands for heights in unit foot.
            w : It is a general weight in kilogram's unit.
            Note : At the end of the method it returns the value of BMI after proper calculations.

            BMI Module -> Designed by Abhay Chaudhary
        """

        # The Information is necessary for programmer or developers in order to understand the source code.
        # Main source code regarding BMI Calculation

        height = h * 0.304
        weight = w
        self.height_in_foot = weight / (height ** 2)
        return self.height_in_foot
    
    # ------------------------------------------ END OF CODE ------------------------------------------------
    # ------------------ Module file is been ended here regarding the code and more knowledge ---------------
    # ------------------------------------------ Thanks for Visiting ----------------------------------------