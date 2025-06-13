import random
import colorgram
import turtle as turtle_module


rgb_colors = []
colors = colorgram.extract('test.png', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.setheading(255)
tim.forward(300)
tim.dot(20,random.choice(rgb_colors))

screen = turtle_module.Screen()
screen.exitonclick()
