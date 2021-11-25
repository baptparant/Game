import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game, x, y, level="1"):
        super().__init__()
        self.level = level
        self.game = game
        self.ratio = 17
        self.image = pygame.image.load("assets/monster.png")
        self.image = pygame.transform.scale(self.image, (self.game.screen_width / self.ratio,
                                                         self.game.screen_width / self.ratio))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 4

