import math

class RightTriangle:
    def __init__(self, leg1=None, leg2=None, hyp=None, angle1=None):
        '''
        At least two arguments must be passed in during initialization. The default value for the other arguments is None
        If more than two are passed in, only the first two are used,the others are set to None and than recalculated 
        by Right_Triangle.solve(). angle1 and angle2 are both in degrees and they are the angles adjacent to leg1 and leg2 respectively. 
        For now, each angle must be between 0 and 90 degrees. Each side of the triangle for now must be greater than 0, and the 
        hypotenuse must always be the longest side of the triangle. 

        Calls self.error_checking()
        assigns class attributes by using the return values of self.solve()
        '''
        
        self.error_checking(leg1, leg2, hyp, angle1)

        # Uses the solve method to "solve" the right triangle
        self.leg1, self.leg2, self.hyp, self.angle1, self.angle2 = self.solve(leg1, leg2, hyp, angle1)
        # Assigns class attributes: leg1, leg2, hyp, angle1, angle2

    def __str__(self):
        '''
        Returns a formated string of the triangle's leg1, leg2, hypotenuse, and two angles (besides the right angle of course)
        '''
        return f"{[self.leg1, self.leg2, self.hyp, self.angle1, self.angle2]}"
    
    def return_leg1(self):
        return self.leg1
    
    def return_leg2(self):
        return self.leg2
    
    def return_hypotenuse(self):
        return self.hyp
    
    def return_angle1(self):
        return self.angle1
    
    def return_angle2(self):
        return self.angle2
        
    def calculate_area(self):
        '''
        Returns the area of the triangle, and is calculated using the formula, Area = (base * height) / 2
        '''
        return (self.leg1 * self.leg2) / 2
    
    def calculate_perimeter(self):
        '''
        Returns the perimeter of the triangle
        '''
        return self.leg1 + self.leg2 + self.hyp
   
    @staticmethod
    def solve(leg1=None, leg2=None, hyp=None, angle1=None):
        '''
        Uses the arguments that were passed into the function to calculate the other unknown parts of the right triangle by using
        the math module's sqrt, hypot, and trigonometric functions. This method is always called at initialization.
        Can also be used as a static method Each answer is rounded to two decimal places, I might add functionality to change that later idk. 
        
        Parameters:

        leg1 (int or float): One of the right triangle's legs
        leg2 (int or float): The second right triangle leg
        hyp  (int or float): The longest side of the right triangle
        angle1 (int or float): The angle in degrees adjacent to leg1
        angle2 (int or float): The angle in degrees adjacent to leg2

        Note that all of the arguments are "optional" because any two or more of these arguments can be passed into the function
        and then the function calculates all the other parameters. Raises ValueError if less than two values are passed into the function
        If more than two arguments are passed in, the function will only look at the first two parameters and use those to recalculate
        the other parameters. 

        Returns:

        list: [leg1, leg2, hyp, angle1, 90 - angle1]
        
        90 - angle1 refers to angle2. 

        '''
        passed_args = locals()
        args = ["leg1", "leg2", "hyp", "angle1"]
        
        known_values = []
        for arg in args:
            if passed_args[arg]:
                known_values.append(arg)
        
        if "leg1" in known_values and "leg2" in known_values:
            # Calculating hyp using Pythagorean Theoram
            hyp = math.hypot(leg1, leg2)
            angle1 = math.degrees(math.atan(leg2 / leg1))

        elif "leg1" in known_values and "hyp" in known_values:
            # Calculating leg2 using Pythagorean Theorm
            leg2 = math.sqrt((hyp**2) - (leg1**2))
            angle1 = math.degrees(math.atan(leg2 / leg1))

        elif "leg1" in known_values and "angle1" in known_values:
            leg2 = leg1 * math.tan(math.radians(angle1))
            hyp = math.hypot(leg1, leg2)

        elif "leg2" in known_values and "hyp" in known_values:
            leg1 = math.sqrt((hyp**2) - (leg2**2))
            angle1 = math.degrees(math.atan(leg2 / leg1))

        elif "leg2" in known_values and "angle1" in known_values:
            leg1 = leg2 / math.tan(math.radians(angle1))
            hyp = math.hypot(leg1, leg2)
        
        elif "hyp" in known_values and "angle1" in known_values:
            leg1 = hyp * math.cos(math.radians(angle1))
            leg2 = leg1 * math.tan(math.radians(angle1))

        # Converts all attributes to floats and rounds them to equal # of decimal places
        attributes = [leg1, leg2, hyp, angle1]
        attributes = [round(float(i), 2) for i in attributes]
        leg1, leg2, hyp, angle1 = attributes

        return [leg1, leg2, hyp, angle1, 90 - angle1] # angle2
    
    def error_checking(self, l1=None, l2=None, hyp=None, angle1=None):
        '''
        Function is run at initialization

        Filters each argument passed in besides self to a list of values that are not None. This shows how many values were passed in,
        and which values were passed in. Each block of code below explains the specifc error that is being catched and for what reason. 
        '''

        known_values = list(filter(lambda x : x is not None, [l1, l2, hyp, angle1]))
        
        # If more than two arguments are passed in, the function makes all of their values None except for the first two values.
        # The other values are then recalculated by RightTriangle.solve()
        if len(known_values) < 2:
            raise ValueError("Provide at least two arguments")
      
        # Checks if legs are greater than 0
        if l1 <= 0 or l2 <= 0:
            raise(ValueError)("Legs must be greater than 0")

        # Checks if hyp is longest side of triangle
        if hyp in known_values and l1 in known_values and hyp <= l1:
            raise ValueError("Hypotenuse must be greater than leg1 and leg2")
        elif hyp in known_values and l2 in known_values and hyp <= l2:
            raise ValueError("Hypotenuse must be greater than leg1 and leg2")
        
        if hyp in known_values and hyp <= 0:
            raise ValueError("Hypotenuse must be greater than 0")
            
        # If angle1 is between 0 and 90 degrees
        if angle1 in known_values:
            if angle1 <= 0 or angle1 >= 90:
                raise ValueError("Angle must be between 0 and 90 degrees")
