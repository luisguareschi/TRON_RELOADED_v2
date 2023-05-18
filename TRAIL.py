import pyxel
import CONSTANTS

class Trail:

    blue_trail = [0, 16, 32, 16, 16]
    red_trail = [0, 0, 32, 16, 16]
    record = False

    def __init__(self):
        self.px = 1000
        self.py = 1000
        self.t = 0
        self.color = 'none'

    def draw(self, bike):
        if self.record == False:
            self.px = bike.px
            self.py = bike.py
            self.record = True
        if bike.color == 'blue' and self.t > CONSTANTS.speed:
            pyxel.blt(self.px, self.py, *self.blue_trail, colkey=False)
            self.color = 'blue'
        elif bike.color == 'red' and self.t > CONSTANTS.speed:
            pyxel.blt(self.px, self.py, *self.red_trail, colkey=False)
            self.color = 'red'
        self.t += 1

    def collision(self, bike, reset):
        bx = bike.px+8
        by = bike.py+8
        tx = self.px+8
        ty = self.py+8
        if tx-(CONSTANTS.speed-1) <= bx <= tx+(CONSTANTS.speed-1) and ty-(CONSTANTS.speed-1) <= by <= ty+(CONSTANTS.speed-1) and bike.crash == True:
            bike.color = 'dead'
            reset = True
        return reset


