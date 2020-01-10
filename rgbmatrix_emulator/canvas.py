import turtle

class Canvas:
    my_turtle = turtle.Turtle()
    border_turtle = turtle.Turtle()
    def __init__(self, options):
        self.width = options.cols * options.chain_length
        self.height = options.rows
        self.virtual_square_size = max(self.width, self.height)

        self.virtual_width_scale = 1
        self.virtual_height_scale = 1

        self.virtual_width = self.width * self.virtual_width_scale
        self.virtual_height = self.height * self.virtual_height_scale

        
        self.border_turtle.getscreen().screensize(self.virtual_square_size, self.virtual_square_size)
        self.border_turtle.getscreen().setworldcoordinates(-1, -self.virtual_square_size, self.virtual_square_size + 1, 0)


        self.border_turtle._tracer(0, 0)

        # setup
        self.border_turtle.hideturtle()
        
        # border
        self.border_turtle.penup()
        self.border_turtle.setpos(0, 0)
        self.border_turtle.pendown()
        self.border_turtle.setpos(self.virtual_width, 0)
        self.border_turtle.setpos(0, 0)
        self.border_turtle.setpos(0, -self.virtual_height)
        self.border_turtle.setpos(0, 0)
        self.border_turtle.penup()

        # draw grid
        self.border_turtle.penup()
        for x in range(0, self.virtual_width, self.virtual_width_scale):
            for y in range(0,-self.virtual_height - 1, -self.virtual_height_scale):
                self.border_turtle.setpos(x,y)
                if(x % (10 * self.virtual_width_scale) == 0 or -y % (10 * self.virtual_height_scale) == 0):
                    self.border_turtle.dot(3, "red")
                else:
                    self.border_turtle.dot(3, "blue")

        self.border_turtle._update()

        self.my_turtle.hideturtle()
        self.my_turtle.penup()



    def Clear(self):
        self.my_turtle.clear()