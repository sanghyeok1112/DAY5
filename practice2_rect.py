import pico2d

pico2d.open_canvas()

grass = pico2d.load_image('grass.png')
character = pico2d.load_image('character.png')

x = 0
y = 90
while 1:
    pico2d.clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if x < 750 and y == 90:
        x += 2
    elif x >= 750 and y < 550:
        y += 2
    elif x > 0 and y == 550:
        x -= 2
    elif x <= 50 and y > 90:
        y -= 2
    pico2d.delay(0.01)

pico2d.clear_canvas()