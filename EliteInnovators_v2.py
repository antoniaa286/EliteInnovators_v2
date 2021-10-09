import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.speed(0)
t.pu()
t.goto(0,400)
t.pd()
t.color("black")
t.right(90)
t.forward(800)
t.pu()
def rectangle(t, c, x,y,l,k):
    t.pu()
    t.color(c)
    t.goto(x,y)
    t.pd()
    for i in range(2):
        t.forward(k)
        t.left(90)
        t.forward(l)
        t.left(90)
    t.pu()

t.begin_fill()
rectangle(t, "grey", -500, 200, 400, 900)
t.end_fill()
t.begin_fill()
rectangle(t, "black", -230, 100, 60, 90)
t.end_fill()
t.begin_fill()
rectangle(t, "yellow", -450, 100, 60, 90)
t.end_fill()
t.begin_fill()
rectangle(t, "black", -230, -100, 60, 90)
t.end_fill()
t.begin_fill()
rectangle(t, "black", -230, -300, 60, 90)
t.end_fill()
t.begin_fill()
rectangle(t, "black", -450, -100, 60, 90)
t.end_fill()
t.begin_fill()
rectangle(t, "yellow", -450, -300, 60, 90)
t.end_fill()
t.pu()
def messages(t, r, angle, color):
  t.color(color)
  t.pendown()
  for i in range(2):
    t.circle(r,angle)
    t.left(180-angle)
  t.penup()
t.goto(-700, 300)
messages(t, 120, 155,"pink")
s=5
p=5
t.goto(-450,100)
t.right(135)
for i in range(6):
    t.pendown()
    t.dot(s)
    s=s+5
    t.penup()
    t.forward(p)
    p=p+10

    
def circle(t, color, size, x, y):
  t.penup()
  t.color(color)
  t.fillcolor(color)
  t.goto(x,y)
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  t.pendown()
    
circle(t ,"green",70, 425, 50)
circle(t ,"light green",50, 550, -20)
circle(t ,"green",30, 120, -20)
circle(t ,"green",50, 125, 150)
circle(t ,"light green",40, 240, 130)
circle(t ,"green",50, 515, 150)
circle(t ,"light green",50, 275, 0)






    


