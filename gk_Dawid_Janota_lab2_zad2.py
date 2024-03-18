import pygame


szerokosc = 400
wysokosc = 400
ekran = pygame.display.set_mode((szerokosc, wysokosc))


bialy = (255, 255, 255)
czarny = (0, 0, 0)
zolty = (255, 255, 0)


ekran.fill(bialy)


pygame.draw.circle(ekran, czarny, (szerokosc/2, wysokosc/2), 100)


pygame.draw.rect(ekran, zolty, (szerokosc/2-50, wysokosc/2-50, 100, 100))


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


