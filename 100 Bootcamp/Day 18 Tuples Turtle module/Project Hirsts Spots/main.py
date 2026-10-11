import colorgram
import turtle as turtle_module
import random

colors = colorgram.extract('image.jpeg', 30)

rgb_colors = []

#To też jest element klasy
for x in colors: # x to obiekt Color
    #print(x.rgb) # to obiekt klasy RGB (klasa z atrybutami r, g, b)
    red = x.rgb.r # atrybut: wartość RED (0-255)
    green = x.rgb.g # atrybut: wartość GREEN (0-255)
    blue = x.rgb.b # atrybut: wartość BLUE (0-255)
    rgb_colors.append((red,green,blue))


print(rgb_colors)
print(colors[0])
#print(colors)

#color_list = [ (243, 250, 246), (250, 244, 248), (240, 245, 250), (234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53)]


"""
Color (obiekt z extract)
└── rgb (atrybut, to obiekt RGB)
    ├── r (atrybut RGB: 255)
    ├── g (atrybut RGB: 128)
    └── b (atrybut RGB: 64)"""


obraz = turtle_module.Turtle() #tworzenie obiektu
obraz.penup()
obraz.hideturtle()
obraz.setheading(225)
obraz.forward(300)
obraz.setheading(0)
obraz.speed("fastest")

number_of_dots = 180

for dot_count in range(1, number_of_dots+1):
        
    random_color = random.choice(rgb_colors)
    r=random_color[0] / 255
    g=random_color[1] /255
    b=random_color[2] / 255

    obraz.dot(30, (r,g,b))
    obraz.forward(50)

    if dot_count % 10 == 0:
        obraz.setheading(90)
        obraz.forward(50)
        obraz.setheading(180)
        obraz.forward(500)
        obraz.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
