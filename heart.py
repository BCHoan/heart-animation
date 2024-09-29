import turtle
import time

def draw_heart(t, size, color):
    t.begin_fill()
    t.color(color)
    t.left(140)
    t.forward(size)

    t.circle(-size // 2, 200)

    t.left(120)
    t.circle(-size // 2, 200)

    t.forward(size)
    t.end_fill()
    t.setheading(0)

def draw_hearts():
    turtle.bgcolor('lightpink')
    t = turtle.Turtle()
    t.speed(8)
    t.width(8)

    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#E793A2', '#DCB7BB', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors):
        t.penup()
        t.goto(0, -size // 2)
        t.pendown()
        draw_heart(t, size, color)

    t.hideturtle()

    # Chữ rơi từ trên xuống dưới
    message_turtle = turtle.Turtle()
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.color('red')

    # Vị trí bắt đầu ở trên cùng của màn hình
    start_y = 300
    x_position = 0
    
    # Dòng chữ rơi từ trên xuống
    for y in range(start_y, -301, -5):
        message_turtle.clear()  # Xóa dòng chữ trước đó
        message_turtle.goto(x_position, y)
        message_turtle.write("Anh yêu Em", align="center", font=("Arial", 40, "bold"))
        time.sleep(0)  

    turtle.done()

draw_hearts()
