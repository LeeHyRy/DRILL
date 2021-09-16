from pico2d import *
import math

def move_rect():
    x = 0
    y = 30
    while x < 790:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 15
        delay(0.01)
    while y < 590:
        clear_canvas()
        grass.draw(400, 30)
        character.draw_now(x, y)
        y += 15
        delay(0.01)
    while x > 10:
        clear_canvas()
        grass.draw(400, 30)
        character.draw_now(x, y)
        x -= 15
        delay(0.01)
    while y > 30:
        clear_canvas()
        grass.draw(400, 30)
        character.draw_now(x, y)
        y -= 15
        delay(0.01)

def move_circle():
    r = 0
    t = 0
    while t < 2*math.pi:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(math.sin(t)*200+400, -math.cos(t)*200+300)
        t += 0.1
        delay(0.01)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    move_rect()
    move_circle()

exitonclick()
close_canvas()

