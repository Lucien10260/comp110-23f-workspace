"""Drawing a simple car using the Turtle module."""
 
__author__ = "730521715"
 
from turtle import Turtle, colormode, done, tracer, update

def draw_car_body(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the body of the car."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("blue")
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(200)
        a_turtle.left(90)
        a_turtle.forward(50)
        a_turtle.left(90)
    a_turtle.end_fill()
    
def draw_wheel(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a wheel of the car."""
    a_turtle.penup()
    a_turtle.goto(x, y - radius)
    a_turtle.pendown()
    a_turtle.color("black")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()

def draw_window(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the windows of the car."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("black")
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(60)
        a_turtle.left(90)
        a_turtle.forward(30)
        a_turtle.left(90)
    a_turtle.end_fill()

def main() -> None:
    """The entrypoint of the car drawing scene."""
    tracer(0, 0)  # Disable delay in tracing
    car_turtle: Turtle = Turtle()
    
    draw_car_body(car_turtle, -100, 0)
    draw_wheel(car_turtle, -80, -50, 20)
    draw_wheel(car_turtle, 60, -50, 20)
    draw_window(car_turtle, -60, 20)
    draw_window(car_turtle, 10, 20)
    
    update()  # Now update the rendering
    done()

if __name__ == "__main__":
    main()