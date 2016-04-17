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


def message_to_screen(msg, color, y_displace=0, size="smallFont"):  # Blits the text returned from text_objects

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

    # Draw the wheels
    pygame.draw.circle(gameDisplay, green, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 0, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 15, y + 20), wheelWidth)

    # Return the turret position
    return turrets[turretPosition]


def enemyTank(x, y, turretPosition):  # Draws the tank and turret

    # Casting x and y to be ints
    x = int(x)
    y = int(y)

    # Set possible turret positions
    turrets = [(x + 27, y - 2),
               (x + 26, y - 5),
               (x + 25, y - 8),
               (x + 23, y - 12),
               (x + 20, y - 14),
               (x + 18, y - 15),
               (x + 15, y - 17),
               (x + 13, y - 19),
               (x + 11, y - 21)]

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

        choices = [green, lightGreen]

        magnitude = 1

        while magnitude < 50:
            explodeBitX = x + random.randrange(-1 * magnitude, magnitude)
            explodeBitY = y + random.randrange(-1 * magnitude, magnitude)

            if explodeBitY > ground + 12:
                pygame.draw.circle(gameDisplay, black, (explodeBitX, explodeBitY), random.randrange(1, 5))

            else:
                pygame.draw.circle(gameDisplay, choices[random.randrange(0,2)], (explodeBitX, explodeBitY), random.randrange(1, 5))

            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False


def fire(pos, turretPos, gunPower, enemyTankX, enemyTankY):  # Function for shooting and controlling bullet physics

    damage = 0

    fire = True

    startingPos = list(pos)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.draw.circle(gameDisplay, green, (startingPos[0], startingPos[1]), 5)

        startingPos[0] -= (10 - turretPos)*2

        startingPos[1] += int((((startingPos[0] - pos[0]) * .015/(gunPower/50))**2) - (turretPos + turretPos / (12 -  turretPos)))

        # If the explosion is on the ground
        if startingPos[1] > ground:

            hitX = int((startingPos[0]))
            hitY = int(startingPos[1])

            # If the explosion hits the tank
            # Various damages for how close it was
            if enemyTankX + 10 > hitX > enemyTankX - 10:
                damage = 25

            elif enemyTankX + 15 > hitX > enemyTankX - 15:
                damage = 20

            elif enemyTankX + 20 > hitX > enemyTankX - 20:
                damage = 15

            elif enemyTankX + 30 > hitX > enemyTankX - 30:
                damage = 5

            explosion(hitX, hitY)

            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage


def enemyFire(pos, turretPos, gunPower, playerX, playerY):  # Function for shooting and controlling bullet physics

    damage = 0
    currentPower = 1
    powerFound = False

    # How the AI decides what power to uses
    while not powerFound:

        currentPower += 1
        if currentPower > 100:
            powerFound = True

        fire = True

        startingPos = list(pos)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            startingPos[0] += (10 - turretPos)*2

            # Make currentPower random between 80% and 120% of the chosen power
            gunPower = random.randrange(int(currentPower * .8), int(currentPower * 1.2))

            startingPos[1] += int((((startingPos[0] - pos[0]) * .015/(gunPower/50))**2) - (turretPos + turretPos / (12 - turretPos)))

            # If the explosion is on the ground
            if startingPos[1] > ground:

                hitX = int((startingPos[0]))
                hitY = int(startingPos[1])

                if playerX + 15 > hitX > playerX - 15:
                    powerFound = True

                fire = False

    fire = True
    startingPos = list(pos)

    # When the power is decided, it shoots
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.draw.circle(gameDisplay, green, (startingPos[0], startingPos[1]), 5)

        startingPos[0] += (10 - turretPos)*2

        startingPos[1] += int((((startingPos[0] - pos[0]) * .015/(gunPower/50))**2) - (turretPos + turretPos / (12 -  turretPos)))

        # If the explosion is on the ground
        if startingPos[1] > ground:

            hitX = int((startingPos[0]))
            hitY = int(startingPos[1])

            # If the explosion hits the tank
            # Various damages for how close it was
            if playerX + 10 > hitX > playerX - 10:
                damage = 25

            elif playerX + 15 > hitX > playerX - 15:
                damage = 20

            elif playerX + 20 > hitX > playerX - 20:
                damage = 15

            elif playerX + 30 > hitX > playerX - 30:
                damage = 5

            explosion(hitX, hitY)

            fire = False


        pygame.display.update()
        clock.tick(60)

    return damage


def power(level):

    text = smallFont.render("Power: " + str(level) + "%", True, green)
    gameDisplay.blit(text, [display_width * .75, 10])


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


def gameWin():  # Function for game introduction screen

    win = True

    while win:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("You won!", green, -100, size="largeFont")
        message_to_screen("Your enemy's tank was destroyed!", green, 0, size="smallFont")
        message_to_screen("Replay to replay or quit to quit!", green, 100, size="smallFont")

        # Text on the buttons
        button("Replay", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def over():  # Function for game introduction screen

    over = True

    while over:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Game over!", green, -100, size="largeFont")
        message_to_screen("Your tank was destroyed!", green, 0, size="smallFont")
        message_to_screen("Replay to replay or quit to quit!", green, 100, size="smallFont")

        # Text on the buttons
        button("Replay", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def health(playerHealth, enemyHealth, pX, eX):  # Health bars

    # Player health
    if playerHealth > 50:
        playerColour = lightGreen
    else:
        playerColour = green

    # Enemy health
    if enemyHealth > 50:
        enemyColour = lightGreen
    else:
        enemyColour = green

    # Draw the health bars
    pygame.draw.rect(gameDisplay, playerColour, (pX - 100, display_height * .7, playerHealth, 10))
    pygame.draw.rect(gameDisplay, enemyColour, (eX, display_height * .7, enemyHealth, 10))


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

    # enemyTank positioning
    enemyTankX = display_width * .2
    enemyTankY = display_height * .8
    tankMove = 0

    # Health
    playerHealth = 100
    enemyHealth = 100

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
                    damage = fire(bullet, curTurretPosition, firePower, enemyTankX, enemyTankY)
                    enemyHealth -= damage
                    damage = enemyFire(enemyBullet, 8, 33, mainTankX, mainTankY)
                    playerHealth -= damage

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
        pX = mainTankX
        eX = enemyTankX
        gameDisplay.fill(black)
        health(playerHealth, enemyHealth, pX, eX)
        bullet = tank(mainTankX, mainTankY, curTurretPosition)
        enemyBullet = enemyTank(enemyTankX, enemyTankY, 8)
        pygame.draw.rect(gameDisplay, green, (0, ground, display_width, 10))

        # Change power of the bullet
        firePower += change

        if firePower <= 1:
            firePower = 1

        if firePower >= 100:
            firePower = 100

        power(firePower)

        # Check if gameOver or gameWin
        if playerHealth < 1:
            over()

        elif enemyHealth < 1:
            gameWin()

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
