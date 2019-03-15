#Höfundur: Huginn Þór Jóhannsson
#2. Hluti: tkinter
from tkinter import *
from random import randint
import time
WIDTH=800
HEIGHT=640
tk=Tk()
canvas=Canvas(width=WIDTH,height=HEIGHT)
tk.title("Kassar og shit")
class Shape():
    def __init__(self,pos1,pos2):
        self.pos1=pos1
        self.pos2=pos2
    def move(self):
        canvas.move(self,4,5)
    def returnParameters(self):
        return [pos1,pos2]
class Square(Shape):
    def __init__(self,pos1,pos2):
        Shape.__init__(self,pos1,pos2)
        canvas.create_rectangle(pos1[0],pos1[1],pos2[0],pos2[1],fill="blue")
class Circle(Shape):
    def __init__(self,pos1,pos2):
        Shape.__init__(self,pos1,pos2)
        canvas.create_oval(pos1[0],pos1[1],pos2[0],pos2[1],fill="red")
class Triangle(Shape):
    def __init__(self,pos1,pos2):
        Shape.__init__(self,pos1,pos2)
        canvas.create_polygon(pos1[0],pos1[1],pos2[0],pos2[1],randint(0,80),randint(0,64),fill="Green")
        Shape.move(self)
def shapeGenerator(objects):
    for x in range(0,99):
        pos1x=randint(0,80)
        pos1y=randint(0,64)
        pos2x=randint(0,80)
        pos2y=randint(0,64)
        typeOf=randint(0,2)
        if typeOf == 0:
            objects.append(Square([pos1x,pos1y],[pos2x,pos2y]))
        elif typeOf == 1:
            objects.append(Circle([pos1x,pos1y],[pos2x,pos2y]))
        elif typeOf== 2:
            objects.append(Triangle([pos1x,pos1y],[pos2x,pos2y]))
objects=[]
shapeGenerator(objects)
#ob1=Square([100,200],[400,500])


canvas.pack()
tk.mainloop()
