import pygame

class Game:
    def __init__(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((800, 800))
        self.is_running: bool = True

    def update_screen(self) -> None:
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self) -> None:
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.update_screen()
