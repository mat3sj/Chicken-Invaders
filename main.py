import player, graphics as g, time, pygame


def main():
    drawer = g.Drawer()

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        drawer.redraw()

if __name__ == "__main__":
    main()

