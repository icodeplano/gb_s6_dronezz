from easytello import tello
from time import sleep

drone = tello.Tello()
drone.takeoff()

# iterate the go() method to see the range of movement.
# change in X
for i in range(20, 200, 5):
    drone.go(i, 0, 0, 20)
    sleep(0.1)

# change in Y
for i in range(20, 200, 5):
    drone.go(0, i, 0, 20)
    sleep(0.1)

# change in Z
for i in range(20, 200, 5):
    drone.go(0, 0, i, 20)
    sleep(0.1)

drone.land()