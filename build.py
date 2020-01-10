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
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../../fonts/5x8.bdf")
        bigfont = graphics.Font()
        bigfont.LoadFont("../../../../fonts/6x10.bdf")
        textColor = graphics.Color(0, 200, 50)
        pos = offscreen_canvas.width
        inputText = self.args.text
        startTime = time.localtime()
        dday = time.strptime("2020-09-01", "%Y-%m-%d")

        while True:
            offscreen_canvas.Clear()

            my_text = inputText

            currTime = time.localtime()
            diff = (time.mktime(currTime) - time.mktime(startTime))
            if diff % 100 < 40:
                my_text = time.strftime("%I:%M:%S %p", time.localtime())
                graphics.DrawText(offscreen_canvas, font, 0, 10, textColor, my_text)
                pos = offscreen_canvas.width
            elif diff % 100 < 80:
                len = graphics.DrawText(offscreen_canvas, bigfont, pos, 10, textColor, my_text)
                pos -= 1
                if (pos + len < 0):
                    pos = offscreen_canvas.width
            else:
                delta = datetime.datetime(2020, 9, 1) - datetime.datetime.now()
                my_text = str(delta.days) + " Days"
                graphics.DrawText(offscreen_canvas, font, 1, 9, textColor, my_text)
                my_text = str(delta.seconds/3600) + " Hours"
                graphics.DrawText(offscreen_canvas, font, 1, 19, textColor, my_text)

                graphics.DrawText(offscreen_canvas, font, 1, 29, textColor, "Until Launch")
                pos = offscreen_canvas.width


            time.sleep(0.5)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
