from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color and prompt user for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (black or white): ")

# Create the canvas from user input
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

while True:
    shape_type = input("Enter the shape to draw(rectangle or square) or type 'quit' to exit: ")
    # The code below forms the rectangle
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter the x value: "))
        rec_y = int(input("Enter the y value: "))
        rec_width = int(input("Enter the rectangle width: "))
        rec_height = int(input("Enter the rectangle height: "))
        red_rec = int(input("How much red? "))
        green_rec = int(input("How much green? "))
        blue_rec = int(input("How much blue? "))

        rectangle = Rectangle(rec_x, rec_y, rec_width, rec_height, (red_rec, green_rec, blue_rec))
        rectangle.draw(canvas)
    # The code below forms the square
    if shape_type.lower() == "square":
        squ_x = int(input("Enter the x value: "))
        squ_y = int(input("Enter the y value: "))
        squ_side = int(input("Enter the square side: "))
        red_squ = int(input("How much red? "))
        green_squ = int(input("How much green? "))
        blue_squ = int(input("How much blue? "))

        square = Square(squ_x, squ_y, squ_side, (red_squ, green_squ, blue_squ))
        square.draw(canvas)
    # This will break the while look
    if shape_type == 'quit':
        break

canvas.make("canvas_image.png")



# # Drawing the rectangle on the canvas
# rectangle1 = Rectangle(x=1, y=6, width=7, height=10, color=(100, 200, 125))
# rectangle1.draw(canvas)
# # Drawing the square on the canvas
# square1 = Square(x=3, y=8, side=10, color=(255, 0, 0))
# square1.draw(canvas)
# # Making and saving the image formed
# canvas.make('canvas_image.png')

