import turtle

def draw_elipse(some_turtle):
    for i in range(19):
        some_turtle.left(10)
        some_turtle.forward(30)
        for i in range(9):
            some_turtle.right(15)
            some_turtle.forward(1)
        some_turtle.right(60)
        some_turtle.forward(30)
        some_turtle.right(5)



def draw_flower():
    canvas = turtle.Screen()
    canvas.bgcolor("blue")

    poo = turtle.Turtle()
    poo.color("red")
    poo.shape("arrow")
    poo.left(90)
    #poo.forward(100)
    draw_elipse(poo)


    canvas.exitonclick()




draw_flower()