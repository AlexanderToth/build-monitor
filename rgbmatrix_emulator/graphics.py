
class Font:
    textSize = 0
    px_height_offset = 0
    def LoadFont(self, file):
        if("5x8.bdf" in file):
            self.textSize = 12 * 8
            self.px_height_offset = 0
        elif("6x10.bdf" in file):
            self.textSize = 13 * 10
            self.px_height_offset = 3
class Color:
    red = 1
    green = 1
    blue = 1
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def DrawText(canvas, font, x_pos, y_pos, text_color, text):
    canvas.my_turtle.setpos(x_pos * canvas.actual_width_mod, -((y_pos * (canvas.actual_height_mod)) + font.px_height_offset))
    canvas.my_turtle.pencolor((text_color.red / 255,text_color.green / 255,text_color.blue / 255))
    start = canvas.my_turtle.position()
    canvas.my_turtle.write(text, font = ('consolas',font.textSize, 'normal'), move = True)
    end = canvas.my_turtle.position()
    return end[0] - start[0]

