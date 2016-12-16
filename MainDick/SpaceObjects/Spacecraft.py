class Spacecraft:
    def __init__(self, name, power, fuel, mass, position_x, position_y, image, direction = 0, position_z = 0):
        self.name = name
        self.power = power
        self.fuel = fuel
        self.mass = mass
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.image = image
        self.direction = direction
