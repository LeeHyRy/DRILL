import random
from pico2d import *
import game_world
import game_framework

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

# 날아가는 속도가 사람의 4배정도 된다고 생각하였다 (20km/h * 4 = 80km/h)
FLY_SPEED_KMPH = 80.0  # Km / Hour

FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed

# 새는 날갯짓을 아주 빠르게 해야 한다고 생각했다.
# 사람이 걸으면서 팔을 좌우로 한 번 흔들 때, 새는 날갯짓을 4번꼴로 하도록 하였다.
TIME_PER_ACTION = 0.125
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.frame = 0
        self.x, self.y, self.fall_speed = random.randint(400, 800-1), random.randint(200, 400-1), 0
        self.velocity = FLY_SPEED_PPS
        self.dir = 1

    def get_bb(self):
        return 0, 0, 0, 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time * self.dir
        if (self.x > 1600):
            self.dir = -1
        elif (self.x < 0):
            self.dir = 1
