from pico2d import *
import random

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
cursor = load_image('hand_arrow.png')

x = 0
y = 0
cursor_x = random.randrange(0, 800)
cursor_y = random.randrange(0, 600)
frame = 0
while 1:
    clear_canvas()
    grass.draw(400, 30)
    cursor.draw(cursor_x, cursor_y)
    # x위치, y위치, 가로폭, 세로폭, 출력위치 x, 출력위치 y
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    if cursor_x > x:
        x += 5
    else:
        x -= 5
    if cursor_y > y:
        y += 5
    else :
        y -= 5

    delay(0.05)
    get_events()

close_canvas()

