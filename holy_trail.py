#Import packages
import pygame
import pygame_textinput
from sys import exit
import os
import random
from lib.high_score_manager import Highscore


pygame.init() ##initialize pygame
screen = pygame.display.set_mode((800, 400)) ##create display surface
pygame.display.set_caption("Holy Trail")
clock = pygame.time.Clock()

##samples

intro_sample = pygame.mixer.Sound("samples/intro.mp3")
jump_sample = pygame.mixer.Sound("samples/jump.wav")
new_high_score_sample = pygame.mixer.Sound("samples/new-high-score.mp3")

## Text ishes
title_font = pygame.font.Font("font/old-school-font.ttf", 20) #get font

def display_score(score_font, score):
    score_surface = score_font.render(f"Score: {score}", False, "White")
    score_rect = score_surface.get_rect(center = (400, 25))
    screen.blit(score_surface, score_rect)

def display_high_score(score_font, user, score, disp):
    score_surface = score_font.render(f"{user}.......{score}", False, "White")
    score_rect = score_surface.get_rect(center = (400, disp))
    screen.blit(score_surface, score_rect)


##Score ish

manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 5)
textinput_custom = pygame_textinput.TextInputVisualizer(manager=manager, font_object=title_font, font_color = "White")

textinput_custom_surface = textinput_custom.surface
textinput_custom_rect = textinput_custom_surface.get_rect(midbottom=(360,200))
##################


##Characters

matty_path = os.path.join('sprites/matty.png')
matty_jump = os.path.join('sprites/matty-jumping.png')

marco_path = os.path.join('sprites/marco.png')
marco_jump =os.path.join("sprites/marco-jumping.png")

luke_path = os.path.join('sprites/luke.png')
luke_jump =os.path.join("sprites/luke-jumping.png")


jj_path = os.path.join('sprites/jj.png')
jj_jump =os.path.join("sprites/jj-jumping.png")


characters = [
    {"name": "Matty", "image":pygame.image.load(matty_path).convert_alpha(), "jump":pygame.image.load(matty_jump).convert_alpha()},
    {"name": "Marco", "image":pygame.image.load(marco_path).convert_alpha(), "jump":pygame.image.load(marco_jump).convert_alpha()},
    {"name": "Luke", "image":pygame.image.load(luke_path).convert_alpha(), "jump":pygame.image.load(luke_jump).convert_alpha()},
    {"name": "JJ", "image":pygame.image.load(jj_path).convert_alpha(), "jump":pygame.image.load(jj_jump).convert_alpha()}
]

##Bandaid to fix tab bug if user presses tab before enterting active_game state.  
##Tab resets evangelist rect.  evangelist rect initialized in choose_character.  This defaults
evangelist = characters[0]
evangelist_surface = evangelist["image"]
evangelist_rect = evangelist_surface.get_rect(midbottom=(40, 300))

#pre-select first character.  When in choose_character state arrow keys add or subtract from this value to simulate selection
selected_character_index = 0

def display_characters(characters, selected_index):
    y_start = 50 #50 pixles from top
    for i, character in enumerate(characters): ##i = index, character = dictionary representing evangelist
        if i == selected_index:
            color="gold" ##sets selected character name to gold
        else:
            color="White" ##not selected is white
        text_surface = title_font.render(character["name"], False, color)
        text_rect = text_surface.get_rect(center=(410, y_start + i * 100)) #off set a bit to right, y value is incremented by 100 for every character
        screen.blit(text_surface, text_rect)
        character_rect = 275, y_start-30 + i * 100 #set character image to left of name
        screen.blit(character["image"], character_rect) #render the image and it's coordinates(rect)


#bad guys
bad_guy_path = os.path.join('sprites/bad_guy.png')
bad_guy_path2 = os.path.join('sprites/bad_guy2.png')


##Surfaces & Rectangles
sky_surface = pygame.Surface((800, 300))
sky_surface.fill("blue")
ground_surface = pygame.Surface((800, 100))
ground_surface.fill("gold")


bad_guy_surface = pygame.image.load(bad_guy_path2).convert_alpha()
bad_guy_rect = bad_guy_surface.get_rect(midbottom=(750, 300))

##### have 2nd bad guy on screen######
bad_guy_surface2 = pygame.image.load(bad_guy_path).convert_alpha()
bad_guy_rect2 = bad_guy_surface2.get_rect(midbottom=(1500, 270))

#####Titles######

intro_title_surface = title_font.render("Holy Trail", False, "White")
intro_title_rect = intro_title_surface.get_rect(center = (400, 200))

ready_surface = title_font.render("Ready...", False, "White")
ready_rect = ready_surface.get_rect(center = (400, 200))

high_score_surface = title_font.render("High Scores", False, "White")
high_score_rect = intro_title_surface.get_rect(center = (400, 50))


#Score, gravity, speed Init
score = 0
player_gravity = 0
speed = 5 #arbitrary speed
speed2 = 8 #arbitrary speed

#States
game_active = False
game_over = False
enter_initials = False
leader_boards = False
choose_character = False
ready_screen = False

# #see high scores in console
# print(Highscore.get_high_scores())

running = True
while running:

    events = pygame.event.get()
    for event in events:
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit() ##to break out of while loop

        if event.type == pygame.KEYDOWN: 
            if not enter_initials and not ready_screen:
        
                if event.key == pygame.K_SPACE:
                
                    #switch states (screens) from pressing space bar
                    if not leader_boards and not choose_character and not game_active and not game_over:
                        leader_boards = True
                    
                    #switch states (screens) from pressing space bar
                    elif leader_boards and not choose_character:
                        leader_boards = False 
                        choose_character = True

                    #can only jump w space bar when character's bottom plane is at 300
                    elif game_active and evangelist_rect.bottom == 300:
                        player_gravity = -20 #always pulling character down unless character's bottom is at 300 (ground)
                        jump_sample.play()


                    #If game over player can press space again and resets characters position, 
                    #bad guy's position, and score
                    elif game_over:
                        game_over = False
                        leader_boards = False
                        game_active = True
                        score = 0
                        evangelist_rect.midbottom = (40,300)
                        bad_guy_rect.midbottom = (800, 300)
                        bad_guy_rect2.midbottom = (1500,270)


            if event.key == pygame.K_RETURN:


                if choose_character:
                    evangelist = characters[selected_character_index] # select character of selected_character_index as chosen by user
                    evangelist_surface = evangelist["image"] # set surface
                    evangelist_rect = evangelist_surface.get_rect(midbottom=(40, 300)) #set rectangle

                    evangelist_surface_jumping = evangelist["jump"]
                    evangelist_rect_jumping = evangelist_surface_jumping.get_rect(midbottom=(40,300))
                    timer = pygame.time.get_ticks() + 3000 #have it wait 3 seconds in ready screen
                    choose_character = False
                    ready_screen = True
                
                if enter_initials:
                    
                    if len(textinput_custom.value) > 0: #ensures initials input is greater than 0 

                        user_name = textinput_custom.value
                        user = Highscore(user_name, score) # call on class to record username and score
                        user.add_score() #adds score to db
                        new_high_score_sample.play()


                        #Reset
                        enter_initials = False
                        game_active = False
                        game_over = False
                        choose_character = False
                        leader_boards = True
                        score = 0
                        textinput_custom.value = ""
                        evangelist_rect = evangelist_surface.get_rect(midbottom=(40,300))
                        bad_guy_rect.midbottom = (800, 300)
                        bad_guy_rect2.midbottom = (800,270)
                
                if game_over:
                    game_over = False
                    leader_boards = False
                    game_active = True
                    score = 0
                    evangelist_rect.midbottom = (40,300)
                    bad_guy_rect.midbottom = (800, 300)
                    bad_guy_rect2.midbottom = (1500,270)

            
            #Logic for character selection
            if event.key == pygame.K_UP:
                if choose_character: 
                    selected_character_index = (selected_character_index - 1) % len(characters)

            if event.key == pygame.K_DOWN:
                if choose_character:
                    selected_character_index = (selected_character_index + 1) % len(characters)

            #return to title screen at any time by pressing tab
            if event.key == pygame.K_TAB:
                game_active = False
                game_over = False
                leader_boards = False 
                choose_character = False
                enter_initials = False
                ready_screen = False
                score = 0
                evangelist_rect = evangelist_surface.get_rect(midbottom=(40,300))
                bad_guy_rect.midbottom = (800, 300)
                bad_guy_rect2.midbottom = (800,270)

        ##Cheat code!!
        #press on character during the game to jump no matter what position it's at.  (simulates flappy bird)
        if game_active and event.type == pygame.MOUSEBUTTONDOWN:
                    if evangelist_rect.collidepoint(event.pos):
                        player_gravity = -20
                        jump_sample.play()
    #end of events

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0,300))
        
        ##Logic for when evangelist is in air then blit him jumping else not        
        screen.blit(bad_guy_surface, bad_guy_rect)#block image transfer
        screen.blit(bad_guy_surface2, bad_guy_rect2)#block image transfer
        display_score(title_font, score)
        
        ##Player
        player_gravity +=1
        
        if evangelist_rect.bottom == 300:
            screen.blit(evangelist_surface, evangelist_rect)#block image transfer
        else:
            screen.blit(evangelist_surface_jumping, evangelist_rect)#block image transfer
        
        evangelist_rect.y += player_gravity
        if evangelist_rect.bottom >= 300 : evangelist_rect.bottom = 300

        ##bad guy
        bad_guy_rect.x -= speed ##speed at which moving left
        if bad_guy_rect.right <= 0: 
            bad_guy_rect.left = 800 #reset to right when goes too far left
            bad_guy_rect.bottom = random.randint(270,300)
           
            ##Set a floor and ceiling for my speed, 5 and 12
            speed =random.randrange(5,12)
            score +=1

        #bad guy 2
        bad_guy_rect2.x -= speed2 ##speed at which moving left
        if bad_guy_rect2.right <= 0: 
            bad_guy_rect2.left = 800 #reset to right when goes too far left
            bad_guy_rect2.bottom = random.randint(270,300)
            ##Set a floor and ceiling for my speed, 5 and 12
            
            speed2 =random.randrange(5,12)
            score +=1        

        #collision
        if evangelist_rect.colliderect(bad_guy_rect) or evangelist_rect.colliderect(bad_guy_rect2):
            game_over_surface = title_font.render("Game Over", False, "White")
            game_over_rect = game_over_surface.get_rect(center = (400, 100))
            game_over = screen.blit(game_over_surface, game_over_rect)
            
            ###if score > 5th highest score, add to it else enter_initials stays false
            if score >= Highscore.get_high_scores()[4][1]:
                enter_initials = True #switch to initials screen
                game_active = False
            else:
                game_active = False
                game_over = True #user didn't get a top 5 score so no chance to enter initials
    
    
    #below renders last screen blit from game_active to game_over screen
    elif game_over == True:
        screen.blit(sky_surface, (0, 0))#block image transfers
        display_score(title_font, score)
        screen.blit(evangelist_surface, evangelist_rect)
        screen.blit(bad_guy_surface, bad_guy_rect)
        screen.blit(bad_guy_surface2, bad_guy_rect2)
        screen.blit(game_over_surface, game_over_rect)

    #below renders last screen blit from game_active to enter_initials screen
    elif enter_initials == True:
        screen.blit(sky_surface, (0, 0))#block image transfer
        display_score(title_font, score)
        screen.blit(evangelist_surface, evangelist_rect)
        screen.blit(bad_guy_surface, bad_guy_rect)
        screen.blit(bad_guy_surface2, bad_guy_rect2)
        screen.blit(game_over_surface, game_over_rect)
        textinput_custom.update(events)#captures initials input
        screen.blit(textinput_custom.surface, textinput_custom_rect)#renders initials input


        # pygame.draw.line(screen, "White", (345,205),(365,205))
        # pygame.draw.line(screen, "White", (375,205),(395,205))
        # pygame.draw.line(screen, "White", (405,205),(425,205))
        # pygame.draw.line(screen, "White", (435,205),(455,205))
        # pygame.draw.line(screen, "White", (465,205),(485,205))

        ##Chatgpt help for above.  Want underscores for ui in initials window
        line_length = 14
        line_gap = 7
        y_position = 205

        # Draw lines closer together and a bit smaller.  draws underscores for user's initials.  draws 5 to tell user only 5 characters can be provided
        pygame.draw.line(screen, "White", (350, y_position), (350 + line_length, y_position), width = 2)
        pygame.draw.line(screen, "White", (350 + line_length + line_gap, y_position), (350 + 2*line_length + line_gap, y_position), width = 2)
        pygame.draw.line(screen, "White", (350 + 2*(line_length + line_gap), y_position), (350 + 3*line_length + 2*line_gap, y_position), width = 2)
        pygame.draw.line(screen, "White", (350 + 3*(line_length + line_gap), y_position), (350 + 4*line_length + 3*line_gap, y_position), width = 2)
        pygame.draw.line(screen, "White", (350 + 4*(line_length + line_gap), y_position), (350 + 5*line_length + 4*line_gap, y_position), width = 2)



    ##This state renders high scores
    elif leader_boards:
        screen.fill("Black")
        screen.blit(high_score_surface, high_score_rect)

        display = 120
        for i in range(0,5):
            display_high_score(title_font, Highscore.get_high_scores()[i][0], Highscore.get_high_scores()[i][1], display)
            display+=50

    
    elif choose_character:
        screen.fill("Black")
        display_characters(characters, selected_character_index)

    elif ready_screen:

        if pygame.time.get_ticks() < timer:
            screen.fill("Black")
            screen.blit(ready_surface, ready_rect)
            intro_sample.stop()

        else:
            ready_screen = False
            game_active = True
    
    #logic to start up w starter screen
    elif not game_active and not game_over and not leader_boards and not choose_character and not ready_screen:
        screen.fill("Black")
        screen.blit(intro_title_surface, intro_title_rect)
        intro_sample.play()

    pygame.display.update()
    clock.tick(60) #should not run faster than 60fps
