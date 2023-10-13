import pygame, random, sys

def setup_walker(number):
    for i in range(0, number):
        walker = pygame.Rect(x_cord, y_cord, width, width)
        walkers.append(walker)
        color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        colors.append(color)

def update_walker():
    for i in range(0, len(walkers)):
        walkers[i].x +=  random.random() * random.randint(-1, 1)
        walkers[i].y += random.random() * random.randint(-1, 1)
        if walkers[i].x > screen_width:
            walkers[i].x -= 1
        if walkers[i].x < 0:
            walkers[i].x += 1
        if walkers[i].y > screen_width:
            walkers[i].y -= 1
        if walkers[i].y < 0:
            walkers[i].y += 1
        pygame.draw.rect(screen, colors[i], walkers[i])
    
width = 5
walker_amount = 10
screen_width = 1280
screen_height = 960
try:
    walker_amount = int(sys.argv[1])
    width = int(sys.argv[2])
    screen_width = int(sys.argv[3])
    screen_height = int(sys.argv[4])

except:
    print("some arguments missing")
    
go = False
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("random_walker")
pygame.init()
x_cord = screen_width / 2
y_cord = screen_height / 2

walkers =  []
colors = []
setup_walker(walker_amount)
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                go = not go
    if go:    
        update_walker()
        pygame.display.flip()