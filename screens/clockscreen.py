import time

class ClockScreen():
    def __init__(self, resources, displayTimeMs, position, text_color):
        self.displayTimeMs = displayTimeMs
        self.resources = resources
        self.position = position
        self.text_color = self.resources.graphics.Color(text_color[0],text_color[1], text_color[2])

    def draw(self):
        my_text = time.strftime("%I:%M:%S %p", time.localtime())
        self.resources.DrawText(
            self.resources.font,
            self.position[0],
            self.position[1],
            self.text_color,
            my_text)