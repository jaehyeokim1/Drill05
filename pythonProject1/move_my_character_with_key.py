from pico2d import *

open_canvas()
TUK_GROUND = load_image('TUK_GROUND.png')
character = load_image('animation.png')
character_idle = load_image('animation_idle.png')

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 10
            elif event.key == SDLK_LEFT:
                dir_x = -10
            elif event.key == SDLK_UP:
                dir_y = 10
            elif event.key == SDLK_DOWN:
                dir_y = -10
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and dir_x > 0:
                dir_x = 0  # 방향키 떼면 0으로 설정
            elif event.key == SDLK_LEFT and dir_x < 0:
                dir_x = 0
            elif event.key == SDLK_UP and dir_y > 0:
                dir_y = 0
            elif event.key == SDLK_DOWN and dir_y < 0:
                dir_y = 0


running = True
x = 800 // 2
y = 90
frame = 0
dir_x = 0
dir_y = 0

min_x = 50
max_x = 750
min_y = 50
max_y = 550

while running:
    clear_canvas()
    TUK_GROUND.draw(400, 300)

    # 캐릭터가 움직이고 있는지 확인
    if dir_x == 0 and dir_y == 0:
        # 움직이지 않을 때: 정지 상태 이미지 사용
        character_idle.draw(x, y,80,80)
    else:
        # 움직일 때: 애니메이션 이미지 사용
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        frame = (frame + 1) % 8

    update_canvas()
    handle_events()


    x = min(max_x, max(min_x, x + dir_x * 5))
    y = min(max_y, max(min_y, y + dir_y * 5))

    delay(0.05)

close_canvas()
