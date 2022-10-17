from abc import ABC,abstractmethod
import numpy as np
import turtle as t
from time import sleep as s
import math

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def draw(self):
        pass

class Triangle(Polygon):
    def __init__(self,edge):
        self.__edge=edge
    def perimeter(self):
        return self.__edge*3
    def area(self):
        return ((self.__edge/(2*np.tan(np.radians(180/3))))*self.perimeter())/2
    def getEdge(self):
        return self.__edge
    def __add__(self, tri):
        return Triangle(self.__edge + tri.getEdge())

    def draw(self):
        for i in range(3):
            t.forward(self.__edge*10)
            t.right(int(360/3))
        s(5)

class Quadrilateral(Polygon):
    def __init__(self, edge):
        self.__edge=edge
    def area(self):
        return ((self.__edge/(2*np.tan(np.radians(180/4))))*self.perimeter())/2
    def perimeter(self):
        return 4*self.__edge
    def draw(self):
        for i in range(4):
            t.forward(self.__edge*10)
            t.right(int(360/4))
        s(5)

class Rect(Polygon):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
    def area(self):
        return self.__width*self.__height
    def perimeter(self):
        return 2*(self.__width+self.__height)
    def draw(self):
        for i in range(2):
            t.forward(self.__width*10)
            t.right(int(360/4))
            t.forward(self.__height*10)
            t.right(360/4)
        s(5)

class Pentagon(Polygon):
    def __init__(self,edge):
        self.__edge=edge
    def area(self):
        return ((self.__edge/(2*np.tan(np.radians(180/5))))*self.perimeter())/2
    def perimeter(self):
        return self.__edge*5
    def draw(self):
        for i in range(5):
            t.forward(self.__edge*10)
            t.right(int(360/5))
        s(5)

class Hexagon(Polygon):
    def __init__(self,edge):
        self.__edge=edge
    def area(self):
        return ((self.__edge/(2*np.tan(np.radians(180/6))))*self.perimeter())/2
    def perimeter(self):
        return self.__edge*6
    def draw(self):
        for i in range(6):
            t.forward(self.__edge*10)
            t.right(int(360/6))
        s(5)

class Octagon(Polygon):
    def __init__(self,edge):
        self.__edge=edge
    def area(self):
        return ((self.__edge/(2*np.tan(np.radians(180/8))))*self.perimeter())/2
    def perimeter(self):
        return self.__edge*8
    def draw(self):
        for i in range(8):
            t.forward(self.__edge*10)
            t.right(int(360/8))
        s(5)


class IsoscelesTriangle(Polygon):
    def __init__(self,base,height):
        self.__height=height
        self.__base=base
        self.__edge=math.sqrt((pow((1/2)*self.__base,2)+pow(self.__height,2)))

   
    def area(self):
        return((1/2)*self.__base*self.__height)

    def perimeter(self):
        return (self.__base+2*self.__edge)
    def draw(self):
        degree=int(math.degrees(math.atan(self.__height/((1/2)*self.__base))))
        t.forward(self.__base*10)
        t.left(180-degree)
        t.forward(self.__edge*10)
        t.left(2*degree)
        t.forward(self.__edge*10)
        t.left(180-degree)
        s(5)

ip = input("Please type a Polygon from:\n 1-Triangle\n 2-Quadrilateral\n 3-Rectangle\n 4-Pentagon\n 5-Hexagon\n 6-Octagon\n 7-Isoscelestriangle\n Please note that some attribute are needed to be given after choosing which shape and function needed to be applied, thank you\n ")
fun = input("Type a function to apply from:\n 1-Calculate area\n 2-Calculate permiter\n 3-Draw shape\n ")
if(ip.upper() == "TRIANGLE" or ip == "1"):
    edge_tri = int(input("please enter an edge for the Triangle "))
    triangleobj = Triangle(edge_tri)
    if(fun.upper() == "CALCULATE AREA" or fun=="1"):
        print(triangleobj.area())
    elif(fun.upper() == "Calculate permiter" or fun=="2"):
        print(triangleobj.perimeter())
    elif(fun.upper() == "DRAW SHAPE" or fun=="3"):
        triangleobj.draw()
if(ip.upper() == "Quadrilateral" or ip == "2"):
    edge_quad = int(input("please enter an edge for the Quadrilateral "))
    Quadrilateralobj = Quadrilateral(edge_quad)
    if(fun.upper()== "CALCULATE AREA" or fun == "1"):
        print(Quadrilateralobj.area())
    elif(fun.upper()== "CALCULATE PERIMETER" or fun == "2"):
        print(Quadrilateralobj.perimeter())
    elif (fun.upper()== "DRAW SHAPE" or fun == "3"):
        Quadrilateralobj.draw()
if(ip.upper()== "RECTANGLE" or ip == "3"):
    width_rect = int(input("please enter the wdith for the rectangle "))
    height_rect = int(input("please enter the height for the rectangle "))
    Rectangleobj = Rect(width_rect , height_rect)
    if(fun.upper()== "CALCULATE AREA" or fun == "1"):
        print(Rectangleobj.area())
    elif(fun.upper()== "CALCULATE PERIMETER" or fun == "2"):
        print(Rectangleobj.perimeter()) 
    elif (fun.upper()== "DRAW SHAPE" or fun == "3"):
        Rectangleobj.draw()
if(ip.upper()== "PENTAGON" or ip == "4"):
    edge_pentagon = int(input("please enter an edge for the pentagon "))
    Pentagonobj = Pentagon(edge_pentagon)
    if(fun.upper()== "CALCULATE AREA" or fun == "1"):
        print(Pentagonobj.area())
    elif(fun.upper()== "CALCULATE PERIMETER" or fun == "2"):
        print(Pentagonobj.perimeter())
    elif(fun.upper()== "DRAW SHAPE" or fun == "3"):
        Pentagonobj.draw()
if(ip.upper() == "HEXAGON" or ip == "5"):
    edge_hexagon = int(input("please enter an edge for the pentagon "))
    Hexagonobj = Hexagon(edge_hexagon)
    if(fun.upper() == "CALCULATE AREA" or fun == "1"):
        print(Hexagonobj.area())
    elif(fun.upper() == "CALCULATE PERIMETER" or fun == "2"):
        print(Hexagonobj.perimeter())
    elif(fun.upper() == "DRAW SHAPE" or fun == "3"):
        Hexagonobj.draw()
if(ip.upper() == "OCTAGON" or ip == "6"):
    edge_octagon  = int(input("please enter an ende for the octagon "))
    Octagonobj= Octagon(edge_octagon)
    if(fun.upper() == "CALCULATE AREA" or fun =="1"):
        print(Octagonobj.area())
    elif(fun.upper()== "CALCULATE PERIMETER" or fun == "2"):
        print(Octagonobj.perimeter())
    elif (fun.upper() == "DRAW SHAPE" or fun == "3"):
        Octagonobj.draw()
if(ip.upper() == "ISOSCELESTRIANGLE" or ip =="7"):
    base_isoscelestriangle = int(input("please enter the base for the isoscelestriangle "))
    height_isoscelestriangle = int(input("please enter the height for the isoscelestriangle "))
    IsoscelesTriangleobj = IsoscelesTriangle(base_isoscelestriangle , height_isoscelestriangle)
    if(fun.upper() == "CALCULATE AREA" or fun =="1"):
        print(IsoscelesTriangleobj.area())
    elif(fun.upper() == "CALCULATE PERIMETER" or fun =="2"):
        print(IsoscelesTriangleobj.perimeter())
    elif(fun.upper() == "DRAW SHAPE" or fun == "3"):
        IsoscelesTriangleobj.draw()