import turtle 
import random

screen = turtle.Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")

stars = turtle.Turtle()
ground = turtle.Turtle()
cloud = turtle.Turtle()
moon = turtle.Turtle()
moon_carve = turtle.Turtle()
tree = turtle.Turtle()

# adjust speed 
ground.speed(0)
cloud.speed(0)
moon.speed(0)
moon_carve.speed(0)
tree.speed(0)
stars.speed(0)

# don't show cursor / turtle 
ground.hideturtle()
cloud.hideturtle()
moon.hideturtle()
moon_carve.hideturtle()
tree.hideturtle()
stars.hideturtle()

# this section creates the stars 
'''
This function is the main, predominant star type that will be drawn in the turtle window. 
'''
def star_type1(): 
    stars.shape("circle")
    stars.shapesize(0.1,0.1)
    stars.color("white")

'''
This function is the second type of star that can be drawn. It is slighly larger and bluer than type 1. 
'''
def star_type2(): 
    stars.shape("circle")
    stars.shapesize(0.15, 0.15)
    stars.color("azure")

star_type_list = [star_type1, star_type1, star_type2] # star type 1 is listed twice, so it is more probable

for i in range(100): # draws stars 
    star_type_list[random.randint(0,2)]()
    stars.stamp()
    stars.penup()
    stars.goto(random.randint(-250,250), random.randint(-250,250))

# this section draws the ground 
ground.width(150)
ground.color("white")
ground.penup()
ground.right(90)
ground.forward(175)
ground.pendown()
ground.left(90)
ground.forward(250)
ground.back(500)

# this section draws the cloud 
cloud.width(50)
cloud.color("light gray")
cloud.penup()
cloud.left(90)
cloud.forward(150)
cloud.right(90)
cloud.pendown()
for i in range(4): 
    cloud.circle(random.randint(4,7))
    cloud.penup()
    cloud.forward(random.randint(30,35))
    cloud.pendown()

# this section draws the full moon 
moon.color("khaki")
moon.fillcolor("khaki")
moon.penup()
moon.back(150)
moon.left(90)
moon.forward(100)
moon.right(90)
moon.pendown()
moon.begin_fill()
moon.circle(30)
moon.end_fill()

# this section carves out a bit of the moon, so it resembles a crescent 
moon_carve.color("black")
moon_carve.fillcolor("black")
moon_carve.penup()
moon_carve.back(180)
moon_carve.left(90)
moon_carve.forward(100)
moon_carve.right(90)
moon_carve.pendown()
moon_carve.begin_fill()
moon_carve.circle(30)
moon_carve.end_fill()

# this section defines the variables and parameters to draw the tree
branch_width = 8
branch_length = 50
branch_ratio = 0.8 + (random.randint(0,1))/40

tree_color_list = ["brown", "rosy brown", "burlywood4", "tan4", "sienna"]

tree.penup()
tree.goto(0,-125)
tree.left(90)
tree.pendown()
tree.color(tree_color_list[random.randint(0,len(tree_color_list)-1)])

'''
This function uses function recursion to draw the tree. It has 2 parameters (and can be given 2 arguments).
'''
def fractal_tree(length, width):
    if length <= 10:
        return None
    
    else: 
        branch_angle = 20.0 + (random.randint(-1,0))
        tree.width(width)
        tree.forward(length)

        tree.left(branch_angle)
        fractal_tree(length * branch_ratio, width * branch_ratio)

        tree.right(2*branch_angle)
        fractal_tree(length * branch_ratio, width * branch_ratio)

        tree.left(branch_angle)
        tree.back(length)

fractal_tree(branch_length, branch_width)

turtle.done()