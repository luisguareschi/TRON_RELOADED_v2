import pyxel

class Background:
    borders_vertical = [0, 0, 48, 16, 16]
    borders_horizontal = [0, 16, 48, 16, 16]
    xxx = 10
    yy = 66-31

    def draw(self):
        xb1 = 2
        yb1 = 35
        for i in range(0, 10):
            pyxel.rectb(xb1, yb1, 32, 32, col=1)
            xb1 += 32

        xb2 = 2
        yb2 = 35+31
        for i in range(0, 10):
            pyxel.rectb(xb2, yb2, 32, 32, col=1)
            xb2 += 32

        xb3 = 2
        yb3 = 35 + 31 + 31
        for i in range(0, 10):
            pyxel.rectb(xb3, yb3, 32, 32, col=1)
            xb3 += 32

        xb4 = 2
        yb4 = 35 + 31 + 31 + 31
        for i in range(0, 10):
            pyxel.rectb(xb4, yb4, 32, 32, col=1)
            xb4 += 32

        xb5 = 2
        yb5 = 35 + 31*4
        for i in range(0, 10):
            pyxel.rectb(xb5, yb5, 32, 32, col=1)
            xb5 += 32

        xb6 = 2
        yb6 = 35 + 31 * 5
        for i in range(0, 10):
            pyxel.rectb(xb6, yb6, 32, 32, col=1)
            xb6 += 32

        xb7 = 2
        yb7 = 35 + 31 * 6
        for i in range(0, 10):
            pyxel.rectb(xb7, yb7, 32, 32, col=1)
            xb7 += 32

        bcolor = 0
        pyxel.rect(0, 0, 256, 30, col=bcolor)
        pyxel.rect(0, 30, 8, 258, col=bcolor)
        pyxel.rect(248, 30, 8, 258, col=bcolor)
        pyxel.rect(0, 248, 256, 10, col=bcolor)

        x0 = 0
        y0 = 31
        for i in range(0, 14):
            pyxel.blt(x0, y0, *self.borders_vertical, colkey=False)
            if i < 12:
                y0 += 16
            else:
                y0 += 10

        x2 = 239
        y2 = 31
        for i in range(0, 14):
            pyxel.blt(x2, y2, *self.borders_vertical, colkey=False)
            if i < 12:
                y2 += 16
            else:
                y2 += 10

        x1 = 8
        y1 = 25
        for i in range(0, 15):
            pyxel.blt(x1, y1, *self.borders_horizontal, colkey=False)
            x1 += 16

        x3 = 8
        y3 = 240
        for i in range(0, 15):
            pyxel.blt(x3, y3, *self.borders_horizontal, colkey=False)
            x3 += 16

        pyxel.blt(95, 8, 0, 0, 64, 16*4, 16, colkey=False)





