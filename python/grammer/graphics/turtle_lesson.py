import turtle

# さんかく
turtle.pencolor('green')
turtle.begin_fill()
for i in range(60):
    turtle.fd(50)
    turtle.left(360 / 3 + 10)
turtle.end_fill()

turtle.pencolor('red')
turtle.begin_fill()
for i in range(200):
    turtle.fd(50)
    turtle.left(360 / 3 + 10)
turtle.end_fill()
turtle.done()


# ほし
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# for i in range(5*3):
#     turtle.forward(100 + i * 10)
#     turtle.right(360 / 5 * 2)
# turtle.end_fill()
# turtle.done()

# しかく
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.end_fill()
# turtle.done()