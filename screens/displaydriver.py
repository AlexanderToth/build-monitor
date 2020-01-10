import time

class DisplayDriver():
    def __init__(self, graphics, matrix):
        self.graphics = graphics
        self.font = graphics.Font()
        self.font.LoadFont("../../../../fonts/5x8.bdf")
        self.bigfont = graphics.Font()
        self.bigfont.LoadFont("../../../../fonts/6x10.bdf")
        self.matrix = matrix
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
    
    def DrawText(self, font, x_pos, y_pos, text_color, text):
        return self.graphics.DrawText(self.offscreen_canvas, font, x_pos, y_pos, text_color, text)
    
    def ClearScreen(self):
        self.offscreen_canvas.Clear()
    
    def SwapOnVSync(self):
        self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)

    def RunScreens(self, screen_list):
        while True:
            for current_job in screen_list:
                job_start = time.time()
                job_end = job_start
                while ((job_end - job_start) <= current_job.displayTimeMs):
                    self.ClearScreen()
                    current_job.draw()
                    time.sleep(0.5)
                    self.SwapOnVSync()
                    job_end = time.time()