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
    def move(self):
        canvas.move(self.item,self.speedX,self.speedY)
        pos=canvas.coords(self.item)
        if pos[3] >= HEIGHT or pos[1]<=0:
            self.speedY=-self.speedY
        elif pos[2] >= WIDTH or pos[0]<=0:
            self.speedX=-self.speedX
class Square(Shape):
    def __init__(self,speedX,speedY):
        self.speedX=speedX
        self.speedY=speedY
        self.item=canvas.create_rectangle(10,10,100,100,fill="red")
class Circle(Shape):
    def __init__(self,speedX,speedY):
        self.speedX=speedX
        self.speedY=speedY
        self.item=canvas.create_oval(30,30,10,10,fill="pink")
class Triangle(Shape):
    def __init__(self,speedX,speedY):
        self.speedX=speedX
        self.speedY=speedY
        self.item=canvas.create_polygon(10,50,30,30,60,60,fill="green")

canvas.pack()

items=[]
for i in range(100):
    typeOf=randint(0,2)
    if typeOf==0:
        items.append(Square(randint(1,10),randint(1,10)))
    elif typeOf==1:
        items.append(Circle(randint(1,10),randint(1,10)))
    elif typeOf==2:
        items.append(Triangle(randint(1,10),randint(1,10)))

while True:
    for x in items:
        x.move()
    tk.update()
    time.sleep(0.03)

tk.mainloop()
