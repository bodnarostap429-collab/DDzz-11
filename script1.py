
print("дивитесь на черепаху")
print("          - - - - - - - - --            ")
print("         /                 )")
print("        /                  |")
print("       /                   | ")
print("      /____________________)")
import turtle

t = turtle.Turtle()
t.speed(3)

# панцир
t.circle(190)

# голова
t.penup()
t.goto(10, 100)
t.pendown()
t.circle(20)

# лапи
t.penup()
t.goto(-70, -50)
t.pendown()
t.circle(20)

t.penup()
t.goto(70, -50)
t.pendown()
t.circle(20)

t.penup()
t.goto(-70, 50)
t.pendown()
t.circle(20)

t.penup()
t.goto(70, 50)
t.pendown()
t.circle(40)

turtle.done()