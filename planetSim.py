import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
YELLOW_BROWN = (204, 153, 102)
GRAY = (128, 128, 128)


class Planet:
    ASTRONOMICAL_UNIT = 149.6e6 * 1000
    GRAVITATIONAL_UNIT = 6.67428e-11
    SCALE = 225 / ASTRONOMICAL_UNIT  # One AU = 100 pixels
    TIMESTEP = 3600 * 24  # One day

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.colour, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    # Planets
    sun = Planet(0, 0, 30, ORANGE, 1.98892 * 10**30)
    sun.sun = True

    # Perhaps create an actual earth coloured earth
    earth = Planet(-1 * Planet.ASTRONOMICAL_UNIT, 0, 16, BLUE, 5.9742 * 10**24)

    mars = Planet(-1.524 * Planet.ASTRONOMICAL_UNIT, 0, 12, RED, 6.39 * 10**23)

    mercury = Planet(0.387 * Planet.ASTRONOMICAL_UNIT, 0, 8, GRAY, 3.30 * 10**23)

    venus = Planet(0.723 * Planet.ASTRONOMICAL_UNIT, 0, 14, YELLOW_BROWN, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WINDOW)
        pygame.display.update()

    pygame.quit()


main()



