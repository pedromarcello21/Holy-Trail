import pygame
import pygame_textinput

pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Enter Your Initials")
test_font = pygame.font.Font("super-mario-bros-nes.ttf", 20) #get font


# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()
textinput.font_object = test_font

clock = pygame.time.Clock()

running = True
while running:
    screen.fill("White")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Save the initials to your database
            initials = textinput.value
            print(f"User initials: {initials}")
            running = False

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
