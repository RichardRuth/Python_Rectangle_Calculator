#!/usr/bin/env python3

#COP2002.0M1 Programming Logic
#Module 13 Project 13-1 Rectange Calculator Program
#Submitted by Richard Ruth

# Program obtains rectangle height and width data from user, and 
# and calculates and displays duration of travel, as well as estimated date of arrival and time of arrival

# Rectangle class stores height and width attributes of rectangle user data, and provides methods
# that calculate perimeter and area of rectangle, and draws string representation of rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return (2 * self.height) + (2 * self.width)

    def printRectangle(self):
        edge_row = "* " * self.width
        center_row = "*" + '  '*(self.width - 2) + " *"
        rectangle_rows = [edge_row] + [center_row]*(self.height - 2) + [edge_row]
        print('\n'.join(rectangle_rows))

def main():

    # Main module obtains user data for rectangle and creates userRectangle object from Rectangle class
    # to display perimter, area, and string representation of user's rectangle

    print("\nRectangle Calculator\n")
    choice = "y"
    while choice.lower() == "y":
        height = int(input("Height:    "))
        width = int(input("Width:     "))
        userRectangle = Rectangle(height, width)
        print("Perimeter:", userRectangle.getPerimeter())
        print("Area:     ", userRectangle.getArea())
        userRectangle.printRectangle()
        print()
        choice = input("Continue? (y/n): ")
        print()

            
# If this module is the main module, call the main() function

if __name__ == "__main__":
     main()
