import pico2d
import math

pico2d.open_canvas()

grass = pico2d.load_image('grass.png')
character = pico2d.load_image('character.png')

x = 0
y = 90
angle = 0
while angle < 2 * math.pi:
    pico2d.clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    angle += 0.1
    x = 400 + 200 * math.cos(angle)
    y = 300 + 200 * math.sin(angle)
    pico2d.delay(0.01)

pico2d.clear_canvas()