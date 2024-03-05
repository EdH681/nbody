import os
import random
import vector

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import time
from math import cbrt, pi


class Body:
    def __init__(self, display, x: float, y: float, mass: float, density: float = 3):
        self.mass = mass
        self.display = display
        self.density = density
        self.pos = vector.Vector2(x, y)
        self.velocity = vector.blank()
        self.others = []

    def __calculate_radius(self):
        m = self.mass*100
        p = self.density
        numerator = 3*m
        denominator = 4*pi*p
        fraction = numerator/denominator
        return cbrt(fraction)

    def __draw(self):
        radius = self.__calculate_radius()
        pos = (self.pos[0], self.pos[1])
        pygame.draw.circle(self.display, "black", pos, radius)

    def __influence(self):
        pass

    def add(self, bodies):
        self.others = bodies

    def run(self):
        self.__draw()


def runtime(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"runtime: {end - start:.2f}")

    return wrapper


@runtime
def run():
    pygame.init()
    win = pygame.display.set_mode((900, 900))
    #
    bodies = [Body(win, random.randint(10, 890), random.randint(10, 890), 1) for _ in range(100)]
    for body in bodies:
        body.add(bodies)
    #
    running = True
    while running:
        win.fill("white")
        #
        for body in bodies:
            body.run()
        #
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


if __name__ == "__main__":
    run()
