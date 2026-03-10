from timeit import repeat

print("не зважайте на цей проект, він просто існує")
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
t.circle(100)

# голова
t.penup()
t.goto(0, 100)
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
t.circle(20)

turtle.done()