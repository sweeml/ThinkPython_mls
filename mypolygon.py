import turtle
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

polygon(nora, 200, 5)