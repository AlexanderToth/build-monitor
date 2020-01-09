from rgbmatrix_emulator.canvas import Canvas
class RGBMatrix:
    def __init__(self, options):
        self.options = options

    def SwapOnVSync(self, canvas):
        return canvas

    def CreateFrameCanvas(self):
        return Canvas(self.options)