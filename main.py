import time

from tello import Tello

drone = Tello()
drone.send_command("command")
drone.send_command("battery?")
drone.send_command("takeoff")
drone.send_command("up 50")
#drone.send_command("flip b")
drone.send_command("land")
