import pygame

class walls:
    def __init__(self, pos, wType, collision):
        self.pos = tuple(pos)
        self.type = wType
        self.collision = collision

    def draw(self,surf):
        surf.blit()