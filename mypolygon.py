from tkinter import N
import turtle
import math

nora = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt((360/n))
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

circle(nora, 40)