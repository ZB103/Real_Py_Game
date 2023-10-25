#Simple pygame program created following a Real Python tutorial: https://realpython.com/pygame-a-primer/
import pygame
pygame.init()

#Make a circle
# #Set up drawing window - 500 pixels on each side
# screen = pygame.display.set_mode([500, 500])

# #Run until user asks to quit
# running = True
# while(running):
    # #Checks if the user clicked the close button and if so closes the program
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # running = False
    
    # #Fill background with white (RFB color)
    # screen.fill((255, 255, 255))
    # #Draw solid blue circle in the center
    # #screen: the window on which to draw
    # #(0, 0, 255): a tuple containing RGB color values
    # #(250, 250): a tuple specifying the center coordinates of the circle
    # #75: the radius of the circle in pixels
    # pygame.draw.circle(screen, (0, 0, 225), (250, 250), 75)
    # #Flip display - updates contents of the screen
    # pygame.display.flip()

# pygame.quit()



#import pygame.locals for easier access to key coordinated
from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT,)

pygame.init()

#Define screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))

#Create a surface
surf = pygame.Surface((50,50))
surf.fill((0,0,0))
rect = surf.get_rect()

#Draw surface on screen - top left corner placed on coordinates given
# screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
surf_center = (((SCREEN_WIDTH-surf.get_width())/2, (SCREEN_HEIGHT-surf.get_height())/2))
screen.blit(surf, surf_center)
pygame.display.flip()

#Event handler - game loop
#Variable to keep main loop running
running = True

#main loop
while running:
    #look at every event in the queue
    for event in pygame.event.get():
        #Detect if a key was pressed
        if event.type == KEYDOWN:
            #Detect which key was pressed
            if event.key == K_ESCAPE:
                #Close the game
                running = False
        
        #Detect if X was clicked
        elif event.type == QUIT:
            #Close the game
            running = False