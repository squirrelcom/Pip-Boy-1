# Game for Pip-Boy
# Imports
import pygame
import random

# Initialise PyGame
pygame.init()

# Set display width and height
display_width = 500
display_height = 500

# Create a gameDisplay using display_width and display_height
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set the caption of the window to Turret Defense
pygame.display.set_caption('Tank Defense!')

# Create colours using RGB values
black = (0, 0, 0)
green = (0, 150, 0)
lightGreen = (0, 255, 0)

# Create fonts
smallFont = pygame.font.SysFont(None, 25)
mediumFont = pygame.font.SysFont(None, 50)
largeFont = pygame.font.SysFont(None, 75)

# Initialise the clock for FPS
clock = pygame.time.Clock()

# Tank part dimensions
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5

# Ground height
ground = .85 * display_height


def text_objects(text, color, size="smallFont"):  # Function returns text for blitting
    if size == "smallFont":
        textSurface = smallFont.render(text, True, color)
    if size == "mediumFont":
        textSurface = mediumFont.render(text, True, color)
    if size == "largeFont":
        textSurface = largeFont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="smallFont"):  # Blits text to button
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + buttonwidth/2), buttony + (buttonheight/2))
    gameDisplay.blit(textSurface, textRect)


def message_to_screen(msg, color, y_displace=0, size= "smallFont"):  # Blits the text returned from text_objects
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurface, textRect)


def tank(x, y, turretPosition):  # Draws the tank and turret
    # Casting x and y to be ints
    x = int(x)
    y = int(y)

    # Set possible turret positions
    turrets = [(x - 27, y - 2),
               (x - 26, y - 5),
               (x - 25, y - 8),
               (x - 23, y - 12),
               (x - 20, y - 14),
               (x - 18, y - 15),
               (x - 15, y - 17),
               (x - 13, y - 19),
               (x - 11, y - 21)]

    # Draw the tank
    pygame.draw.circle(gameDisplay, green, (int(x), int(y)), 10)
    pygame.draw.rect(gameDisplay, green, (x - tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, green, (x, y), turrets[turretPosition], turretWidth)

    pygame.draw.circle(gameDisplay, green, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 0, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 15, y + 20), wheelWidth)

    return turrets[turretPosition]


def explosion(x, y):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        magnitude = 1

        while magnitude < 50:
            explodeBitX = x + random.randrange(-1 * magnitude, magnitude)
            explodeBitY = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(gameDisplay, green, (explodeBitX, explodeBitY), random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False


def fire(pos, tanxX, tankY, turretPos, gunPower):  # Function for shooting and controlling bullet physics
    fire = True
    startingPos = list(pos)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.draw.circle(gameDisplay, green, (startingPos[0], startingPos[1]), 5)
        startingPos[0] -= (10 - turretPos)*2

        startingPos[1] += int((((startingPos[0] - pos[0]) * .01/(gunPower/50))**2) - (turretPos + turretPos / (12 -  turretPos)))

        # If the explosion is on the ground
        if startingPos[1] > ground:

            hitX = int((startingPos[0]))
            hitY = int(startingPos[1])
            explosion(hitX, hitY)

            fire = False

        pygame.display.update()
        clock.tick(100)


def power(level):
    text = smallFont.render("Power: " + str(level) + "%", True, green)
    gameDisplay.blit(text, [display_width * .8, 0])


def game_controls():  # Function for controls screen
    controls = True

    while controls:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Controls!", green, -100, size="largeFont")
        message_to_screen("Left and right arrow keys to move the tank!", green, 10, size="smallFont")
        message_to_screen("Up and down arrow keys to move the tank's turret!", green, 40, size="smallFont")
        message_to_screen("A  and D keys change the turret's power!", green, 70, size="smallFont")
        message_to_screen("P to pause the game!", green, 100, size="smallFont")

        # Buttons
        button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, colour, active_colour, action):  # Creates the button, both active and inactive
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(gameDisplay, active_colour, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()

            if action == "controls":
                game_controls()

            if action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, colour, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def pause():  # Pauses the game
    paused = True
    message_to_screen("Paused", green, -225, size="largeFont")
    message_to_screen("C to continue playing", green, -175, size="smallFont")
    message_to_screen("Q to quit", green, -150, size="smallFont")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        clock.tick(5)


def game_intro():  # Function for game introduction screen

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Tank Defense!", green, 0, size="largeFont")

        # Text on the buttons
        button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Controls", 200, 400, 100, 50, green, lightGreen, action="controls")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def gameLoop():  # Main game loop
    gameExit = False
    gameOver = False
    FPS = 15

    # Tank positioning
    mainTankX = display_width * .8
    mainTankY = display_height * .8
    tankMove = 0
    curTurretPosition = 0
    changeTurretPosition = 0

    # Fire power
    firePower = 50
    change = 0

    while not gameExit:
        if gameOver == True:
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Movement for tank
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTurretPosition = 1

                elif event.key == pygame.K_DOWN:
                    changeTurretPosition = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    fire(bullet, mainTankX, mainTankY, curTurretPosition, firePower)

                elif event.key == pygame.K_a:
                    change = -1

                elif event.key == pygame.K_d:
                    change = 1

            # If user stops pressing the button, stop moving the tank
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTurretPosition = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    change = 0

        # Draw the game screen
        mainTankX += tankMove
        gameDisplay.fill(black)
        bullet = tank(mainTankX, mainTankY, curTurretPosition)
        pygame.draw.rect(gameDisplay, green, (0, ground, display_width, ground))

        # Change power of the bullet
        firePower += change
        power(firePower)

        # Turret positioning
        curTurretPosition += changeTurretPosition
        if curTurretPosition > 8:
            curTurretPosition = 8
        elif curTurretPosition < 0:
            curTurretPosition = 0

        # Avoid tank and walls collision
        if mainTankX > display_width:
            mainTankX -= 5

        if mainTankX < 0:
            mainTankX += 5

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
