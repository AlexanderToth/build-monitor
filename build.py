#!/usr/bin/env python
# Display a runtext with double-buffering.
from screens import *

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
        driver = DisplayDriver(graphics, self.matrix)
        inputText = self.args.text
        color = (0, 200, 50)
        driver.RunScreens([
            ClockScreen(driver, 40, position=(0, 10), text_color=color),
            MarqueeScreen(driver, 40, inputText, text_start_position=(driver.offscreen_canvas.width, 10), text_color=color),
            CountdownScreen(driver, 20, text_color=color)
        ])
    
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
