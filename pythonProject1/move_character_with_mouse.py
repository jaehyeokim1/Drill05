import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def lerp(a, b, t):
    return a + (b - a) * t


def set_random_target():
    global target_x, target_y

    target_x = random.randint(0, TUK_WIDTH)
    target_y = random.randint(0, TUK_HEIGHT)


running = True
frame = 0


x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
target_x, target_y = x, y

hide_cursor()


set_random_target()


facing_right = True

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    if target_x > x:
        facing_right = True
    elif target_x < x:
        facing_right = False


    x = lerp(x, target_x, 0.1)
    y = lerp(y, target_y, 0.1)


    if facing_right:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, '', x, y, 100, 100)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)


    hand.draw(target_x, target_y)

    update_canvas()


    if abs(x - target_x) < 10 and abs(y - target_y) < 10:
        set_random_target()

    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
