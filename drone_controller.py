from time import sleep

import pygame
from djitellopy import tello


def is_pressed(key):
    pressed_keys = pygame.key.get_pressed()
    my_key = getattr(pygame, "K_{}".format(key))
    return True if pressed_keys[my_key] else False


def process_input():
    x, y, z, rot = 0, 0, 0, 0

    if is_pressed("g"): z += drone_speed
    if is_pressed("b"): z -= drone_speed

    if is_pressed("a"): x -= drone_speed
    if is_pressed("d"): x += drone_speed

    if is_pressed("w"): y += drone_speed
    if is_pressed("s"): y -= drone_speed

    if is_pressed("q"): rot += drone_speed
    if is_pressed("e"): rot -= drone_speed

    drone.send_rc_control(x, y, z, rot)


drone_speed = 50

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
screen = pygame.display.set_mode((960, 720))
pygame.init()

font = pygame.font.SysFont(None, 46)
battery_img = pygame.image.load("battery.png").convert_alpha()
battery_img = pygame.transform.scale(battery_img, (100, 50))

drone.streamon()
drone.takeoff()

running = True

while running:
    image = drone.get_frame_read().frame
    image = pygame.image.frombuffer(image.tobytes(), image.shape[1::-1], "BGR")
    screen.blit(image, (0, 0))
    battery_label = font.render(str(drone.get_battery()), True, (0, 0, 0))
    screen.blit(battery_img, (20, 20))
    screen.blit(battery_label, (50, 30))

    process_input()

    if is_pressed("p"):
        running = False

    pygame.display.update()
    pygame.event.pump()
    sleep(0.05)

drone.land()
drone.streamoff()
pygame.quit()
