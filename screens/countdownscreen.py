import datetime

class CountdownScreen():
    def __init__(self, resources, displayTimeMs, text_color):
        self.displayTimeMs = displayTimeMs
        self.resources = resources
        self.text_color = self.resources.graphics.Color(text_color[0],text_color[1], text_color[2])

    def draw(self):
        delta = datetime.datetime(2020, 9, 1) - datetime.datetime.now()
        my_text = str(delta.days) + " Days"
        self.resources.DrawText(self.resources.font, 1, 9, self.text_color, my_text)
        my_text = str(int(delta.seconds/3600)) + " Hours"
        self.resources.DrawText(self.resources.font, 1, 19, self.text_color, my_text)

        self.resources.DrawText(self.resources.font, 1, 29, self.text_color, "Until Launch")
        pos = self.resources.offscreen_canvas.width