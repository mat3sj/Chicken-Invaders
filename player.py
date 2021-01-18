import random

# controlled by player
class Rocket(object):
    ver_velocity = 0
    hor_velocity = 0
    max_speed = 3
    def __init__(self, x, y):
        self.weapon = 'red'
        self.x = x
        self.y = y

    def move(self, ver, hor):
        if ver != 0 or self.ver_velocity !=0:
            if ver != 0 and abs(self.ver_velocity) < self.max_speed:
                self.ver_velocity += ver
            else:
                self.ver_velocity -= self.ver_velocity/abs(self.ver_velocity)
        if hor != 0 or self.hor_velocity != 0:
            if hor != 0 and abs(self.hor_velocity) < self.max_speed:
                self.hor_velocity += hor
            else:
                self.hor_velocity -= self.hor_velocity/abs(self.hor_velocity)
        self.x += self.hor_velocity
        self.y += self.ver_velocity

class Projectile(object):
    def __init__(self, x, y, power, ver, hor,type):
        self.ver_velocity = ver
        self.hor_velocity = hor
        self.power = power
        self.x = x
        self.y = y

    def move(self):
        self.x += self.hor_velocity
        self.y += self.ver_velocity

class Weapon(Rocket):
    def __init__(self):
        self.type = "red"
        self.power = 1

    def fire(self):
        if self.type == "red":
            if self.power == 1:
                drawer.projectiles.append(Projectile(self.x,self.y,-4,0,'red'))
            elif self.power == 2:
                drawer.projectiles.append(Projectile(self.x+2, self.y, -4, 0,'red'))
                drawer.projectiles.append(Projectile(self.x-2, self.y, -4, 0,'red'))
            elif self.power == 3:
                drawer.projectiles.append(Projectile(self.x+3, self.y, -4, 0,'red'))
                drawer.projectiles.append(Projectile(self.x, self.y, -4, 0,'red'))
                drawer.projectiles.append(Projectile(self.x-3, self.y, -4, 0,'red'))

        elif self.type == "green":
            pass

class Drawer(object):
    rockets = []
    projectiles = []

drawer = Drawer()