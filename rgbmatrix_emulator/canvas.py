import turtle

class Canvas:
    my_turtle = turtle.Turtle()
    border_turtle = turtle.Turtle()
    def __init__(self, options):
        self.width = options.cols * options.chain_length
        self.height = options.rows
        self.squareSize = max(self.width,self.height)
        print(self.squareSize)
        self.actual_width_mod = 1
        self.actual_height_mod = 1

        self.actual_width = self.width * self.actual_width_mod
        self.actual_height = self.height * self.actual_height_mod

        self.border_turtle.getscreen().screensize(self.squareSize, self.squareSize)
        self.border_turtle.getscreen().setworldcoordinates(0,-self.squareSize, self.squareSize, 0)


        self.border_turtle._tracer(0, 0)

        # setup
        self.border_turtle.hideturtle()
        
        # border
        self.border_turtle.penup()
        self.border_turtle.setpos(0, 0)
        self.border_turtle.pendown()
        self.border_turtle.setpos(self.actual_width, 0)
        self.border_turtle.setpos(0, 0)
        self.border_turtle.setpos(0, -self.actual_height)
        self.border_turtle.setpos(0, 0)
        self.border_turtle.penup()

        # draw grid
        self.border_turtle.penup()
        for x in range(0, self.actual_width + 1, self.actual_width_mod):
            for y in range(0,-self.actual_height - 1, -self.actual_height_mod):
                self.border_turtle.setpos(x,y)
                if(x % (10 * self.actual_width_mod) == 0 or -y % (10 * self.actual_height_mod) == 0):
                    self.border_turtle.dot(3, "red")
                else:
                    self.border_turtle.dot(3, "blue")

        self.border_turtle._update()

        self.my_turtle.hideturtle()
        self.my_turtle.penup()



    def Clear(self):
        self.my_turtle.clear()