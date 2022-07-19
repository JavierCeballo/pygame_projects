# import pygame package
import pygame

# initializing imported module
pygame.init()

# displaying a window
# height: 500, width: 400
window = pygame.display.set_mode((600, 800))

# Setting a window title
pygame.display.set_caption("My First Window PyGame")


# creating a boolean value which checks
# if the game is running
is_running = True

# keeping the game running till running is True
while is_running:

  # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
          
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            is_running = False

pygame.exit()