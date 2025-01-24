import pygame
size = width, heigth = (800, 600)
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
pygame.init()

class Ball:
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
    
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 0)

class Player:
    def __init__(self, x, y, w, h, vy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vy = vy
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h))

ball = Ball(400, 300, 10, 3, 3)
left = Player(100, 100, 10, 100, 3)

while True: #начало программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #------------------------------------------        
    screen.fill((255, 255, 255))   
    #Управление шариком
    ball.draw()    
    ball.x += ball.vx
    ball.y += ball.vy    
    if ball.x>width-ball.r:
        ball.vx = -ball.vx
    if ball.x<ball.r:
        ball.vx = -ball.vx        
    if ball.y>heigth-ball.r:
        ball.vy = -ball.vy
    if ball.y<ball.r:
        ball.vy = -ball.vy 
    
    #Управление игроками
    #Левый
    left.draw()
     
    
    
    #------------------------------------------
    pygame.display.flip()
    fpsClock.tick(60) #конец программы