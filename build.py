#!/usr/bin/env python
# Display a runtext with double-buffering.
import time
import datetime

if(__debug__):
    from rgbmatrix_emulator.simplebase import SampleBase
    from rgbmatrix_emulator import graphics
else:
    from samplebase import SampleBase
    from rgbmatrix import graphics

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        resources = displayResources(graphics, self.matrix.CreateFrameCanvas())
        pos = resources.offscreen_canvas.width
        inputText = self.args.text
        startTime = time.localtime()
        dday = time.strptime("2020-09-01", "%Y-%m-%d")
        

        screen_list = [
            ClockScreen(resources, 1),
            MarqueeScreen(resources,1, inputText),
            CountdownScreen(resources,1)
        ]
        

        currTime = time.localtime()
        diff = (time.mktime(currTime) - time.mktime(startTime))
        while True:
            for current_job in screen_list:
                job_start = time.time()
                job_end = job_start
                while ((job_end - job_start) <= current_job.displayTimeMs):
                    resources.offscreen_canvas.Clear()
                    current_job.draw()
                    time.sleep(0.5)
                    resources.offscreen_canvas = self.matrix.SwapOnVSync(resources.offscreen_canvas)
                    job_end = time.time()

class displayResources():
    def __init__(self, graphics, offscreen_canvas):
        self.graphics = graphics
        self.font = graphics.Font()
        self.font.LoadFont("../../../../fonts/5x8.bdf")
        self.bigfont = graphics.Font()
        self.bigfont.LoadFont("../../../../fonts/6x10.bdf")
        self.offscreen_canvas = offscreen_canvas
    def DrawText(self, font, x_pos, y_pos, text_color, text):
        return self.graphics.DrawText(self.offscreen_canvas, font, x_pos, y_pos, text_color, text)



class ClockScreen():
    def __init__(self, resources, displayTimeMs):
        self.displayTimeMs = displayTimeMs
        self.resources = resources

    def draw(self):
        my_text = time.strftime("%I:%M:%S %p", time.localtime())
        self.resources.DrawText(
            self.resources.font,
            0,
            10,
            self.resources.graphics.Color(0, 200, 50),
            my_text)


class MarqueeScreen():
    def __init__(self, resources, displayTimeMs, my_text):
        self.displayTimeMs = displayTimeMs
        self.my_text = my_text
        self.resources = resources
        self.pos = self.resources.offscreen_canvas.width
        self.textColor = graphics.Color(0, 200, 50)

    def draw(self):
        len = self.resources.DrawText(self.resources.bigfont, self.pos, 10, self.textColor, self.my_text)
        self.pos -= 1
        if (self.pos + len < 0):
            self.pos = offscreen_canvas.width

class CountdownScreen():
    def __init__(self, resources, displayTimeMs):
        self.displayTimeMs = displayTimeMs
        self.resources = resources
        self.textColor = graphics.Color(0, 200, 50)

    def draw(self):
        delta = datetime.datetime(2020, 9, 1) - datetime.datetime.now()
        my_text = str(delta.days) + " Days"
        self.resources.DrawText(self.resources.font, 1, 9, self.textColor, my_text)
        my_text = str(delta.seconds/3600) + " Hours"
        self.resources.DrawText(self.resources.font, 1, 19, self.textColor, my_text)

        self.resources.DrawText(self.resources.font, 1, 29, self.textColor, "Until Launch")
        pos = self.resources.offscreen_canvas.width


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
