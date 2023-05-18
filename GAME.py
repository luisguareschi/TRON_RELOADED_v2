import pyxel
import winsound
import BIKE
import TRAIL
import CONSTANTS
import BACKGROUND


class Game:
    bluebike = BIKE.Bike(CONSTANTS.pxb, CONSTANTS.pyb, CONSTANTS.speed, CONSTANTS.directionb, CONSTANTS.colorb,
                         CONSTANTS.lives)
    redbike = BIKE.Bike(CONSTANTS.pxr, CONSTANTS.pyr, CONSTANTS.speed, CONSTANTS.directionr, CONSTANTS.colorr,
                        CONSTANTS.lives)
    background = BACKGROUND.Background()
    trails_b = []
    trails_r = []
    reset = False
    game_time = 0
    dead_time = 0
    state = 'intro'
    title_time = 0
    total_game_time = 0
    load_match_time = 0
    load_menu_time = 0

    # POSSIBLE STATES:
    # INTRO, GAME, OVER

    def __init__(self):
        pyxel.init(256, 256, caption='TRON')
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.play(0, 1, loop=False)
            pyxel.quit()

        if self.state == 'intro':
            if pyxel.btnp(pyxel.KEY_ENTER):
                pyxel.play(0, 1, loop=False)
                self.state = 'load_match'
            if self.title_time == 2:
                winsound.PlaySound('arena.wav', winsound.SND_ASYNC)
            self.title_time += 1

        if self.state == 'load_match':
            if self.load_match_time > 15:
                self.load_match_time = 0
                self.state = 'game'
            self.load_match_time += 1

        if self.state == 'load_menu':
            if self.load_menu_time > 15:
                self.load_menu_time = 0
                self.state = 'intro'
            self.load_menu_time += 1

        if self.state == 'game':
            if self.total_game_time == 2:
                winsound.PlaySound('title.wav', winsound.SND_ASYNC)
            if self.game_time > 90:
                # Move bikes and create the trail
                self.bluebike.move(self.bluebike)
                self.redbike.move(self.redbike)
                self.trails_r.append(TRAIL.Trail())
                self.trails_b.append(TRAIL.Trail())

                # Borders
                self.bluebike.boundaries()
                self.redbike.boundaries()

                # Collisions
                for trail in self.trails_b:
                    self.reset = trail.collision(self.redbike, self.reset)
                    self.reset = trail.collision(self.bluebike, self.reset)
                for trail in self.trails_r:
                    self.reset = trail.collision(self.redbike, self.reset)
                    self.reset = trail.collision(self.bluebike, self.reset)

                # Restart to initial position after collision
                self.reset = self.pos_init(self.bluebike, self.redbike, self.trails_b, self.trails_r, self.reset)

                # GAME OVER
                if (self.bluebike.lives == 0 or self.redbike.lives == 0) and self.dead_time == 35:
                    self.state = 'over'
            self.game_time += 1
            self.total_game_time += 1
        if self.state == 'over':
            self.total_game_time = 0
            self.title_time = 0
            winsound.PlaySound(None, winsound.SND_ASYNC)
            if pyxel.btnp(pyxel.KEY_ENTER):
                pyxel.play(0, 1, loop=False)
                self.state = 'load_menu'
                self.bluebike.lives, self.redbike.lives = 3, 3
            elif pyxel.btn(pyxel.KEY_Q):
                pyxel.play(0, 1, loop=False)
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        if self.state == 'intro':
            xi = 0
            for i in range(18):
                pyxel.line(xi, 0, xi, 80, col=1)
                pyxel.line(xi, 256 - 80, xi, 256, col=1)
                xi += 15
            yi = 0
            yii = 256 - 80
            for i in range(6):
                pyxel.line(0, yi, 256, yi, col=1)
                pyxel.line(0, yii, 256, yii, col=1)
                pyxel.line(0, 255, 256, 255, col=1)
                yi += 16
                yii += 16

            pyxel.text(50, 125 + 10, 'PRESS ENTER TO START', col=7)
            pyxel.text(50, 135 + 10, 'PRESS Q TO QUIT', col=7)
            pyxel.blt(95, 100, 0, 0, 64, 16 * 4, 16, colkey=False)

        if self.state == 'game':
            # Draw Background
            self.background.draw()

            # Draw bikes
            self.bluebike.draw(self.bluebike)
            self.redbike.draw(self.redbike)

            # Draw trails
            for trail in self.trails_b:
                trail.draw(self.bluebike)
            for trail in self.trails_r:
                trail.draw(self.redbike)

            # STATS
            pyxel.text(10, 15, 'PLAYER 1 LIVES: ' + str(self.bluebike.lives), 12)
            pyxel.text(180, 15, 'PLAYER 2 LIVES: ' + str(self.redbike.lives), 8)

            if self.game_time in range(0, 31):
                pyxel.text(40, 40, '3...', col=7)
                if self.game_time == 1:
                    pyxel.play(0, 2, loop=False)
            if self.game_time in range(31, 61):
                pyxel.text(40, 40, '2...', col=7)
                if self.game_time == 32:
                    pyxel.play(0, 2, loop=False)
            if self.game_time in range(61, 91):
                pyxel.text(40, 40, '1...', col=7)
                if self.game_time == 62:
                    pyxel.play(0, 2, loop=False)
            if self.game_time in range(91, 101):
                pyxel.text(40, 40, 'GO!', col=7)
                if self.game_time == 92:
                    pyxel.play(0, 3, loop=False)

            # MOUSE STATS
            # pyxel.text(30, 10, 'x ' + str(pyxel.mouse_x), 7)
            # pyxel.text(30, 20, 'y ' + str(pyxel.mouse_y), 7)
        if self.state == 'over':
            if self.bluebike.lives > self.redbike.lives:
                pyxel.text(110, 120, 'BLUE WINS!', col=1)
            else:
                pyxel.text(110, 120, 'RED WINS!', col=8)
            pyxel.text(70, 140, 'PRESS ENTER TO GO TO MAIN MENU', col=7)
            pyxel.text(70, 160, 'PRESS Q TO GO TO EXIT GAME', col=7)

    def pos_init(self, bike1, bike2, trails1, trails2, reset):
        if reset == True:
            self.dead_time += 1
            bike1.crash = False
            bike2.crash = False
            bike1.speed = 0
            bike2.speed = 0
        if self.dead_time == 1:
            if bike1.color == 'dead':
                bike1.lives -= 1
            elif bike2.color == 'dead':
                bike2.lives -= 1
        if reset == True and self.dead_time == 40:
            bike1.px = CONSTANTS.pxb
            bike1.py = CONSTANTS.pyb
            bike2.px = CONSTANTS.pxr
            bike2.py = CONSTANTS.pyr
            bike1.direction = 'down'
            bike2.direction = 'up'
            trails1.clear()
            trails2.clear()
            bike1.color = 'blue'
            bike2.color = 'red'
            bike1.speed = CONSTANTS.speed
            bike2.speed = CONSTANTS.speed
            bike1.crash = True
            bike2.crash = True
            self.dead_time = 0
            self.game_time = 0
            reset = False

        return reset


Game()
