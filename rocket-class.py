class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, step_y=1, step_x=0):
        self.y += step_y
        self.x += step_x


rocket = Rocket(2, 5)
rocket.move_rocket(10)
