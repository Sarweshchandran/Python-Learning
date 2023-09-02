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

    def function(self):
        Area = self.calculateArea()
        Cube = self.calculateCube()
        print("Area of rectangle with length" , self.length ," cm" ," and width " , self.width ,"cm is:" , Area)
        print("Volume of rectangle with length", self.length, " cm", "width ", self.width ," cm and height " ,self.height, " cm is: ", Cube)

if __name__ == "__main__":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    O = Rectangle(length, width, height)
    O.function()

