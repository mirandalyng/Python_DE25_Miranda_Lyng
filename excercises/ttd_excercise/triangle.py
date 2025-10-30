
from numbers import Number
#Skeleton for the Triangle class 
class Triangle: 
    #x and y optional 
    def __init__(self, base, height):
        self.base = base
        self.height = height

    
    @property
    def base(self): 
        return self._base


    @base.setter
    def base(self,value): 
        if not isinstance(value, Number):
            raise TypeError("Must be a number")
        
        if value <= 0:
            raise ValueError("Base must be larger than 0")
        self._base = value



    @property
    def height(self): 
        return self._height

    @height.setter
    def height(self, value): 
        if not isinstance(value, Number):
            raise TypeError("Must be a number")
        if value <= 0:
            raise ValueError("Height must be larger than 0")
        if value == True or value == False:
            raise TypeError("Height must be a number")
    
        self._height = value


    @property
    def area(self): 
        return (self.base * self.height)/ 2

    

    # @property
    # def perimeter(self): 
    #     pass


    def __eq__(self, other): 
        pass

    def __lt__(self, other): 
        pass

    
    def __gt__(self, other): 
        pass


    def __repr__(self): 
        pass