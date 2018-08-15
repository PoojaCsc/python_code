import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    mithu = turtle.Turtle()
    mithu.shape("turtle")
    mithu.color("yellow")
    mithu.speed(2)

    for i in range(36):
        draw_square(mithu)
        mithu.right(10)

    window.exitonclick()




draw_art()