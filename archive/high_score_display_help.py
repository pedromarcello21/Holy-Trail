import pygame
import pygame_textinput
from lib.high_score_manager import Highscore

pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
test_font = pygame.font.Font("super-mario-bros-nes.ttf", 20) #get font

intro_title_surface = test_font.render("High Scores", False, "Black")
intro_title_rect = intro_title_surface.get_rect(center = (400, 50))


def display_score(score_font, score, disp):
    score_surface = score_font.render(f"Score: {score}", False, "Black")
    score_rect = score_surface.get_rect(center = (400, disp))
    screen.blit(score_surface, score_rect)

clock = pygame.time.Clock()

#see high scores in console
# print(Highscore.get_high_scores()[4][1])



running = True
while running:
    screen.fill("White")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    
    # Blit its surface onto the screen

    screen.blit(intro_title_surface, intro_title_rect)
    
    display = 75
    for i in range(0,5):
        display_score(test_font, Highscore.get_high_scores()[i][1], display)
        display+=25

    pygame.display.update()
    clock.tick(30)

pygame.quit()