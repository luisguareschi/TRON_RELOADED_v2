import pyxel
import CONSTANTS


class Bike:
    blue_up = [0, 16, 0, 16, 16]
    blue_down = [0, 16, 0, 16, -16]
    blue_right = [0, 16, 16, 16, 16]
    blue_left = [0, 16, 16, -16, 16]
    blue = {'right': blue_right, 'left': blue_left, 'down': blue_down, 'up': blue_up}

    red_up = [0, 0, 0, 16, 16]
    red_down = [0, 0, 0, 16, -16]
    red_right = [0, 0, 16, 16, 16]
    red_left = [0, 0, 16, -16, 16]
    red = {'right': red_right, 'left': red_left, 'down': red_down, 'up': red_up}

    def __init__(self, px, py, speed, direction, color, lives):
        self.px = px
        self.py = py
        self.speed = speed
        self.direction = direction
        self.color = color
        self.crash = True
        self.lives = lives
        self.crash_snd = True

    def draw(self, bike):
        if bike.color == 'blue':
            pyxel.blt(self.px, self.py, *self.blue[bike.direction], colkey=False)
            self.crash_snd = True

        elif bike.color == 'red':
            pyxel.blt(self.px, self.py, *self.red[bike.direction], colkey=False)
            self.crash_snd = True

        elif bike.color == 'dead':
            if self.crash_snd == True:
                pyxel.play(0, 0, loop=False)
                self.crash_snd = False
            pyxel.blt(self.px, self.py, 0, 32, 0, 16, 16, colkey=False)

    def move(self, bike):
        if bike.color == 'blue':
            if pyxel.btnp(pyxel.KEY_D) and bike.direction != 'left':
                bike.direction = 'right'
            elif pyxel.btnp(pyxel.KEY_A) and bike.direction != 'right':
                bike.direction = 'left'
            elif pyxel.btnp(pyxel.KEY_S) and bike.direction != 'up':
                bike.direction = 'down'
            elif pyxel.btnp(pyxel.KEY_W) and bike.direction != 'down':
                bike.direction = 'up'

            if pyxel.btnp(pyxel.KEY_D) and bike.direction == 'right':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_D) and bike.direction == 'right':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_A) and bike.direction == 'left':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_A) and bike.direction == 'left':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_W) and bike.direction == 'up':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_W) and bike.direction == 'up':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_S) and bike.direction == 'down':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_S) and bike.direction == 'down':
                bike.speed = CONSTANTS.speed


        elif bike.color == 'red':
            if pyxel.btnp(pyxel.KEY_RIGHT) and bike.direction != 'left':
                bike.direction = 'right'
            elif pyxel.btnp(pyxel.KEY_LEFT) and bike.direction != 'right':
                bike.direction = 'left'
            elif pyxel.btnp(pyxel.KEY_DOWN) and bike.direction != 'up':
                bike.direction = 'down'
            elif pyxel.btnp(pyxel.KEY_UP) and bike.direction != 'down':
                bike.direction = 'up'

            if pyxel.btnp(pyxel.KEY_RIGHT) and bike.direction == 'right':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_RIGHT) and bike.direction == 'right':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_LEFT) and bike.direction == 'left':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_LEFT) and bike.direction == 'left':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_UP) and bike.direction == 'up':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_UP) and bike.direction == 'up':
                bike.speed = CONSTANTS.speed
            if pyxel.btnp(pyxel.KEY_DOWN) and bike.direction == 'down':
                bike.speed = 3
            if pyxel.btnr(pyxel.KEY_DOWN) and bike.direction == 'down':
                bike.speed = CONSTANTS.speed

        elif bike.color == 'dead':
            bike.direction = 'none'

        if bike.direction == 'right':
            bike.px += bike.speed
        if bike.direction == 'left':
            bike.px -= bike.speed
        if bike.direction == 'down':
            bike.py += bike.speed
        if bike.direction == 'up':
            bike.py -= bike.speed
        if bike.direction == 'none':
            bike.px = bike.px
            bike.py = bike.py

    def boundaries(self):
        if self.px < 0:
            self.px = 0
        elif self.px + 16 > 253:
            self.px = 253 - 16
        if self.py < 25:
            self.py = 25
        elif self.py + 16 > 256:
            self.py = 255 - 16
