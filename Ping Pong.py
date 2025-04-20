from pygame import *

window = display.set_mode((700,500))
window.fill((84, 240, 240))

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(105,85))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and gs.rect.y > 1:
            gs.rect.y -= 5
        if keys_pressed[K_s] and gs.rect.y < 410:
            gs.rect.y += 5
        if keys_pressed[K_UP] and gs1.rect.y > 10:
            gs1.rect.y -= 5
        if keys_pressed[K_DOWN] and gs1.rect.y < 410:
            gs1.rect.y += 5

gs = Player(5, 'палка.png.png', 30, 200)
gs1 = Player(5, 'палка.png.png', 600, 200)

clock = time.Clock()
fps = 60


game = True
while game: 
    window.fill((84, 240, 240))

    for e in event.get():
        if e.type == QUIT:
            game = False

    gs.reset()
    gs.update()

    gs1.reset()
    gs1.update()

    clock.tick(fps)

    display.update()