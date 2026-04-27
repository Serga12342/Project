import math
from maps import map1

#Класс игрока
class Player:
    def __init__(self, coords, speed, health, angle, angle_speed):
        self.coords = coords
        self.speed = speed
        self.health = health
        self.angle = angle
        self.angle_speed = angle_speed

    def moove_W(self, delta_time):
        new_x = self.coords[0] + self.speed*delta_time*math.cos(math.radians(self.angle))
        new_y = self.coords[1] + self.speed*delta_time*math.sin(math.radians(self.angle))
        if map1[int(new_y//50)][int(new_x//50)] == 1:
            self.coords = [new_x, new_y]

    def moove_S(self, delta_time):
        new_x = self.coords[0] - (self.speed*delta_time*math.cos(math.radians(self.angle)))
        new_y = self.coords[1] - (self.speed*delta_time*math.sin(math.radians(self.angle)))
        if map1[int(new_y//50)][int(new_x//50)] == 1:
            self.coords = [new_x, new_y]

    def moove_A(self, delta_time):
        new_x = self.coords[0] + self.speed*delta_time*math.sin(math.radians(self.angle))
        new_y = self.coords[1] - (self.speed*delta_time*math.cos(math.radians(self.angle)))
        if map1[int(new_y//50)][int(new_x//50)] == 1:
            self.coords = [new_x, new_y]

    def moove_D(self, delta_time):
        new_x = self.coords[0] - (self.speed*delta_time*math.sin(math.radians(self.angle)))
        new_y = self.coords[1] + self.speed*delta_time*math.cos(math.radians(self.angle))
        if map1[int(new_y//50)][int(new_x//50)] == 1:
            self.coords = [new_x, new_y]      




