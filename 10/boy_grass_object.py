from pico2d import *
import random


# Game object class here
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(3, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 60:
            self.y -= self.speed
        elif self.y < 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(3, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 60:
            self.y -= self.speed
        elif self.y < 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
ball1 = Ball()
ball2 = Ball()
ball3 = Ball()
ball4 = Ball()
ball5 = Ball()
ball6 = Ball()
ball7 = Ball()
ball8 = Ball()
ball9 = Ball()
ball0 = Ball()
bigball1 = BigBall()
bigball2 = BigBall()
bigball3 = BigBall()
bigball4 = BigBall()
bigball5 = BigBall()
bigball6 = BigBall()
bigball7 = BigBall()
bigball8 = BigBall()
bigball9 = BigBall()
bigball0 = BigBall()

grass = Grass()

running = True

# game main loop code



while running:
    handle_events()
    ball1.update()
    ball2.update()
    ball3.update()
    ball4.update()
    ball5.update()
    ball6.update()
    ball7.update()
    ball8.update()
    ball9.update()
    ball0.update()
    bigball1.update()
    bigball2.update()
    bigball3.update()
    bigball4.update()
    bigball5.update()
    bigball6.update()
    bigball7.update()
    bigball8.update()
    bigball9.update()
    bigball0.update()
    clear_canvas()
    grass.draw()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()
    ball6.draw()
    ball7.draw()
    ball8.draw()
    ball9.draw()
    ball0.draw()
    bigball1.draw()
    bigball2.draw()
    bigball3.draw()
    bigball4.draw()
    bigball5.draw()
    bigball6.draw()
    bigball7.draw()
    bigball8.draw()
    bigball9.draw()
    bigball0.draw()
    update_canvas()
    delay(0.05)

# finalization code

close_canvas()
