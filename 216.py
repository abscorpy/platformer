import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'),pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'),pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png')]
walkLeft = [pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),pygame.image.load('L1.png'),  pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = False
        
    def draw(self, win):
        if(self.walkCount < 50):

            if not (self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount], (self.x, self.y))
                    self.walkCount +=1
                    ##print (self.walkCount)
                elif self.right:
                    win.blit(walkRight[self.walkCount], (self.x, self.y))
                    self.walkCount +=1
                    ##print (self.walkCount)
            else:
                if (self.right):
                    win.blit(walkRight[0], (self.x, self.y))
        
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
                    ##print(self.walkCount)
                
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    man.draw(win)


    for bullet in bullets:
        bullet.draw(win)
            
    ##pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

#mainloop
man = player(300, 410, 64, 64)

bullets = []
run = True
keys = pygame.key.get_pressed()

while run:
    clock.tick(27)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round (man.y + man.height //2), 6, (0, 0, 0), facing))

    

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:

        man.standing=True

    if not(man.isJump):
        ##if keys[pygame.K_UP] and man.y > man.vel:
          ##  man.y -= man.vel
        if keys[pygame.K_DOWN] and man.y < 500 - man.height - man.vel:
            man.y += man.vel
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right= False
            man.left = False

            man.walkCount = 0
    else:
        if man.jumpCount >= -5:
            neg = 1
            if man.jumpCount < 0:
                neg = -1                
            man.y -= (man.jumpCount ** 2)* 2 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 5

    redrawGameWindow()
    ##win.fill((0, 0, 0))

    ##pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
