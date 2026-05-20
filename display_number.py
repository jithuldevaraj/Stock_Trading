import turtle
import Stock_functions

# Set up the screen
ins_screen = turtle.Screen()
ins_screen.bgcolor("lightblue")
ins_screen.setup(width=800, height=500)

# Create a turtle to write the text
obj_turt_writer = turtle.Turtle()
obj_turt_writer.hideturtle()  # Hide the turtle arrow
obj_turt_writer.penup()  # Don't draw lines while moving


def update_number():
    """Fetches a new number, updates the screen, and schedules the next update."""
    # 1. Get the newly generated random number
    number = Stock_functions.get_random_number()

    # 2. Clear the previous number from the screen
    obj_turt_writer.clear()

    # 3. Go to center and write the new number
    obj_turt_writer.goto(0, 0)
    obj_turt_writer.write(f"Number: {number}", align="center", font=("Arial", 24, "bold"))

    # 4. Schedule this function to run again after 1000 ms (1 second)
    ins_screen.ontimer(update_number, 1000)


# Start the continuous updating loop
update_number()

# Keep the window open and running
ins_screen.mainloop()