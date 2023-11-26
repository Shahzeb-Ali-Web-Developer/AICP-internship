class Hexagon:
    def __init__(self, s):
        self.s = s

    def calArea(self):
        return 1.5 * 1.732 * self.s

    def calcPeri(self):
        return 6*self.s

    def calcAngleSum(self):
        return (6-2) * 180          # (n-2) * 180 degrees where n is count of side of polygon

    def display(self):
        print(f"Area of hexagon : {self.calArea()}")
        print(f"Perimeter of hexagon : {self.calcPeri()}")
        print(f"Angle Sum of hexagon : {self.calcAngleSum()}")

class Square:
    def __init__(self, s):
        self.s = s

    def calcArea(self):
        return self.s*self.s

    def calcPeri(self):
        return 4*self.s

    def display(self):
        print(f"Area of Square : {self.calcArea()}")
        print(f"Perimeter of Square : {self.calcPeri()}")


def main(s):

    obj_Hexagon = Hexagon(s)
    obj_Square = Square(s)

    i = int(input(f"Press 1 to display Area, Perimeter and Angle Sum of Hexagon\nPress 2 to display Area and Perimeter of Square\n"
                  f"Press any key to exit\n"))
    if i == 1:
        obj_Hexagon.display()
    elif i == 2:
        obj_Square.display()

main(2)