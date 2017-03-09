import bodies
import pygame
import time
import math
from constants import earth_orbit_speed as speed
from constants import earth_distance_from_sun as radius
from constants import km_per_pixel as km_per_pixel

hour_angle = speed / radius #Angle round a circle that earth move in one hour
P = (math.pi - hour_angle) / 2
vector_length = 2 * (math.sin(0.5 * hour_angle) * radius) #Length of travel in one hour
inverse_angle = (math.pi / 2) - P #Inverse of vector length, used in calculating shift

x_shift = math.sin(inverse_angle) * vector_length * -1
y_shift = math.cos(inverse_angle) * vector_length

pygame.init()

earth = bodies.earth
sun = bodies.sun
created_bodies = bodies.created_bodies

(width, height) = (1200, 800)
X_OFFSET = width / 2
Y_OFFSET = height / 2

screen = pygame.display.set_mode((width, height))

def km_to_p(x):
    if x == 0:
        return 0
    return (x / km_per_pixel)

def update_pos(body):
    global x_shift
    global y_shift
    if type(body) != bodies.Body:
        raise SystemExit
    body.position[0] = body.position[0] + x_shift
    body.position[1] = body.position[1] + y_shift
    x_shift_old = x_shift
    y_shift_old = y_shift
    x_shift = (x_shift_old * math.cos(hour_angle)) - (y_shift_old * math.sin(hour_angle))
    y_shift = (y_shift_old * math.cos(hour_angle)) + (x_shift_old * math.sin(hour_angle))

def draw_body(body):
    if type(body) != bodies.Body:
        raise SystemExit
    pygame.draw.circle(screen, (255,255,255), (int(km_to_p(body.position[0])+X_OFFSET),
                                               int(km_to_p(body.position[1])+Y_OFFSET)),10, 2)


#pygame.draw.circle(screen, (255,255,255), (150, 100), 10, 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_body(earth)
    draw_body(sun)
    update_pos(earth)
    
    pygame.display.flip()
    
    time.sleep(1)

#pygame.display.quit()

