import pygame
from random import randint , choice

def calculate_time():
    time = int(pygame.time.get_ticks() / 1000)
    return time

pygame.init()
pygame.display.set_caption('Mar Ghorosne')
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()

images = {
    'Apple': pygame.image.load("F:\\Python Enjoyer\\summer_project\\apple.png").convert_alpha(),
    'banana': pygame.image.load("F:\\Python Enjoyer\\summer_project\\banana.png").convert_alpha(),
    'bomb': pygame.image.load("F:\\Python Enjoyer\\summer_project\\bomb.png").convert_alpha(),
    'strawberry': pygame.image.load("F:\\Python Enjoyer\\summer_project\\strawberry.png").convert_alpha()
}

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("F:\\Python Enjoyer\\summer_project\\snake.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
            if self.rect.right >= 700:
                self.rect.right = 700
        elif keys[pygame.K_DOWN]:
            self.rect.y += 10
            if self.rect.bottom >= 700:
                self.rect.bottom = 700
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 10
            if self.rect.left <= 0:
                self.rect.left = 0
        elif keys[pygame.K_UP]:
            self.rect.y -= 10
            if self.rect.top <= 0:
                self.rect.top = 0

    def update(self):
        self.movement()

class rewards(pygame.sprite.Sprite):
    def __init__(self , type , image_dict):
        super().__init__()
        self.image = image_dict[type]
        if type == 'Apple':
            self.rect = self.image.get_rect(center = (randint(300 , 650),randint(100 , 500)))
        elif type == 'banana':
            self.rect = self.image.get_rect(center = (randint(100 , 600),randint(300 , 650)))
        elif type == 'strawberry':
            self.rect = self.image.get_rect(center = (randint(200 , 500),randint(200 , 400)))

def collision_sprite():
    if pygame.sprite.spritecollide(snake.sprite , fruit , True):
        return True
    else:
        return False

def show_score():
    score_sur = font.render(f'Score:{score}' , False , (200,130,100))
    score_rect = score_sur.get_rect(center = (350,50))
    screen.blit(score_sur , score_rect)

# showing score
font = pygame.font.Font(None , 50)
score = 0
#snake
snake = pygame.sprite.GroupSingle()
snake.add(Snake())

#Fruits
fruit = pygame.sprite.Group()

track = 0
#ground
ground_sur = pygame.image.load('F:\\Python Enjoyer\\summer_project\\ground.jpg')

#Eat Track
last_eaten_time = None

running = True

# Music Game
music = pygame.mixer.Sound('F:\\Python Enjoyer\\summer_project\\Bethoven – Moonlight sonata.mp3')
music.set_volume(0.3)
music.play(loops=-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False         


    screen.blit(ground_sur,(0,0))

    snake.update()
    snake.draw(screen)
    timer = calculate_time()
    
    if len(fruit) == 0:
        if last_eaten_time == None:
            prize = choice(['Apple','banana','strawberry'])
            fruit.add(rewards(prize , images))
        elif abs(last_eaten_time - timer) >= 5:
            prize = choice(['Apple','banana','strawberry'])
            fruit.add(rewards(prize , images))
    

    if collision_sprite():
        if prize == 'Apple':
            score += 1
        elif prize == 'banana':
            score += 2
        elif prize == 'strawberry':
            score += 3
        last_eaten_time = timer
    
    fruit.draw(screen)
    show_score()
    
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()

