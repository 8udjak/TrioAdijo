import time

from tello import Tello

drone = Tello()
drone.send_command("command")
#drone.send_command("streamon")
drone.send_command("battery?")
#drone.send_command("sleep 5")
#drone.send_command("streamoff")

drone.send_command("takeoff")
drone.send_command("up 50")
drone.send_command("forward 100")
drone.send_command("flip b")
drone.send_command("flip f")
drone.send_command("flip l")
drone.send_command("flip r")
drone.send_command("land")

