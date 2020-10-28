import turtle
import random
import math

# Distance function
def distance(x1, y1, x2, y2):
    """Returns the distance between two points.
    You may recognize the distance formula from algebra/geometry."""
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

# The next five functions are only called once, at the start of the game.
# They are used to set up the game environment.
# -----------------------------------------------------------------------

def setup_keys():
    """Sets up key bindings -- ties a function to a certain key,
    so that the function is called whenever the user presses a key."""
    wn.onkey(update, "Up")
    wn.listen()

def setup_turtle():
    """Sets up the turtle."""
    t.shape("turtle")
    t.speed(0)
    t.penup()

def setup_box():
    """Draws the box with opposite corners at (300, 300) and (-300, -300)"""
    corner = 300
    t.goto(-corner, -corner)
    t.pendown()
    for i in range(4):
        t.forward(corner * 2)
        t.left(90)
    t.penup()
    t.goto(0, 0)

def setup_shark():
    """Sets up the shark that is chasing the turtle."""
    shark.shape("triangle")
    shark.penup()
    shark.color("grey")
    shark.goto(random.randrange(-300, 300), random.randrange(-300, 300))

def setup():
    """Function to set up the game. Called once at the beginning of the program."""
    setup_keys()
    setup_turtle()
    setup_box()
    setup_shark()
    wn.bgcolor("#00ccff")
    t.color("green")

# -----------------------------------------------------------------------



# The next few functions are called every time the player presses a key.
# They update the state of the game.
# -----------------------------------------------------------------------

def move_shark():
    """Moves the shark to 'chase' the player.
    You do not have to change this function."""
    deltax = t.xcor() - shark.xcor()
    deltay = t.ycor() - shark.ycor()
    angle = math.atan(deltay/deltax)
    if deltax < 0:
        angle += math.pi
    shark.setheading(180 * angle / math.pi)
    shark.forward(15)

def check_alive():
    """Checks if the shark is too close to the turtle.
    It's checking if they are closer than 20 pixels apart."""

def check_bounds():
    """This function checks if the turtle is out of bounds.
    Right now it is incomplete."""

def update():
    move_shark()
    check_alive()
    check_bounds()
    t.forward(10)

# Here is the main code:
# -----------------------------------------------------------------------

score = 0
wn = turtle.Screen()
t = turtle.Turtle()
shark = turtle.Turtle()
setup()
wn.exitonclick()