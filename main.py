import pygame

FPS = 24

TILESIZE = 10

pygame.init()

screen = pygame.display.set_mode((50*TILESIZE, 50*TILESIZE))
clock = pygame.time.Clock()

pygame.display.set_caption("TPS")

screen_width, screen_height = pygame.display.get_window_size()

objects = []

class Camera:
    def __init__(self, target):
        self.target = target
    
    def update(self):
        for obj in objects:
            obj.x -= self.target.direction.x
            obj.y -= self.target.direction.y



class Player:
    def  __init__(self) -> None:
        self.surf = pygame.Surface((TILESIZE*2, TILESIZE*2))
        self.rect = self.surf.get_rect()
        
        self.direction = pygame.math.Vector2((0, 0))

        self.x, self.y = 0, 0

        self.speed = 5

        self.rect.center = (screen_width / 2) + self.x, (screen_height / 2) + self.y

        self.camera = Camera(self)
    

    def handleinput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y -= (0.1 * self.speed)
        elif keys[pygame.K_DOWN]:
            self.direction.y += (0.1 * self.speed)
        else:
            if self.direction.y > 0.5:
                self.direction.y -= 0.5
            elif self.direction.y < -0.5:
                self.direction.y += 0.5
            else:
                self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x -= (0.1 * self.speed)
        elif keys[pygame.K_RIGHT]:
            self.direction.x += (0.1 * self.speed)
        else:
            if self.direction.x > 0.5:
                self.direction.x -= 0.5
            elif self.direction.x < -0.5:
                self.direction.x += 0.5
            else:
                self.direction.x = 0

            


        self.y += self.direction.y
        self.x += self.direction.x


    def update(self):
        self.rect.center = (screen_width / 2) + self.x, (screen_height / 2) + self.y
        self.handleinput()
        self.camera.update()
        self.surf.fill((20, 20, 20))

        
class Other:
    def __init__(self, xy) -> None:
        self.surf = pygame.Surface((TILESIZE*2, TILESIZE*2))
        self.surf.fill((255, 0, 0))

        self.x, self.y = xy


        self.rect = self.surf.get_rect()
        self.rect.center = (screen_width/2) + self.x, (screen_height/2)+self.y
    
    def update(self):
        self.rect.center = (screen_width/2) + self.x, (screen_height/2)+self.y
        self.surf.fill((255, 0, 0))


class Bullet():
    def __init__(self, player: Player, pos) -> None:
        self.surf = pygame.Surface((TILESIZE/2, TILESIZE/2))
        self.surf.fill((255, 0, 0))

        self.x, self.y = player.x, player.y
        
        self.pos = pos

        self.vector = pygame.math.Vector2

        self.rect = self.surf.get_rect()
        self.rect.center = (screen_width/2) + self.x, (screen_height/2)+self.y
    
    def update(self):
        self.rect.center = (screen_width/2) + self.x, (screen_height/2)+self.y
        self.surf.fill((255, 0, 0))



crosshairsurf = pygame.transform.scale(pygame.image.load("crosshair.bmp"), (30, 30))
crosshairrect = crosshairsurf.get_rect()

pygame.mouse.set_visible(False)

running = False
if __name__ ==  "__main__":
    running = True

player = Player()

objects.append(player)

otherobj = Other((20, 20))

otherobj2 = Other((-10, -40))


objects.append(otherobj)

objects.append(otherobj2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen_width, screen_height = pygame.display.get_window_size()
    
    screen.fill((13, 153, 0))

    

    for obj in objects:
        screen.blit(obj.surf, obj.rect)
        obj.update()

    crosshairrect.center = pygame.mouse.get_pos()

    screen.blit(crosshairsurf, crosshairrect)
    pygame.display.update()
    clock.tick(FPS)