import time

class ClockScreen():
    def __init__(self, driver, displayTimeMs, position, text_color):
        self.displayTimeMs = displayTimeMs
        self.driver = driver
        self.position = position
        self.text_color = self.driver.graphics.Color(text_color[0],text_color[1], text_color[2])

    def draw(self):
        my_text = time.strftime("%I:%M:%S %p", time.localtime())
        self.driver.DrawText(
            self.driver.font,
            self.position[0],
            self.position[1],
            self.text_color,
            my_text)