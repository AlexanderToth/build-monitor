
class Font:
    textSize = 0
    def LoadFont(self, file):
        if("5x8.bdf" in file):
            self.textSize = 78
            self.width = 5
            self.height = 8
        elif("6x10.bdf" in file):
            self.textSize = 105
            self.width = 6
            self.height = 10
class Color:
    red = 1
    green = 1
    blue = 1
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def DrawText(canvas, font, x_pos, y_pos, text_color, text):
    position = (x_pos * canvas.virtual_width_scale, -((y_pos * (canvas.virtual_height_scale)) + font.height))
    physical_font_length = position[0] + (font.width * len(text))
    
    # Actual size box
    canvas.my_turtle.fillcolor('pink')
    canvas.my_turtle.begin_fill()
    box(canvas.my_turtle, (position[0],position[1]), (physical_font_length, position[1] + font.height))
    canvas.my_turtle.end_fill()

    # Text representation
    canvas.my_turtle.setpos(position[0], position[1])
    canvas.my_turtle.pencolor((text_color.red / 255,text_color.green / 255,text_color.blue / 255))
    canvas.my_turtle.write(text, font = ('consolas',font.textSize, 'normal'))

    return physical_font_length

# Source: https://stackoverflow.com/a/45520085
def box(turtle, lower_left, upper_right):
    position = turtle.position()
    isdown = turtle.isdown()

    if isdown:
        turtle.penup()
    turtle.goto(lower_left)
    turtle.pendown()
    turtle.goto(upper_right[0], lower_left[1])
    turtle.goto(upper_right)
    turtle.goto(lower_left[0], upper_right[1])
    turtle.goto(lower_left)

    turtle.penup()
    turtle.setposition(position)
    if isdown:
        turtle.pendown()