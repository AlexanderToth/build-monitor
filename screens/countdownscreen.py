import datetime

class CountdownScreen():
    def __init__(self, driver, displayTimeMs, text_color):
        self.displayTimeMs = displayTimeMs
        self.driver = driver
        self.text_color = self.driver.graphics.Color(text_color[0],text_color[1], text_color[2])

    def draw(self):
        delta = datetime.datetime(2020, 9, 1) - datetime.datetime.now()
        my_text = str(delta.days) + " Days"
        self.driver.DrawText(self.driver.font, 1, 9, self.text_color, my_text)
        my_text = str(int(delta.seconds/3600)) + " Hours"
        self.driver.DrawText(self.driver.font, 1, 19, self.text_color, my_text)

        self.driver.DrawText(self.driver.font, 1, 29, self.text_color, "Until Launch")
        pos = self.driver.offscreen_canvas.width