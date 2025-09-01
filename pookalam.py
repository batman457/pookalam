import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")  # Background color

# Setup turtle
t = turtle.Turtle()
t.speed(0)

# --- Draw outer green circle ---
outer_green_radius = 282
t.color("green")
t.begin_fill()
t.penup()
t.goto(0, -outer_green_radius)
t.pendown()
t.circle(outer_green_radius)
t.end_fill()


# --- Draw outer white circle ---
outer_white_radius = 230
t.color("red")
t.begin_fill()
t.penup()
t.goto(0, -outer_white_radius)
t.pendown()
t.circle(outer_white_radius)
t.end_fill()

# --- Draw alternating red and white triangles around outer red circle ---
num_triangles = 40
base_angle = 360 / num_triangles
triangle_height = 42

# White triangles (shifted half step between red ones)
for i in range(num_triangles):
    angle = i * base_angle + base_angle / 2  # shift half step

    x1 = outer_white_radius * math.cos(math.radians(angle - base_angle/2))
    y1 = outer_white_radius * math.sin(math.radians(angle - base_angle/2))

    x2 = outer_white_radius * math.cos(math.radians(angle + base_angle/2))
    y2 = outer_white_radius * math.sin(math.radians(angle + base_angle/2))

    tip_x = (outer_white_radius + triangle_height) * math.cos(math.radians(angle))
    tip_y = (outer_white_radius + triangle_height) * math.sin(math.radians(angle))

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(tip_x, tip_y)
    t.goto(x1, y1)
    t.end_fill()


# --- Draw outer red circle ---
outer_red_radius = 240
t.color("red")
t.begin_fill()
t.penup()
t.goto(0, -outer_red_radius)
t.pendown()
t.circle(outer_red_radius)
t.end_fill()

# --- Draw outer yellow circle ---
outer_yellow_radius = 210
t.color("yellow")
t.begin_fill()
t.penup()
t.goto(0, -outer_yellow_radius)
t.pendown()
t.circle(outer_yellow_radius)
t.end_fill()

# --- Draw inner red circle ---
inner_radius = 160
t.color("green")
t.begin_fill()
t.penup()
t.goto(0, -inner_radius)
t.pendown()
t.circle(inner_radius)
t.end_fill()

# --- Draw inner white circle ---
inner_white_radius = 85
t.color("white")
t.begin_fill()
t.penup()
t.goto(0, -inner_white_radius)
t.pendown()
t.circle(inner_white_radius)
t.end_fill()

# --- Draw flower petals between yellow and white circles ---
num_petals = 25
mid_radius = (outer_yellow_radius + inner_radius) / 2
petal_radius = 8
dot_radius = 2
colors = ["darkblue", "black"]

for i in range(num_petals):
    angle = (360 / num_petals) * i
    x = mid_radius * math.cos(math.radians(angle))
    y = mid_radius * math.sin(math.radians(angle))

    # Petal
    t.penup()
    t.goto(x, y - petal_radius)
    t.pendown()
    t.color(colors[i % 2])
    t.begin_fill()
    t.circle(petal_radius)
    t.end_fill()

    # Dot
    t.penup()
    t.goto(x, y - dot_radius)
    t.pendown()
    t.color("lightgreen")
    t.begin_fill()
    t.circle(dot_radius)
    t.end_fill()

# --- Draw alternating red and white triangles around outer red circle ---
num_triangles = 40
base_angle = 360 / num_triangles
triangle_height = 42

# Red triangles
for i in range(num_triangles):
    angle = i * base_angle

    x1 = outer_red_radius * math.cos(math.radians(angle - base_angle/2))
    y1 = outer_red_radius * math.sin(math.radians(angle - base_angle/2))

    x2 = outer_red_radius * math.cos(math.radians(angle + base_angle/2))
    y2 = outer_red_radius * math.sin(math.radians(angle + base_angle/2))

    tip_x = (outer_red_radius + triangle_height) * math.cos(math.radians(angle))
    tip_y = (outer_red_radius + triangle_height) * math.sin(math.radians(angle))

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(tip_x, tip_y)
    t.goto(x1, y1)
    t.end_fill()



# --- Draw yellow triangles on yellow boundary ---
triangle_height_orange = 40
for i in range(num_triangles):
    angle = i * base_angle

    x1 = outer_yellow_radius * math.cos(math.radians(angle - base_angle/2))
    y1 = outer_yellow_radius * math.sin(math.radians(angle - base_angle/2))

    x2 = outer_yellow_radius * math.cos(math.radians(angle + base_angle/2))
    y2 = outer_yellow_radius * math.sin(math.radians(angle + base_angle/2))

    tip_x = (outer_yellow_radius + triangle_height_orange) * math.cos(math.radians(angle))
    tip_y = (outer_yellow_radius + triangle_height_orange) * math.sin(math.radians(angle))

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(tip_x, tip_y)
    t.goto(x1, y1)
    t.end_fill()

# green triangles between inner white and red circles
num_triangles = 7
base_angle = 360 / num_triangles

# --- Draw green triangles on white boundary ---
triangle_height_orange = 75
for i in range(num_triangles):
    angle = i * base_angle

    x1 = inner_white_radius * math.cos(math.radians(angle - base_angle/2))
    y1 = inner_white_radius * math.sin(math.radians(angle - base_angle/2))

    x2 = inner_white_radius * math.cos(math.radians(angle + base_angle/2))
    y2 = inner_white_radius * math.sin(math.radians(angle + base_angle/2))

    tip_x = (inner_white_radius + triangle_height_orange) * math.cos(math.radians(angle))
    tip_y = (inner_white_radius + triangle_height_orange) * math.sin(math.radians(angle))

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(tip_x, tip_y)
    t.goto(x1, y1)
    t.end_fill()

# --- Draw inner white circle ---
inner_white_radius = 85
t.color("yellow")
t.begin_fill()
t.penup()
t.goto(0, -inner_white_radius)
t.pendown()
t.circle(inner_white_radius)
t.end_fill()

# --- Draw Boat (lower hemisphere of an oval) ---
def draw_boat():
    t.penup()
    t.goto(-80, -5)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for angle in range(0, 181, 5):  # lower half of ellipse
        x = 80 * math.cos(math.radians(angle))
        y = -20 * math.sin(math.radians(angle)) - 5
        t.goto(x, y)
    t.goto(80, -5)
    t.goto(-80, -5)
    t.end_fill()

# --- Draw Man (circle head + triangular body) ---
def draw_man():
    # Head
    t.penup()
    t.goto(0, 15)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

    # Body (isosceles triangle)
    t.penup()
    t.goto(-12, -5)
    t.pendown()
    t.begin_fill()
    t.goto(12, -5)
    t.goto(0, 15)
    t.goto(-12, -5)
    t.end_fill()

# --- Draw Oar (rectangle + circle at tip) ---
def draw_oar():
    # Long rectangle
    t.penup()
    t.goto(5, 5)
    t.pendown()
    t.begin_fill()
    t.goto(50, -35)
    t.goto(54, -33)
    t.goto(9, 7)
    t.goto(5, 5)
    t.end_fill()

    # Circle at end of oar
    t.penup()
    t.goto(52, -45)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()

# Place objects in white circle
draw_boat()
draw_man()
draw_oar()

# Finish
t.hideturtle()
turtle.done()
