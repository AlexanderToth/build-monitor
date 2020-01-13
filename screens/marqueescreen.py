class MarqueeScreen():
    
    def __init__(self, driver, displayTimeMs, my_text, text_start_position, text_color):
        self.displayTimeMs = displayTimeMs
        self.my_text = my_text
        self.driver = driver
        self.pos = text_start_position[0]
        self.text_color = self.driver.graphics.Color(text_color[0],text_color[1], text_color[2])
        self.text_height = text_start_position[1]

    def draw(self):
        len = self.driver.DrawText(self.driver.bigfont, self.pos, self.text_height, self.text_color, self.my_text)
        self.pos -= 1
        if (self.pos + len < 0):
            self.pos = self.driver.offscreen_canvas.width