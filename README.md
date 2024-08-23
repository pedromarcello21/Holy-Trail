# Holy Trail

Holy Trail is a 2D side-scrolling game where you control a character navigating through various obstacles while avoiding enemies. The game features multiple characters to choose from and includes a high score system.

## Installation

To play Holy Trail, you need to have Python installed along with the following packages:

- `pygame`
- `pygame_textinput`

You can install these packages using pip:

```bash
pip install pygame pygame_textinput
```

## How to Play

### Controls

- **Space Bar**: Navigate through different screens in the game, jump while playing.
- **Return (Enter) Key**: Select character, enter initials for high scores.
- **Tab**: Return to the title screen at any time.

### Game Flow

1. **Title Screen**: Press the Space Bar to start navigating through the game.
2. **High Scores Screen**: Press the Space Bar to move to the character selection screen.
3. **Character Selection Screen**: Use the Up and Down arrow keys to select a character. Press the Return key to confirm your selection.
4. **Ready Screen**: Wait for a few seconds before the game starts.
5. **Gameplay**: Use the Space Bar to jump and avoid enemies.
6. **Game Over Screen**: If your score is high enough, enter your initials using the Return key. Otherwise, press the Space Bar to restart.

## Game Assets

The game includes various assets such as sprites for characters and enemies, background images, and sound effects. These assets are loaded and used within the game to provide a rich and engaging experience.

## Code Overview

Here's a brief overview of the main components of the game:

- **Initialization**: Setting up the game screen, loading assets, and initializing game variables.
- **Event Handling**: Capturing user inputs to navigate through different game states and control the character.
- **Game States**: Managing different screens such as the title screen, high scores screen, character selection screen, gameplay, and game over screen.
- **Rendering**: Drawing game elements on the screen based on the current game state.
- **Collision Detection**: Checking for collisions between the character and enemies to handle game over scenarios.

## Sample Code

Here's a snippet of the main game loop to give you an idea of how the game is structured:

```python
running = True
while running:

    events = pygame.event.get()
    for event in events:
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN: 
            if not enter_initials and not ready_screen:
                if event.key == pygame.K_SPACE:
                    # Handle state transitions and jumping
                if event.key == pygame.K_RETURN:
                    # Handle character selection and initials entry
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # Handle character selection navigation
                if event.key == pygame.K_TAB:
                    # Return to title screen

    if game_active:
        # Update game state and render gameplay
    elif game_over:
        # Render game over screen
    elif enter_initials:
        # Render initials entry screen
    elif leader_boards:
        # Render high scores screen
    elif choose_character:
        # Render character selection screen
    elif ready_screen:
        # Render ready screen
    else:
        # Render title screen

    pygame.display.update()
    clock.tick(60)
```

## Conclusion

Holy Trail is a project of mine at the Flatiron school that has both showcased my passion for retro gaming and allowed me to awcknowledge my Jesuit education. By following the installation instructions and understanding the game flow, you can enjoy playing and competing for high scores. Enjoy!
