class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculateArea(self):
        Area = self.length * self.width
        return Area

    def calculateCube(self):
        Cube = self.length * self.width * self.height
        return Cube

    def perimeter(self):
        P = 2 * (self.length + self.width)
        return P

    def function(self):
        Area = self.calculateArea()
        Cube = self.calculateCube()
        P = self.perimeter()
        print("Area of rectangle with length" , self.length ," cm" ," and width " , self.width ,"cm is:" , Area)
        print("Volume of rectangle with length", self.length, " cm", "width ", self.width ," cm and height " ,self.height, " cm is: ", Cube)
        print("Perimeter of Rectangle is :" ,P)
if __name__ == "__main__":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    O = Rectangle(length, width, height)
    O.function()

