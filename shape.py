#Shape - parent class
class Shape():
    id = 0
    def __init__(self):
        Shape.id += 1
        self.shape_id = Shape.id

    def print(self):
        print(f"{self.shape_id}: {__class__.__name__}, perimeter: undefined, area: undefined")

    def perimeter(self):
        return None

    def area(self):
        return None

    def equals(self, other):
        return (self.__class__.__name__ == other.__class__.__name__)


#Circle class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return "{:.5f}".format(2 * (22/7) * self.radius)

    def area(self):
        return "{:.5f}".format((22/7) * pow(self.radius,2))

    def print(self):
        print(f"{self.shape_id}: {__class__.__name__}, perimeter: {self.perimeter()}, area: {self.area()}")

    def equals(self, other):
        return (self.__class__.__name__ == other.__class__.__name__ and self.radius == other.radius)



#Ellipse class
class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()

        if (a > b):
         self.major = a
         self.minor = b
        else:
         self.major = b
         self.minor = a

    def perimeter(self):
        return None

    def area(self):
        return "{:.5f}".format( (22/7) * self.major * self.minor ) # A = πab

    def eccentricity(self):
        try:
         c = pow( pow(self.major, 2) - pow(self.minor, 2), 0.5 )
         return "{:.5f}".format(c)
        except ArithmeticError:
         return None;

    def print(self):
        print(f"{self.shape_id}: {__class__.__name__}, perimeter: undefined, area:  {self.area()}, linear eccentricity: {self.eccentricity()}")

    def equals(self, other):
        return (self.__class__.__name__ == other.__class__.__name__ and self.minor == other.minor and self.major == other.major)


#Rhombus class
class Rhombus(Shape):
    def __init__(self, p, q):
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        return "{:.4f}".format( 2* pow(pow(self.p,2) + pow(self.q,2),0.5) )

    def area(self):
        return "{:.4f}".format( (self.p * self.q)/2 )

    def side(self):
        return "{:.4f}".format( pow(pow(self.p,2) + pow(self.q,2),0.5) / 2 )

    def inradius(self):
        try:
            r = self.p * self.q / (2 * pow(pow(self.p,2) + pow(self.q,2),0.5))
            return "{:.4f}".format(r)
        except ArithmeticError:
            return None

    def print(self):
        print(f"{self.shape_id}: {__class__.__name__}, perimeter: {self.perimeter()}, area: {self.area()}, in-radius: {self.inradius()}")

    def equals(self, other):
        return (self.__class__.__name__ == other.__class__.__name__ and self.p == other.p and self.q == other.q)


