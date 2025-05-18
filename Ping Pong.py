from pygame import *

font.init()
mixer.init()


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

class Heart(GameSprite):
    def __init__(self, player_speed, player_image, player_x, player_y):
        super().__init__(player_speed, player_image, player_x, player_y)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image),(50,40))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

clock = time.Clock()
fps = 60

but_x = 293
but_y = 226
but_w = 122
but_h = 85


game_status = True

while game_status:
    window.fill((41, 182, 214))

    for e in event.get():
        if e.type == QUIT:
            game_status = False

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                game_status = False
                mouse_pos = mouse.get_pos()

                if but_x <= mouse_pos[0] <= but_x + but_w and but_y <= mouse_pos[1] <= but_y + but_h:
                    print('Хорошей игры!')
            
    #draw.rect(window, (255,0,0), (but_x, but_y, but_w, but_h))

    play = transform.scale(image.load('but_play.png'),(400,300))
    window.blit(play, (175, 150))

    clock.tick(fps)

    display.update()



gs = Player(5, 'палка.png', 50, 160)
gs1 = Player(5, 'палка.png', 650, 160)

ball = Ball(5, 'мяч.png', 300, 200)

hearts_left = [
    Heart(1, 'красное сердце.png', 2, 460),
    Heart(1, 'красное сердце.png', 2, 430)
]

hearts_right = [
    Heart(1, 'красное сердце.png', 654, 460),
    Heart(1, 'красное сердце.png', 654, 430)
]

gray_hearts_left = [
    Heart(1, 'серое сердце.png', 2, 460),
    Heart(1, 'серое сердце.png', 2, 430)
]

gray_hearts_right = [
    Heart(1, 'серое сердце.png', 654, 460),
    Heart(1, 'серое сердце.png', 654, 430)
]



pong = mixer.Sound('отскок.ogg')

count = 0
lives_right = 2
lives_left = 2

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

while game_status == False:
    window.fill((41, 182, 214))

    font_5 = font.Font(None, 40)
    cont = font_5.render('Счет:'+ str(count), True, (0,0,0))

    window.blit(cont, (325,20))

    for e in event.get():
            if e.type == QUIT:
                game_status = True

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(gs, ball) or sprite.collide_rect(gs1, ball):
        speed_x *= -1.1
        pong.play()
        count += 1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1.1

    if ball.rect.x > 650: 
        lives_right -= 1
        if lives_right >= 0:
            ball.rect.x, ball.rect.y = 300, 200
            count = 0
            speed_x, speed_y = 3, 2
        else:
            finish = True
            window.blit(lose1, (400, 220))
            window.blit(win2, (63, 220))
                
    if ball.rect.x < 0:  
        lives_left -= 1
        if lives_left >= 0:
            ball.rect.x, ball.rect.y = 300, 200
            count = 0
            speed_x, speed_y = 3, 2
        else:
            finish = True
            window.blit(lose2, (63, 220))
            window.blit(win1, (400, 220))

    for i in range(2):
        if i < lives_left:
            hearts_left[i].reset()
        else:
            gray_hearts_left[i].reset()
        
        if i < lives_right:
            hearts_right[i].reset()
        else:
            gray_hearts_right[i].reset()

    gs.reset()
    gs.update()

    gs1.reset()
    gs1.update()

    ball.reset()

    clock.tick(fps)

    display.update()
