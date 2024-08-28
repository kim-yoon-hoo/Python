import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('skyblue')
t.hideturtle()
t.penup()
t.goto(-100,220)
t.pendown
t.color("blue")
t.write("로또번호 생성기",font=("Verdana",50,"bold"))


for i in range(-500,501,200):
    t.penup()
    t.goto(i,-10)
    t.pendown()
    t.pensize(3)
    t.color('red')
    t.begin_fill()
    t.circle(70,360)
    t.end_fill()
    t.penup()

t.penup()
t.goto(-570,40)
t.pendown
t.color("blue")
t.write("01",font=("Verdana",25,"bold"))


turtle.done()