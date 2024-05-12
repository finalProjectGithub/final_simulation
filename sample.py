import threading
import pygame
import random
import time
import sys

pygame.init()
clock = pygame.time.Clock()

# Font for time
fontTimePath = 'fonts/timeFont/digital-7.ttf'
fontTimeSize = 85
fontTime = pygame.font.Font(fontTimePath, fontTimeSize)
fontTimeColor = (255, 255, 0)

# Font for title
fontTitlePath = 'fonts/titleFont/DynaPuff_Condensed-Regular.ttf'
fontTitleSize = 35
fontTitle = pygame.font.Font(fontTitlePath, fontTitleSize)
fontTitleColor = (255, 255, 255)


def sideScreenRenders():
    timeOnScreen = fontTime.render(
        timeString,
        True,
        fontTimeColor
    )
    screen.blit(timeOnScreen, (1040, 100))

    titleOnScreen1 = fontTitle.render(
        'REAL-TIME TRAFFIC',
        True,
        fontTitleColor
    )
    screen.blit(titleOnScreen1, (1035, 350))

    titleOnScreen2 = fontTitle.render(
        'ANALYSIS & STREET',
        True,
        fontTitleColor
    )
    screen.blit(titleOnScreen2, (1035, 400))

    titleOnScreen3 = fontTitle.render(
        'MANAGEMENT',
        True,
        fontTitleColor
    )
    screen.blit(titleOnScreen3, (1070, 450))

    titleOnScreen3 = fontTitle.render(
        'SYSTEM',
        True,
        fontTitleColor
    )
    screen.blit(titleOnScreen3, (1110, 500))


def randomNumberGenerator():
    maxNum = 1000
    fixedNum = 1

    while True:
        randomNum = random.randint(0, maxNum)

        if randomNum < fixedNum:
            entry = random.randint(1)


def currentTime():
    global timeString

    hours = 17
    minutes = 59
    seconds = 58

    while True:
        seconds = seconds + 1
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
            if minutes == 60:
                minutes = 0
                hours = hours + 1
                if hours == 24:
                    hours = 0
        timeString = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(timeString)
        time.sleep(1)


class Main:
    # Make the screen global so every function can access it
    global screen

    # Instantiate the current time in the simulation
    firstThread = threading.Thread(
        name="currentTime",
        target=currentTime,
        args=()
    )
    firstThread.daemon = True
    firstThread.start()

    secondThread = threading.Thread(
        name="randomNumberGenerator",
        target=randomNumberGenerator,
        args=()
    )

    # Screensize
    screenWidth = 1300
    screenHeight = 800
    screenSize = (screenWidth, screenHeight)

    # Setting background image
    background = pygame.image.load('assets/background_updated.png')

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("bruh")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill((0, 0, 0))
        screen.blit(
            background,
            (0, 0)
        )

        sideScreenRenders()

        pygame.display.update()
        clock.tick(60)
