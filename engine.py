import pygame
import math
from maps import map1

#3D-движек проекта
class Engine:
    def __init__(self, width, height):
        self.DEPTH = 1000
        self.ANGLE = 60
        self.RAYS = 800
        self.width = width
        self.height = height

                
    def get_cur_tile(self, x, y):
        return (x // 50), (y // 50)


    def ray_casting(self, player_pos, player_angle, color, screen, texture):
        ray_width = self.width / self.RAYS
        cur_x, cur_y = player_pos
        tile_x, tile_y = self.get_cur_tile(cur_x, cur_y)
        angle = player_angle - self.ANGLE / 2

        MAP_HEIGHT = len(map1)
        MAP_WIDTH = len(map1[0])

        for i in range(self.RAYS):
            sin_a = math.sin(math.radians(angle))
            cos_a = math.cos(math.radians(angle))

            x, dx = (tile_x * 50 + 50, 1) if cos_a >= 0 else (tile_x * 50, -1)
            depth_v = self.DEPTH
            for _ in range(0, self.width, 50):
                depth_v = (x - cur_x) / (cos_a if cos_a != 0 else 0.0001)
                y_v = cur_y + depth_v * sin_a
                a, b = self.get_cur_tile(x + (1 if cos_a >= 0 else -1), y_v)
            
                if 0 <= a < MAP_WIDTH and 0 <= b < MAP_HEIGHT:
                    if map1[int(b)][int(a)] == 0: break
                else: break
                x += dx * 50

        
            y, dy = (tile_y * 50 + 50, 1) if sin_a >= 0 else (tile_y * 50, -1)
            depth_h = self.DEPTH
            for _ in range(0, self.height, 50):
                depth_h = (y - cur_y) / (sin_a if sin_a != 0 else 0.0001)
                x_h = cur_x + depth_h * cos_a
                a, b = self.get_cur_tile(x_h, y + (1 if sin_a >= 0 else -1))
            
                if 0 <= a < MAP_WIDTH and 0 <= b < MAP_HEIGHT:
                    if map1[int(b)][int(a)] == 0: break
                else: break
                y += dy * 50

        
            depth, offset = (depth_v, y_v) if depth_v < depth_h else (depth_h, x_h)
            offset = int(offset) % 50
            
            depth *= math.cos(math.radians(angle - player_angle))
            depth = max(0.1, depth)

            proj_height = int(30000 / depth)

            texture_x = int((offset / 50) * 799)

            wall_part = texture.subsurface(texture_x, 0, 1, 600)

            wall_part = pygame.transform.scale(wall_part, (int(ray_width) + 1, proj_height))

            screen.blit(wall_part, (i * ray_width, self.height // 2 - proj_height // 2))

            angle += self.ANGLE / self.RAYS



        