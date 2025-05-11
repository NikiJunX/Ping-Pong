from pygame import *

font.init()

window = display.set_mode((700,500))
window.fill((41, 182, 214))

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(95,75))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__(player_speed, player_image, player_x, player_y)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(10,100))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and gs.rect.y > 1:
            gs.rect.y -= 5
        if keys_pressed[K_s] and gs.rect.y < 400:
            gs.rect.y += 5
        if keys_pressed[K_UP] and gs1.rect.y > 1:
            gs1.rect.y -= 5
        if keys_pressed[K_DOWN] and gs1.rect.y < 400:
            gs1.rect.y += 5

class Ball(GameSprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__(player_speed, player_image, player_x, player_y)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(50,40))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


gs = Player(5, 'палка.png', 50, 160)
gs1 = Player(5, 'палка.png', 650, 160)

ball = Ball(5, 'мяч.png', 300, 200)

clock = time.Clock()
fps = 60

count = 0

speed_x = 3
speed_y = 2

font_1 = font.Font(None, 50)
win1 = font_1.render('player 1-st win', True, (0, 230, 0))

font_2 = font.Font(None, 50)
lose1 = font_2.render('player 1-st lose', True, (230, 0, 0))

font_3 = font.Font(None, 50)
win2 = font_3.render('player 2-nd win', True, (0, 230, 0))

font_4 = font.Font(None, 50)
lose2 = font_4.render('player 2-nd lose', True, (230, 0, 0))


finish = False
game = True
while game: 
    window.fill((41, 182, 214))

    font_5 = font.Font(None, 40)
    cont = font_5.render('Счет:'+ str(count), True, (0,0,0))

    window.blit(cont, (325,20))

    for e in event.get():
            if e.type == QUIT:
                game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(gs, ball) or sprite.collide_rect(gs1, ball):
        speed_x *= -1.1
        count += 1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1.1

    if ball.rect.x > 650:
        window.blit(lose1, (400, 220))
        window.blit(win2, (63, 220))
        finish = 1
    
    if ball.rect.x < 0:
        window.blit(lose2, (63, 220))
        window.blit(win1, (400, 220))
        finish = 1

    gs.reset()
    gs.update()

    gs1.reset()
    gs1.update()

    ball.reset()

    clock.tick(fps)

    display.update()
