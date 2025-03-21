'''
Welcome to my game! This was a simple project I did with the goal of learning and practicing with pygame. 

With this project, I aimed to practice my skills with making a game, and using different Python libraries
with pygame. I was overall happy with the result and learned quite a bit. Reflecting upon the final product, 
I know I could have cut down on some lines of code and made it more efficient. I will work on this with
future projects. However, overall, I like the flow of the game and how everything works together to
create a fun game.

All sprites and music used used are for education purposes only and under the Copyright Disclaimer
section 107 of the Copyright Act of 1976, allowance is made for "fair use" for the purpose of 
education and research.

Author of this Code: Hector Cortez Pineda
Date that this game was made: July 2024
Author's Email: hcpineda33@gmail.com 

Enjoy! :)
'''

# Libraries imported
import pygame
import time
import sys
import math
import random
import platform
import time
from os import system

pygame.init()       # Game is initialized.

# Sprites used are all listed below for future use to blit to the game window.
bg = (pygame.image.load("bg_title.jpg"))
HUD = [pygame.image.load("pause_button.png"), pygame.image.load("easyText.png"), pygame.image.load("easyOff.png"), pygame.image.load("easyHover.png"), pygame.image.load("hardText.png"), pygame.image.load("hardOff.png"), pygame.image.load("hardHover.png")]
menu_screen = [pygame.image.load("mainmenu.jpg"), pygame.image.load("text.png"), pygame.image.load("bg100%.jpg"), pygame.image.load("main_menu_gold.png")]
title_x_o = [pygame.image.load("X_red.png"), pygame.image.load("X_blue.png"), pygame.image.load("O_green.png"), pygame.image.load("O_orange.png")]
menu_options = [pygame.image.load("neon.png"), pygame.image.load("egypt.png"), pygame.image.load("western.png"), pygame.image.load("snow.png")]
background = [pygame.image.load("neon.jpg"), pygame.image.load("egypt.jpg"), pygame.image.load("western.jpg"), pygame.image.load("snow.jpg"), pygame.image.load("bonus.jpg")]
board = [pygame.image.load("board_neon.png"), pygame.image.load("board_egypt.png"), pygame.image.load("board_west.png"), pygame.image.load("board_ice.png"), pygame.image.load("board_ice.png"), pygame.image.load("bonus_board.png")]

achieve = [pygame.image.load("achievementBlank.jpg"), pygame.image.load("achievementBlankBack.jpg"), pygame.image.load("achieveOne.png"), pygame.image.load("achieveTwo.png"), pygame.image.load("achieveThree.png"), pygame.image.load("achieveFour.png"), pygame.image.load("achieveFive.png"), pygame.image.load("achieveSix.png")]
selectA = [pygame.image.load("achievementSelectOne.jpg"), pygame.image.load("achievementSelectTwo.jpg"), pygame.image.load("achievementSelectThree.jpg"), pygame.image.load("achievementSelectFour.jpg"), pygame.image.load("achievementSelectFive.jpg"), pygame.image.load("achievementSelectSix.jpg")]
blankA = [pygame.image.load("emptyPageOne.png"), pygame.image.load("emptyPageTwo.png"), pygame.image.load("emptyPageThree.png"), pygame.image.load("emptyPageFour.png"), pygame.image.load("emptyPageFive.png"), pygame.image.load("emptyPageSix.png")]

shopOne = [pygame.image.load("shopC1.png"), pygame.image.load("shopC2.png"), pygame.image.load("shopC3.png"), pygame.image.load("shopC4.png"), pygame.image.load("shopC5.png"), pygame.image.load("shopC6.png")]
shopBought = [pygame.image.load("shopB1.png"), pygame.image.load("shopB2.png"), pygame.image.load("shopB3.png"), pygame.image.load("shopB4.png"), pygame.image.load("shopB5.png"), pygame.image.load("shopB6.png")]

rowA = [pygame.image.load("1a.png"), pygame.image.load("2a.png"), pygame.image.load("3a.png"), pygame.image.load("4a.png"), pygame.image.load("5a.png"), pygame.image.load("6a.png"),]
rowB = [pygame.image.load("1b.png"), pygame.image.load("2b.png"), pygame.image.load("3b.png"), pygame.image.load("4b.png"), pygame.image.load("5b.png"), pygame.image.load("6b.png"),]
rowC = [pygame.image.load("1c.png"), pygame.image.load("2c.png"), pygame.image.load("3c.png"), pygame.image.load("4c.png"), pygame.image.load("5c.png"), pygame.image.load("6c.png"),]

minimax = [pygame.image.load("Questbg.jpg"), pygame.image.load("minimax.png"), pygame.image.load("check.png"), pygame.image.load("prelude.jpg"), pygame.image.load("begone.png"), pygame.image.load("glhf.png"), pygame.image.load("minimax_bg.jpeg"), pygame.image.load("board_minimax.png"), pygame.image.load("max.png"), pygame.image.load("refresh.png")]
final = [pygame.image.load("won_mm.png"), pygame.image.load("lost_mm.png"), pygame.image.load("tied_mm.png")]
HUD_mm = [pygame.image.load("heart_player.png"), pygame.image.load("life_mm.png"), pygame.image.load("uhoh.png"), pygame.image.load("victoryText.png"), pygame.image.load("creditsText.png")]
postBG = [pygame.image.load("postMMBG.jpg")]
postText = [pygame.image.load("vicText1.png"), pygame.image.load("vicText2.png"), pygame.image.load("vicText3.png"), pygame.image.load("next.png"), pygame.image.load("nextR.png")]

gameX = [pygame.image.load("X_neon.png"),  pygame.image.load("X_egypt.png"), pygame.image.load("X_west.png"),  pygame.image.load("X_ice.png"), pygame.image.load("x_minimax.png"), pygame.image.load("x_bonus.png")]
gameO = [pygame.image.load("O_neon.png"), pygame.image.load("O_egypt.png"),  pygame.image.load("O_west.png"), pygame.image.load("O_ice.png"), pygame.image.load("o_minimax.png"), pygame.image.load("o_bonus.png")]

musicPlayer = [pygame.image.load("musicPlayer1.jpg"), pygame.image.load("musicPlayer2.jpg"), pygame.image.load("musicPlayer3.jpg"), pygame.image.load("musicPlayer4.jpg"),]
unknownTrack = [pygame.image.load("unknownTrackA.png"), pygame.image.load("unknownTrackB.png"), pygame.image.load("unknownTrackC.png"), pygame.image.load("unknownTrackD.png"), pygame.image.load("unknownTrackE.png")]

winText = [pygame.image.load("win_neon.png"), pygame.image.load("win_egypt.png"), pygame.image.load("win_west.png"), pygame.image.load("win_ice.png"), pygame.image.load("victory.png"), pygame.image.load("win_bonus.png")]
loseText = [pygame.image.load("lose_neon.png"), pygame.image.load("lose_egypt.png"), pygame.image.load("lose_west.png"), pygame.image.load("lose_ice.png"), pygame.image.load("lose_ice.png"), pygame.image.load("lose_bonus.png")]
tieText = pygame.image.load("tie_game.png")
pauseText = pygame.image.load("pauseText.png")


win = pygame.display.set_mode((600,600))    # Main Window Setting, with dimensions x and y.
pygame.display.set_caption("Tic Tac Toe")   # Caption for Window.

surface = pygame.Surface((600,600), pygame.SRCALPHA)    # A surface is made to create a transparent filter when this surface is called.
screen = pygame.Surface((600,600), pygame.SRCALPHA)

programIcon = pygame.image.load('icon.png')     # Changes the icon of the game application.
pygame.display.set_icon(programIcon)

checkBoard = [0,0,0,0,0,0,0,0,0]                # This represents the tic-tac-toe board. A "0" indicates an empty space, a "1" an X, and a "2" an O.

# Sound effects used throughout the game are listed below.
selectedSound = pygame.mixer.Sound('dark.wav')
spotlightSound = pygame.mixer.Sound('spotlight.wav')
trophySound = pygame.mixer.Sound("trophy.wav")
missionSound = pygame.mixer.Sound("MC.wav")
questSound = pygame.mixer.Sound("QC.wav")
refreshSound = pygame.mixer.Sound("refresh.wav")
purchaseSound = pygame.mixer.Sound("chaching.wav")
errorSound = pygame.mixer.Sound("error.wav")
godSound = pygame.mixer.Sound("godMode.wav")

# Clock is measured here for use with game FPS.
clock = pygame.time.Clock()

'''
The following variables listed below are used throughout the game, with different purposes including moving sprites,
keeping track of scores, or checking if a game checkpoint has been reached yet or not.
'''
osc = 0             # An oscilating variable makes sprites with oscilating properties move up and down according to a wave.
choice = 0          # This variable keeps track of what stage the player has chosen, or what state the game should be in, in some cases.

vertical = 0        # For vertical movement.
horizontal = 0      # For horizontal movement.

tempScore = 0       # Keeps track of a temporary score for the minimax algorithm's board.

won = False         # Checks if the game has been won by the player.
lost = False        # Checks if the game has been lost by the player.
tied = False        # Checks if the game has been tied.

paused = 0          # If this variable is "0", the game is not paused. If it is "1", the game is paused.
chose = 0           # The "hard mode" algorithm uses this variable to check for any potential wins or losses.

# The hover variables below are used to alternate between idle sprites on the menu and active sprites for added design.
hover_1 = False         # For the stages in the main menu.
hover_2 = False
hover_3 = False
hover_4 = False
hover_5 = False
hover_6 = False

hover_A = False         # For the special icons in the main menu.
hover_S = False
hover_M = False

hover_Quest = False     # For misc. buttons.
hover_Menu = False

hover_easy = False      # For the easy/hard mode buttons in the main menu.
hover_hard = False

purchase_1 = False      # For the shop options in the item shop. Checks if each item has been purchased yet or not.
purchase_2 = False
purchase_3 = False
purchase_4 = False
purchase_5 = False
purchase_6 = False

quest = False           # For the "quest" loop of the "minimax" quest to run.
quest_complete = False  # Checks if all four quest objectives have been completed or not.     
prelude = False
epilogue = False

menu = True             # For the main menu loop to run.
game = False            # For the game loop to run.
trophy = False          # For the trophy screen loop to run.
bonusLevel = False      # To check if the secret bonus level has been unlocked.
shopping = False        # For the item shop loop to run.
soundtrack = False      # For the music room loop to run.

choseEasy = True        # Checks if the player has picked easy or hard mode.
choseHard = False

var = -1                # The variables below are for the oscilating variable to move sprites up and down.
bounce = 0               
sliding = -85           
dropDown = -0.000005 * (sliding ** 4) 
rise = 500
oneTime = False

globalWon = 0           # These variables keep track of the player's score throughout the game.
globalLost = 0
globalTied = 0
money = 0
easyLosses = 0
hardWins = 0

backTruth = False       # Checks if the player has clicked the back button in the main menu.
gameComplete = False    # Checks if the player has completed the game or not.

W1 = False              # These variables are used to check if the player has won in each stage of the game.
W2 = False
W3 = False
W4 = False
W5 = False

L1 = False              # These variables are used to check if the player has lost in each stage of the game.
L2 = False
L3 = False
L4 = False
L5 = False

T1 = False              # These variables are used to check if the player has tied in each stage of the game.
T2 = False
T3 = False
T4 = False
T5 = False

postGame = False        # Checks if the player has completed the game or not.

up_pressed = False      # Used to check if the player has pressed the arrow keys for the secret code to complete the game instantly.
down_pressed = False
left_pressed = False
right_pressed = False

selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    # Used to check if the player has selected a track in the music room.
track = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       # Used to check if the player has unlocked a track in the music room.
checking = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        # Used to check if the player has completed a certain task in the game.

RGB = [255,0,0]                 # Used to change the color of the quest mark in the main menu.
minimax_check = [0,0,0,0]       # Used to check if the player has completed the minimax quest stages or not (below included)
minimaxSC = [0,0,0,0,0]

PLAYER = -1            # Used for the minimax algorithm to check if the player has won or lost.
COMP = +1              # Used for the minimax algorithm to check if the computer has won or lost.

minimaxBoard = [                        # The minimax board is created here.
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

h_choice = 'X'                          # The player's choice is set to 'X'.
c_choice = 'O'                          # The computer's choice is set to 'O'.

move = -1                               # The move variable is set to -1.
moves = {                               # The moves dictionary is created here.
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
}

center = win.get_rect().center          # The center of the game window is found here.

# The following variables are used to keep track of the player's score throughout the game.
def results_screen():

    # The global variables are called here.
    global won, lost, tied, paused, osc, hover_Play

    # If the player has won and is not in the Minimax stage, the coin sprite is blitted to the screen.
    if won and choice != 5:
        win.blit(winText[choice-1], winText[choice-1].get_rect(center = win.get_rect().center))
        win.blit(pygame.image.load("gotPaid.png"), (0,0))

    # If the player has won and is in the Minimax stage, the coin sprite is not blitted to the screen. A unique animation is played instead.
    if won and choice == 5:
        win.blit(pygame.transform.scale(winText[choice-1], (1736//4,980//4)), (78,100))

    # If the player has lost, the lose sprite is blitted to the screen.
    if lost:
        win.blit(loseText[choice-1], loseText[choice-1].get_rect(center = win.get_rect().center))
    
    # If the player has tied, the tie sprite is blitted to the screen.
    if tied:
        win.blit(tieText, tieText.get_rect(center = win.get_rect().center))

    # If the game is paused, the pause sprite is blitted to the screen.
    if paused:
        win.blit(pauseText, pauseText.get_rect(center = win.get_rect().center))

    # A rectangle is drawn to the screen to create a transparent filter.
    pygame.draw.rect(surface,(0,0,1,80),[0,0,600,600])

# The following function is used to draw the game screen.
def draw_screen():

    # The global variables are called here.
    global game

    pygame.draw.rect(surface,(245,245,245,120),[62.5,15,475,475])       # The game screen is drawn here.

    pygame.draw.rect(surface,(245,245,245,120),[62.5,505,185,75])       # The pause button is drawn here.

    pygame.draw.rect(surface,(245,245,245,120),[352.5,505,185,75])      # The quit button is drawn here.

    # If the player has chosen the Minimax stage, the minimax board is drawn to the screen.
    if choice == 5:
        pygame.draw.rect(surface,(100,100,101,120),[62.5,15,475,475])   # The minimax board is drawn here.

        pygame.draw.rect(surface,(100,100,101,120),[62.5,505,185,75])   # The pause button is drawn here.

        pygame.draw.rect(surface,(100,100,101,120),[352.5,505,185,75])  # The quit button is drawn here.

    # The screen is blitted to the game window, depending on the choice the player has made.
    if choice == 1:
        win.blit(pygame.transform.scale(board[0], (470,470)), (65,17.5))            # For the Neon stage.
    elif choice == 2:
        win.blit(pygame.transform.scale(board[1], (425,425)), (62.5+25,15+25))      # For the Egypt stage.
    elif choice == 3:
        win.blit(pygame.transform.scale(board[2], (425,425)), (62.5+25,15+25))      # For the Western stage.
    elif choice == 4:
        win.blit(pygame.transform.scale(board[3], (425,425)), (62.5+25,15+25))      # For the Ice stage.
    elif choice == 5:
        win.blit(pygame.transform.scale(minimax[7], (425,425)), (62.5+25,15+25))    # For the Minimax stage.
    elif choice == 6:
        win.blit(pygame.transform.scale(board[5], (425,425)), (62.5+25,15+25))      # For the Bonus stage.
    
    pygame.draw.circle(win, ("white"), (300,544), 40)                               # The pause button is drawn here.
    if hover_Play:
        pygame.draw.circle(win, ("black"), (300,544), 40)        # If the player hovers over the pause button, the color changes.

    if choice != 5:
        win.blit(pygame.transform.scale(HUD[0], (75,75)),(262.5,505))       # If the player is not in the Minimax stage, the pause button is blitted to the screen.
    elif choice == 5:
        win.blit(pygame.transform.scale(minimax[8], (75,75)),(262.5,505))   # If the player is in the Minimax stage, the "max" button is blitted to the screen.
    
    if choice == 5 and slippedUp == 5:
        win.blit(pygame.transform.scale(HUD_mm[2], (630//25,1668//25)), (320, 500))  # If the randomly selected number is 5, the "uh oh" sprite is blitted to the screen.

    outFont = pygame.font.SysFont("impact", 64)                     # The font for the score is set here.
    numFont = pygame.font.SysFont("impact", 58)                     
    lifeFont = pygame.font.SysFont("impact", 37)

    outPlay = outFont.render(str(scorePlayer), True, ("black"))     # The score for the player is rendered here.
    inPlay = numFont.render(str(scorePlayer), True, ("green"))
    lifeLeft = lifeFont.render(str(scorePlayer), True, ("white"))

    outCPU = outFont.render(str(scoreCPU), True, ("black"))         # The score for the computer is rendered here.
    inCPU = numFont.render(str(scoreCPU), True, ("red"))
    lifeCPU = lifeFont.render(str(scoreCPU), True, ("white"))

    if choice == 5:                                                         # If the player is in the Minimax stage, the minimax board is drawn here.
        win.blit(pygame.transform.scale(HUD_mm[0], (70, 70)), (117, 505))
        win.blit(pygame.transform.scale(HUD_mm[1], (62, 62)), (410, 510))

    if choice != 5:                                   # If the player is not in the Minimax stage, the player score is blitted to the screen.
        win.blit(outPlay, (135,503))
        win.blit(inPlay, (135,505))

    if choice != 5:                                   # If the player is not in the Minimax stage, the computer score is blitted to the screen.
        win.blit(outCPU, (425,503))
        win.blit(inCPU, (425,505))
    
    if choice == 5:                                   # If the player is in the Minimax stage, the player's "lives" are blitted to the screen.
        win.blit(lifeLeft, (133,518))
        win.blit(lifeCPU, (432,520))

# The following function is used to redraw the game window after each frame.
def redrawGameWindow():

    # The global variables are called here.
    global vertical, horizontal, mouse, CPU_Turn, hover_Play, hover_Quit, hover_Menu

    global hover_1, hover_2, hover_3, hover_4, paused, var, bounce, quest_complete, sliding, dropDown

    global clock, start, finish, savedTime

    # If the game is running, the title screen is blitted to the screen.
    if run:
        win.blit(pygame.transform.scale(bg, (650,650)), (-50,0))    # The title screen is blitted to the screen.

        pygame.draw.rect(win, (0,0,1), (170, 0, 30, 600))       # Menu Grid Bars (Vertical)
        pygame.draw.rect(win, (0,0,1), (400, 0, 30, 600))

        pygame.draw.rect(win, (0,0,1), (0, 170, 600, 30))       # Menu Grid Bars (Horizontal)
        pygame.draw.rect(win, (0,0,1), (0, 400, 600, 30))

        pygame.draw.rect(win, (0,0,255), (13, 265 + 10 * math.sin(osc), 150, 75))    # Title Screen Options
        pygame.draw.rect(win, (0,0,1), (8, 260 + 10 * math.sin(osc), 150, 75))

        # If the player hovers over the "Quit" button, the color changes.
        if hover_Quit:
            pygame.draw.rect(win, (255,0,0), (8, 260 + 10 * math.sin(osc), 150, 75))

        pygame.draw.rect(win, (0,0,255), (443, 265 + 10 * math.sin(osc), 150, 75))  # Title Screen Options
        pygame.draw.rect(win, (0,0,1), (438, 260 + 10 * math.sin(osc), 150, 75))

        # If the player hovers over the "Play" button, the color changes.
        if hover_Play:
            pygame.draw.rect(win, (0,255,0), (438, 260 + 10 * math.sin(osc), 150, 75))

        font = pygame.font.SysFont("impact", 60)                # The font for the title screen is set here.
        large_font = pygame.font.SysFont("impact", 80)

        Tic = large_font.render("Tic", True, (255,0,0))         # The text for the title screen is rendered here.
        Tac = large_font.render("Tac", True, (255,0,0))
        Toe = large_font.render("Toe", True, (255,0,0))

        Play = font.render("Play!", True, (255,255,255))        # The text for the pause and quit buttons are rendered here.
        Quit = font.render("Quit", True, (255,255,255))

        win.blit(Tic, (245 + 10 * math.sin(osc),30))            # The text for the title screen is blitted to the screen.
        win.blit(Tac, (240 + 10 * math.sin(-1* osc),250))
        win.blit(Toe, (240 + 10 * math.sin(osc),470))

        win.blit(Play, (450,260 + 10 * math.sin(osc)))          # The text for the pause and quit buttons are blitted to the screen.
        win.blit(Quit, (30,260 + 10 * math.sin(osc)))

        win.blit(title_x_o[0], (50 + 10 * math.sin(osc),20 + 10 * math.sin(osc)))   # The title effect sprites are blitted to the screen.
        win.blit(title_x_o[3], (50 + 10 * math.sin(osc),450 + 10 * math.sin(-osc)))
        win.blit(title_x_o[2], (475 + 10 * math.sin(-osc),20 + 10 * math.sin(osc)))
        win.blit(title_x_o[1], (475 + 10 * math.sin(-osc),450 + 10 * math.sin(-osc)))

        # If the player backed out from the main menu to the title screen, the apporpiate achievement is blitted to the screen.
        if backTruth and checking[11] == 0:

            dropDown = -0.000005 * (sliding ** 4)

            win.blit(pygame.image.load("D3.png"), (0, 25 + int(dropDown)))

            if int(dropDown) == -2 and sliding < 0:
                trophySound.play()

            sliding += 1.8

            if sliding > 100:
                checking[11] = 1

    # If not on the title screen, the main menu is blitted to the screen.
    elif menu:

        # The normal main menu is blitted to the screen.
        if not gameComplete:
            win.blit(pygame.transform.scale(menu_screen[0], (600,600)), (0,0))
            win.blit(pygame.transform.scale(menu_screen[1],(400,100)), (100,30+10*math.sin(osc)))
        # The 100% completion main menu is blitted to the screen, if the player has completed the game 100%.
        elif gameComplete:
            win.blit(pygame.transform.scale(menu_screen[2], (600,600)), (0,0))
            win.blit(pygame.transform.scale(menu_screen[3],(400,100)), (100,30+10*math.sin(osc)))

        # The main menu options are blitted to the screen.
        pygame.draw.rect(win, (255,255,255), (100,150+10*math.sin(osc),400,75))
        pygame.draw.rect(win, (0,0,1), (95,145+10*math.sin(osc),400,75))

        # If the player hovers over the "Play" button, the color changes.
        if hover_1:
            pygame.draw.rect(win, (161,5,245), (95,145+10*math.sin(osc),400,75))

        # The "Play" button is blitted to the screen.
        win.blit(pygame.transform.scale(menu_options[0], (518/1.25, 130/1.25)), (90,130+10*math.sin(osc)))

        # The main menu options are blitted to the screen.
        pygame.draw.rect(win, (255,255,255), (100,250+10*math.sin(osc),400,75))
        pygame.draw.rect(win, (0,0,1), (95,245+10*math.sin(osc),400,75))

        # If the player hovers over the second stage option and has purchased the second stage, the color changes.
        if hover_2 and purchase_1:
            pygame.draw.rect(win, (227,223,102), (95,245+10*math.sin(osc),400,75))
        elif hover_2 and not purchase_1:
            pygame.draw.rect(win, (13,59,94), (95,245+10*math.sin(osc),400,75))

        # If purchased, the second stage option is blitted to the screen, if not, the locked sprite is blitted to the screen.
        if purchase_1:
            win.blit(pygame.transform.scale(menu_options[1], (518/1.35, 130/1.35)), (100,235+10*math.sin(osc)))
        elif not purchase_1:
            win.blit(pygame.image.load("locked.png"), (265, 245+10*math.sin(osc)))

        pygame.draw.rect(win, (255,255,255), (100,350+10*math.sin(osc),400,75))
        pygame.draw.rect(win, (0,0,1), (95,345+10*math.sin(osc),400,75))

        # If the player hovers over the third stage option and has purchased the third stage, the color changes.
        if hover_3 and purchase_2:
            pygame.draw.rect(win, (173,116,10), (95,345+10*math.sin(osc),400,75))
        elif hover_3 and not purchase_2:
            pygame.draw.rect(win, (13,59,94), (95,345+10*math.sin(osc),400,75))

        # If purchased, the third stage option is blitted to the screen, if not, the locked sprite is blitted to the screen.
        if purchase_2:
            win.blit(pygame.transform.scale(menu_options[2], (518/1.35, 130/2.15)), (100,350+10*math.sin(osc)))
        elif not purchase_2:
            win.blit(pygame.image.load("locked.png"), (265, 345+10*math.sin(osc)))

        pygame.draw.rect(win, (255,255,255), (100,450+10*math.sin(osc),400,75))
        pygame.draw.rect(win, (0,0,1), (95,445+10*math.sin(osc),400,75))

        # If the player hovers over the fourth stage option and has purchased the fourth stage, the color changes.
        if hover_4 and purchase_3:    
            pygame.draw.rect(win, (9,60,135), (95,445+10*math.sin(osc),400,75))
        elif hover_4 and not purchase_3:
            pygame.draw.rect(win, (13,59,94), (95,445+10*math.sin(osc),400,75))

        # If purchased, the fourth stage option is blitted to the screen, if not, the locked sprite is blitted to the screen.
        if purchase_3:
            win.blit(pygame.transform.scale(menu_options[3], (518/1.45, 130/2)), (120,450+10*math.sin(osc)))
        elif not purchase_3:
            win.blit(pygame.image.load("locked.png"), (265, 445+10*math.sin(osc)))

        # If the bonus level has been unlocked, the bonus level option is blitted to the screen.
        if bonusLevel:

            # Calls the RGB_Cycle function to change the color of the bonus level option in a rainbow pattern.
            RGB_Cycle()

            # The bonus level option is blitted to the screen in the form of a circle.
            pygame.draw.circle(win, (RGB[0], RGB[1], RGB[2]), (555, 450), 25)
            pygame.draw.circle(win, (0,0,1), (555, 450), 20)

            # If the player hovers over the bonus level option, the color changes.
            if hover_S:
                pygame.draw.circle(win, (54,194,54), (555, 450), 20)

        menuFont = pygame.font.SysFont("impact", 55)                    # The font for the main menu is set here.
        smallmenuFont = pygame.font.SysFont("impact", 35)

        backArrow = menuFont.render("←", True, (255,255,255))           # The back arrow sprite is rendered here.
        quitX = menuFont.render("x", True, (255,255,255))               # The quit "x" sprite is rendered here.
        questMark = smallmenuFont.render("?", True, (255,255,255))      # The question mark sprite is rendered here.
        special = smallmenuFont.render("S", True, (255,255,255))        # The special icon sprite is rendered here.

        musicNote = smallmenuFont.render("♫", True, (255,255,255))      # The music note sprite is rendered here.
        star = smallmenuFont.render("♦", True, (255,255,255))           # The star sprite is rendered here.
        dollar = smallmenuFont.render("$", True, (255,255,255))         # The dollar sign sprite is rendered here.

        var += 0.05                     # The oscilating variable is increased by 0.05.
        bounce = -100*var**2 + 101      # The bounce variable is calculated here.

        if var > 1:                     # If the oscilating variable is greater than 1, the oscilating variable is reset to -1.
            var = -1

        # The main menu sprites for the shop, music room, and achievements are blitted to the screen.
        pygame.draw.circle(win, (0,0,255), (50, 50), 35)
        pygame.draw.circle(win, (0,0,1), (50, 50), 30)

        pygame.draw.circle(win, (0,0,255), (550, 50), 35)
        pygame.draw.circle(win, (0,0,1), (550, 50), 30)

        pygame.draw.circle(win, ("gold"), (50, 555), 25)
        pygame.draw.circle(win, (0,0,1), (50, 555), 20)

        pygame.draw.circle(win, ("teal"), (50, 475), 25)
        pygame.draw.circle(win, (0,0,1), (50, 475), 20)

        pygame.draw.circle(win, ("white"), (50, 395), 25)
        pygame.draw.circle(win, (0,0,1), (50, 395), 20)

        # If the player hovers over the shop, music room, or achievements options, the color changes.
        if hover_A:
            pygame.draw.circle(win, ("silver"), (50, 555), 20)
        
        if hover_5:
            pygame.draw.circle(win, ("green"), (50, 475), 20)
        
        if hover_M:
            pygame.draw.circle(win, (194,118,31), (50, 395), 20)

        # If the player has purchased the minimax quests, the question mark is blitted to the screen.
        if purchase_4:
            if quest_complete and not bonusLevel:
                pygame.draw.circle(win, (0,0,255), (555, 555-int(bounce)), 25)
                pygame.draw.circle(win, (0,0,1), (555, 555-int(bounce)), 20)
            elif not quest_complete:
                pygame.draw.circle(win, (0,0,255), (555, 555), 25)
                pygame.draw.circle(win, (0,0,1), (555, 555), 20)
            elif quest_complete and bonusLevel:
                pygame.draw.circle(win, (0,0,255), (555, 555), 25)
                pygame.draw.circle(win, (0,0,1), (555, 555), 20)
        
        # The back arrow and quit "x" sprites are blitted to the screen.
        if hover_Menu:
            pygame.draw.circle(win, (230,255,3), (50, 50), 30)

        if hover_Quit:
            pygame.draw.circle(win, (255,0,0), (550, 50), 30)
        
        # If the player is hovering over the minimax quests option, the color changes. Otherwise, it remains the same.
        if purchase_4:
            if hover_Quest and quest_complete and not bonusLevel:
                pygame.draw.circle(win, (RGB[0],RGB[1],RGB[2]), (555, 555-int(bounce)), 20)
            elif hover_Quest and not quest_complete:
                pygame.draw.circle(win, (RGB[0],RGB[1],RGB[2]), (555, 555), 20)
            elif hover_Quest and quest_complete and bonusLevel:
                pygame.draw.circle(win, ("orange"), (555, 555), 20)

        # The back arrow and quit "x" sprites are blitted to the screen.
        win.blit(backArrow, (23, 10))
        win.blit(quitX, (538, 10))

        # The question mark and special icon sprites are blitted to the screen.
        if purchase_4:
            if quest_complete and not bonusLevel:
                win.blit(questMark, (547,532-int(bounce)))
            elif not quest_complete:
                win.blit(questMark, (547,532))
            elif quest_complete and bonusLevel:
                win.blit(questMark, (547,532))

        # If the bonus level has been unlocked, the special icon is blitted to the screen.
        if bonusLevel:
            win.blit(special, (546,428))
        
        RGB_Cycle()     # Calls the RGB_Cycle function for reference.

        if choseEasy:
            win.blit(pygame.transform.scale(HUD[1], (279//2.1, 175//2.1)), (150,525))   # If the player has chosen easy mode, the green easy mode sprite is blitted to the screen.
        
        if not choseEasy:
            win.blit(pygame.transform.scale(HUD[2], (279//2.1, 175//2.1)), (150,525))   # If the player has not chosen easy mode, the black easy mode sprite is blitted to the screen.
        
        if not choseEasy and hover_easy:
            win.blit(pygame.transform.scale(HUD[3], (279//2.1, 175//2.1)), (150,525))   # If the player hovers over the easy mode button, the outlined easy mode sprite is blitted to the screen.
        
        if choseHard:
            win.blit(pygame.transform.scale(HUD[4], (316//2.1, 175//2.1)), (300,525))   # If the player has chosen hard mode, the red hard mode sprite is blitted to the screen.

        if not choseHard:
            win.blit(pygame.transform.scale(HUD[5], (316//2.1, 175//2.1)), (300,525))   # If the player has not chosen hard mode, the black hard mode sprite is blitted to the screen.
        
        if not choseHard and hover_hard:
            win.blit(pygame.transform.scale(HUD[6], (316//2.1, 175//2.1)), (300,525))   # If the player hovers over the hard mode button, the outlined hard mode sprite is blitted to the screen.

        win.blit(musicNote, (36.5,370.5))   # The music note sprite is blitted to the screen.    
        win.blit(dollar, (41,453))          # The dollar sign sprite is blitted to the screen.
        win.blit(star, (39,530))            # The star sprite is blitted to the screen.
        
        if quest_complete and minimaxSC[4] == 0:            # If the player has completed the minimax quests, the question mark sprite has a bouncing animation and is blitted to the screen.

            dropDown = -0.000005 * (sliding ** 4)

            win.blit(pygame.image.load("QC.png"), (0, 25 + int(dropDown)))

            if int(dropDown) == -261 and sliding < 0:
                questSound.play()

            sliding += 1.5

            if sliding < 175:
                pygame.mixer.music.pause()
            elif sliding > 175:
                pygame.mixer.music.unpause()
                minimaxSC[4] = 1

    elif game:                                      # If not on the title or main menu screen, the game screen is blitted to the screen.

        if choice == 1:                             # If the player chooses the Neon stage, the Neon stage background is blitted to the screen.
            win.blit(background[0], (0,0))
        elif choice == 2:                           # If the player chooses the Egypt stage, the Egypt stage background is blitted to the screen.
            win.blit(pygame.transform.scale(background[1], (650,650)), (0,0))
        elif choice == 3:                           # If the player chooses the Western stage, the Western stage background is blitted to the screen.
            win.blit(pygame.transform.scale(background[2], (1150,650)), (-150,0))
        elif choice == 4:                           # If the player chooses the Ice stage, the Ice stage background is blitted to the screen.
            win.blit(pygame.transform.scale(background[3], (650,650)),(0,0))
        elif choice == 5:                           # If the player chooses the Minimax stage, the Minimax stage background is blitted to the screen.
            win.blit(pygame.transform.scale(minimax[6], (600,600)), (0,0))
        elif choice == 6:                           # If the player chooses the Bonus stage, the Bonus stage background is blitted to the screen.
            win.blit(background[4],(0,0))

        win.blit(surface, (0,0))                    # The game screen is blitted to the screen.
        draw_screen()                               # The draw_screen function is called here.
        
        if checkBoard[0] == 1:                      # If the player has placed an "X" on the first square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (100,60))
        elif checkBoard[0] == 2:                    # If the computer has placed an "O" on the first square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (100,60))

        if checkBoard[1] == 1:                      # If the player has placed an "X" on the second square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (235,60))
        elif checkBoard[1] == 2:                    # If the computer has placed an "O" on the second square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (235,60))

        if checkBoard[2] == 1:                      # If the player has placed an "X" on the third square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (390,60))
        elif checkBoard[2] == 2:                    # If the computer has placed an "O" on the third square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (390,60))

        if checkBoard[3] == 1:                      # If the player has placed an "X" on the fourth square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (100,200))
        elif checkBoard[3] == 2:                    # If the computer has placed an "O" on the fourth square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (100,200))

        if checkBoard[4] == 1:                      # If the player has placed an "X" on the fifth square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (235,200))
        elif checkBoard[4] == 2:                    # If the computer has placed an "O" on the fifth square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (235,200))

        if checkBoard[5] == 1:                      # If the player has placed an "X" on the sixth square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (390,200))
        elif checkBoard[5] == 2:                    # If the computer has placed an "O" on the sixth square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (390,200))

        if checkBoard[6] == 1:                      # If the player has placed an "X" on the seventh square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (100,350))
        elif checkBoard[6] == 2:                    # If the computer has placed an "O" on the seventh square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (100,350))

        if checkBoard[7] == 1:                      # If the player has placed an "X" on the eighth square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (235,350))
        elif checkBoard[7] == 2:                    # If the computer has placed an "O" on the eighth square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (235,350))

        if checkBoard[8] == 1:                      # If the player has placed an "X" on the ninth square, the "X" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameX[choice-1], (100,110)), (390,350))
        elif checkBoard[8] == 2:                    # If the computer has placed an "O" on the ninth square, the "O" sprite is blitted to the screen.
            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (390,350))
    
        if minimax_check[1] == 1 and minimaxSC[1] == 0:      # If the player has completed the second minimax quest, the "M2" sprite is blitted to the screen.

            dropDown = -0.000005 * (sliding ** 4)

            win.blit(pygame.image.load("M2.png"), (0, 25 + int(dropDown)))

            if int(dropDown) == -2 and sliding < 0:
                godSound.play()

            sliding += 1

            if sliding > 150:
                minimaxSC[1] = 1

    if won or lost or tied or paused:                   # If the game is won, lost, tied, or paused, the apporpiate sprites are blitted to the screen.

        # The global variables are called here.
        global scorePlayer, scoreCPU, rise

        if choice == 5 and game and scoreCPU == 1:      # If the player is in the Minimax stage and the computer has won, the "lost" sprite is blitted to the screen.
            dropDown = -0.000005 * (sliding ** 4)
            sliding += 1

            if sliding > -1 and sliding < 11:           # If the player has lost, the "lost" sprite is blitted to the screen.
                win.blit(pygame.transform.scale(minimax[9], (425,425)), (62.5+25,15+25))
                if int(sliding) > -4 and int(sliding) < 0:
                    refreshSound.play()                 # The refresh sound is played here.
                for i in range(0,9):                    # The checkBoard is reset to 0 for all squares.
                    checkBoard[i] = 0

            if int(sliding) > -7 and int(sliding) < -5 and not won:
                refreshSound.play()

            if tied:                                    # If the game is tied, the "tied" sprite is blitted to the screen.
                win.blit(final[2], (150, 200 + int(dropDown)))

            if lost:                                    # If the player has lost, the "lost" sprite is blitted to the screen.
                win.blit(final[1], (150, 200 + int(dropDown)))

            if int(sliding) > -7 and int(sliding) < -5:     # To keep track of the score.
                if won:
                    scoreCPU += -1
                if lost:
                    scorePlayer += -1

            if int(sliding) > 84:                           # Control value.    
                sliding = -85

        if choice == 5 and game and scoreCPU > 1:           # If the player is in the Minimax stage and the computer has won, the "lost" sprite is blitted to the screen.

            dropDown = -0.000005 * (sliding ** 4)           # For oscilations.

            if sliding > -1 and sliding < 11:
                win.blit(pygame.transform.scale(minimax[9], (425,425)), (62.5+25,15+25))
                if int(sliding) > -4 and int(sliding) < 0:
                    refreshSound.play()
                for i in range(0,9):
                    checkBoard[i] = 0

            if tied:
                win.blit(final[2], (150, 200 + int(dropDown)))      # If the game is tied, the "tied" sprite is blitted to the screen.

            if lost:
                win.blit(final[1], (150, 200 + int(dropDown)))      # If the player has lost, the "lost" sprite is blitted to the screen.
            
            if won:
                win.blit(pygame.transform.scale(final[0], (712//1.5, 177//1.5)), (62.5, 240 + int(dropDown)))       # If the player has won, the "won" sprite is blitted to the screen.
            
            sliding += 1            # For oscilations.

            if int(sliding) > -7 and int(sliding) < -5:     # To keep track of the score.
                refreshSound.play()
                if lost:
                    scorePlayer += -1
                if won:
                    scoreCPU += -1

            if int(sliding) > 84:    # Control value.
                sliding = -85

        if choice == 5 and won and scoreCPU == 0:       
            pass

        if choice != 5:                    # If the player is not in the Minimax stage, the apporpiate sprites are blitted to the screen.
            font = pygame.font.SysFont("impact", 60)                    # The font for the game screen is set here.
            bigFont = pygame.font.SysFont("impact", 90)

            Rematch = font.render("Rematch!", True, (255,255,255))      # The "Rematch" text is rendered here.
            Resume = font.render("Resume", True, (255,255,255))         # The "Resume" text is rendered here.

            backArrow = bigFont.render("←", True, (255,255,255))        # The back arrow sprite is rendered here.
            quitX = bigFont.render("x", True, (255,255,255))            # The quit "x" sprite is rendered here.

            pygame.draw.rect(win, (0,0,255), (145, 405, 310, 110))      # The "Rematch" button is blitted to the screen.
            pygame.draw.rect(win, (0,0,1), (150, 410, 300, 100))        # The "Rematch" button is outlined.

            pygame.draw.circle(win, (0,0,255), (75, 75), 55)            # The back arrow sprite is blitted to the screen.
            pygame.draw.circle(win, (0,0,1), (75, 75), 50)              # The back arrow sprite is outlined.

            pygame.draw.circle(win, (0,0,255), (525, 75), 55)           # The quit "x" sprite is blitted to the screen.
            pygame.draw.circle(win, (0,0,1), (525, 75), 50)             

            if hover_Play:                                              # If the player hovers over the "Rematch" button, the color changes.
                pygame.draw.rect(win, (0,255,0), (150, 400 + 10, 300, 100))
            
            if hover_Menu:                                              # If the player hovers over the back arrow, the color changes.
                pygame.draw.circle(win, (230,255,3), (75, 75), 50)

            if hover_Quit:                                              # If the player hovers over the quit "x" sprite, the color changes.
                pygame.draw.circle(win, (255,0,0), (525, 75), 50)

            if not paused:                                              # If the game is over, the "Rematch" text is blitted to the screen.
                win.blit(Rematch, (185, 425))

            if paused:                                                  # If the game is paused, the "Resume" text is blitted to the screen.
                win.blit(Resume, (200, 425))

            win.blit(backArrow, (30, 10))                               # The back arrow sprite is blitted to the screen.
            win.blit(quitX, (505, 15))                                  # The quit "x" sprite is blitted to the screen.

        if choice != 5:                                                 # If the player is not in the Minimax stage, the apporpiate sprites are blitted to the screen.
            if globalWon == 1 and checking[0] == 0:                     # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("A1.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7
            
            if globalLost == 1 and checking[1] == 0:                    # For achievements.    

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("A2.png"), (0, 25 + int(dropDown)))    # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalTied == 1 and checking[2] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("A3.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalWon == 5 and checking[3] == 0:                     # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("B1.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalLost == 5 and checking[4] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("B2.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalTied == 5 and checking[5] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("B3.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalWon == 10 and checking[6] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("C1.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalLost == 10 and checking[7] == 0:                   # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("C2.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if globalTied == 10 and checking[8] == 0:                   # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("C3.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if easyLosses == 3 and checking[9] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("D1.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if hardWins == 10 and checking[10] == 0:                    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("D2.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if W1 and W2 and W3 and W4 and W5 and checking[15] == 0:    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("F1.png"), (0, 25 + int(dropDown)))    # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7 

            if L1 and L2 and L3 and L4 and L5 and checking[16] == 0:    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("F2.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if T1 and T2 and T3 and T4 and T5 and checking[17] == 0:    # For achievements.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("F3.png"), (0, 25 + int(dropDown)))      # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    trophySound.play()
                
                if oneDraw < 1:                                         # Control value.
                    sliding += 0.7

            if minimax_check[0] == 1 and minimaxSC[0] == 0:             # For Minimax Quest tracking.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("M1.png"), (0, 25 + int(dropDown)))    # Achievement sprite is blitted to the screen.
            
                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    godSound.play()

                if oneDraw < 1:                                         # Control value.
                    sliding += 0.5

                if sliding > 150:                                       # Also a control value.
                    minimaxSC[0] = 1

            if minimax_check[2] == 1 and minimaxSC[2] == 0:             # For Minimax Quest tracking.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("M3.png"), (0, 25 + int(dropDown)))  # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    godSound.play()

                if oneDraw < 1:                                         # Control value.
                    sliding += 0.5

                if sliding > 150:                                       # Also a control value.                    
                    minimaxSC[2] = 1

            if minimax_check[3] == 1 and minimaxSC[3] == 0:             # For Minimax Quest tracking.

                if not oneTime and sliding < 100:                       # Achievement sprite is animated.
                    win.blit(screencopy, (0,0))

                dropDown = -0.000005 * (sliding ** 4)                   # For oscilations.

                win.blit(pygame.image.load("M4.png"), (0, 25 + int(dropDown)))  # Achievement sprite is blitted to the screen.

                if int(dropDown) == -2 and sliding < 0:                 # If the sprite has reached the bottom, the trophy sound is played.
                    godSound.play()

                if oneDraw < 1:                                         # Control value.
                    sliding += 0.5

                if sliding > 150:                                       # Also a control value.
                    minimaxSC[3] = 1

    pygame.display.update()                                             # The display is updated here.

# To get the "x" position on the board that the CPU chose.
def getCoordinate_x(CPU):

    if CPU == 0 or 3 or 6:
        return 100              # The value is returned as 100 to pinpoint where on the x axis the "O" sprite will be blitted.
    
    if CPU == 1 or 4 or 7:
        return 235              # Same with 235.
    
    if CPU == 2 or 5 or 8:
        return 390              # Same with 390.

# To get the "y" position on the board that the CPU chose.
def getCoordinate_y(CPU):

    if CPU == 0 or 1 or 2:
        return 60               # The value is returned as 60 to pinpoint where on the y axis the "O" sprite will be blitted.
    
    if CPU == 3 or 4 or 5:
        return 200              # Same with 200.
    
    if CPU == 6 or 7 or 8:
        return 350              # Same with 350.

# To determine how many spaces are left on the board.
def MovesLeft():

    if checkBoard.count(0) != 0:
        return False            # If there are no spaces left on the board, the function returns False.
    
    return True                 # If there are spaces left on the board, the function returns True.

# Analytically keeps track of the game board based on player and CPU moves (easy mode).
def game_board():

    # The global variables are called here.
    global CPU_Turn, tied

    CPU = random.randint(0,8)       # The CPU chooses a random number between 0 and 8 on easy mode.

    count = 0                       # If the CPU has made 20 moves (sanity check) and the game is not won, the game is tied.

    while not tied:                 # While the game is not tied, the game board is analyzed.

        if won:                     # If the game is won, the loop is broken.
            break

        if checkBoard[CPU] == 0:    # If the CPU has not placed an "O" on the board, the CPU places an "O" on the board.

            x_coor = getCoordinate_x(CPU)       # The x coordinate is determined here.
            y_coor = getCoordinate_y(CPU)       # The y coordinate is determined here.

            win.blit(pygame.transform.scale(gameO[choice-1], (100,110)), (x_coor, y_coor))      # The "O" sprite is blitted to the screen.
            CPU_Turn = False                                                                    # The CPU's turn is over.
            checkBoard[CPU] = 2                                                                 # The CPU's move is recorded on the checkBoard.
            break                                                                               # The loop is broken.

        elif checkBoard[CPU] == 1 or 2:         # If the CPU or the player has placed an "X" or "O" on the board, the CPU chooses another random number between 0 and 8 (easy mode)
            CPU = random.randint(0,8)           # and the process is repeated.
            count += 1                          # The count is incremented by 1.

            if won == True:                     # If the game is won, the loop is broken.
                break
            elif count == 20 and won == False:  # If the CPU has made 20 moves (sanity check) and the game is not won, the game is tied.
                tied = True

# Analytically keeps track of the game board based on player and CPU moves (hard mode).
def tough_board():
    
    # The global variables are called here.
    global CPU_Turn, tied, checkBoard

    chose = 0               # The variable chose is set to 0.

    testBoard = [0,0,0,0,0,0,0,0,0]     # The testBoard is initialized here.

    for i in range(0,9):                    # The game board is analyzed here.

        for j in range(0,9):                
            grabVal = checkBoard[j]         # The value of the checkBoard is stored in grabVal.
            testBoard[j] = grabVal          # The value of grabVal is stored in the testBoard.

        if testBoard[i] == 0:               # If the testBoard is empty, the CPU places an "O" on the board.
            testBoard[i] = 2                # The CPU's move is recorded on the testBoard.

        # If the CPU wins on the testBoard, the best move is recorded to be used on the actual board.
        if testBoard[0] == 2 and testBoard[1] == 2 and testBoard[2] == 2:    # Row 1
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
    
        if testBoard[3] == 2 and testBoard[4] == 2 and testBoard[5] == 2:    # Row 2
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[6] == 2 and testBoard[7] == 2 and testBoard[8] == 2:    # Row 3
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[0] == 2 and testBoard[3] == 2 and testBoard[6] == 2:    # Column 1
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[1] == 2 and testBoard[4] == 2 and testBoard[7] == 2:    # Column 2
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[2] == 2 and testBoard[5] == 2 and testBoard[8] == 2:    # Column 3
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[0] == 2 and testBoard[4] == 2 and testBoard[8] == 2:    # Diagonal 1
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.
        
        if testBoard[2] == 2 and testBoard[4] == 2 and testBoard[6] == 2:    # Diagonal 2
            chose = 1                       # The variable chose is set to 1.
            CPU_Turn = False                # The CPU's test turn is over.
            break                           # The loop is broken.

        if chose == 0 and testBoard[i] == 2:    # If the CPU has not won on the testBoard, the process is repeated.
            testBoard[i] = 0

    if chose == 1:                          # If the CPU has won on the testBoard, the best move is recorded on the checkBoard.
        checkBoard[i] = 2
    elif chose == 0:                        # If the CPU has not won on the testBoard, the process is repeated.
        for i in range(0,9):

            # **See above code, as the processs is the same but with different variables.**
            for j in range(0,9):
                grabVal = checkBoard[j]
                testBoard[j] = grabVal

            if testBoard[i] == 0:
                testBoard[i] = 1

            if testBoard[0] == 1 and testBoard[1] == 1 and testBoard[2] == 1:    # Row 1
                chose = 1
                CPU_Turn = False
                break
        
            if testBoard[3] == 1 and testBoard[4] == 1 and testBoard[5] == 1:    # Row 2
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[6] == 1 and testBoard[7] == 1 and testBoard[8] == 1:    # Row 3
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[0] == 1 and testBoard[3] == 1 and testBoard[6] == 1:    # Column 1
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[1] == 1 and testBoard[4] == 1 and testBoard[7] == 1:    # Column 2
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[2] == 1 and testBoard[5] == 1 and testBoard[8] == 1:    # Column 3
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[0] == 1 and testBoard[4] == 1 and testBoard[8] == 1:    # Diagonal 1
                chose = 1
                CPU_Turn = False
                break
            
            if testBoard[2] == 1 and testBoard[4] == 1 and testBoard[6] == 1:    # Diagonal 2
                chose = 1
                CPU_Turn = False
                break
            
            if chose == 0 and testBoard[i] == 2:
                testBoard[i] = 0

    if chose == 1:
        checkBoard[i] = 2       # If the CPU has won on the testBoard, the best move is recorded on the checkBoard.
    
    if CPU_Turn:
        game_board()            # The CPU's choice is recorded on the actual game board.
    
    CPU_Turn = False            # The CPU's turn is over.

# This function converts the CPU's choice into coordinates to determine where to blit the "O" sprite.
def check_to_2D(converting, x, y):

    # The global variables are called here.
    global checkBoard

    if converting:              # If the CPU's choice is being converted into coordinates, the following code is executed.

        if x == 0 and y == 0 and checkBoard[0] == 0:
            checkBoard[0] = 2
        
        if x == 0 and y == 1 and checkBoard[1] == 0:
            checkBoard[1] = 2

        if x == 0 and y == 2 and checkBoard[2] == 0:
            checkBoard[2] = 2
        
        if x == 1 and y == 0 and checkBoard[3] == 0:
            checkBoard[3] = 2
        
        if x == 1 and y == 1 and checkBoard[4] == 0:
            checkBoard[4] = 2
        
        if x == 1 and y == 2 and checkBoard[5] == 0:
            checkBoard[5] = 2
        
        if x == 2 and y == 0 and checkBoard[6] == 0:
            checkBoard[6] = 2
        
        if x == 2 and y == 1 and checkBoard[7] == 0:
            checkBoard[7] = 2
        
        if x == 2 and y == 2 and checkBoard[8] == 0:
            checkBoard[8] = 2

        return


'''
The following functions used for the Minimax algorithm were not made by me, but adapted from someone on GitHub. Their
information is listed below:

Author's Name: Jan Andersson
Code URL: https://github.com/GreenVortex/CollegeProjects/blob/6686e5f1dc41a414a36bb939bae2eef303857a22/Tic%20tac%20toe/main.py
Date Accessed: 07/15/2024

Thank you :)
'''

'''Borrowed Code Begins Here.'''
# Evaluates the heuristic value of current branch.
def evaluation(state):

    if wins(state, COMP):
        score = +1
    elif wins(state, PLAYER):
        score = -1
    else:
        score = 0
    
    return score

def wins(state, player):       # A matrix of all the possible win states.

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):           # The function checks the game state and returns if the game is over.
    return wins(state, PLAYER) or wins(state, COMP)

def empty_cells(state):         # Creates an array of empty cells and returns them.

    cells = []

    for x, rows in enumerate(state):
        for y, cell in enumerate(rows):
            if cell == 0:
                cells.append([x, y])
    
    return cells

def valid_move(x, y):

    # Returns true or false depending on the move.
    if [x, y] in empty_cells(minimaxBoard):
        return True
    else:
        return False
    
def set_move(x, y, player):
    # redraw board with move if move is correct

    if valid_move(x, y):
        minimaxBoard[x][y] = player
        return True
    else:
        return False

def minimax_picks(state, depth, player):
    # AI function that chooses the best best next move based on the current state of the board
    # Searches all the nodes in the tree and chooses the best outcome

    if player == COMP:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if depth == 0 or game_over(state):
        score = evaluation(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax_picks(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

'''Borrowed Code Ends Here.'''

def hell_board(c_choice, h_choice):
    # The function is used to determine the CPU's move based on the Minimax algorithm.

    # The global variables are called here.
    global CPU_Turn

    for i in range(0,3):                # The game board is analyzed here.
        for j in range(0,3):
            minimaxBoard[i][j] = checkBoard [j+(3*i)]

            if minimaxBoard[i][j] == 1:     # The player's move is recorded on the minimaxBoard.
                minimaxBoard[i][j] = -1

            if minimaxBoard[i][j] == 2:     # The CPU's move is recorded on the minimaxBoard.
                minimaxBoard[i][j] = +1

    depth = len(empty_cells(minimaxBoard))  # The depth of the Minimax algorithm is determined here.
    if depth == 0 or game_over(minimaxBoard):
        return

    move = minimax_picks(minimaxBoard, depth, COMP) # The CPU's move is determined here.
    x, y = move[0], move[1]                         # The CPU's move is stored in x and y.

    converting = True                               # The CPU's move is converted into coordinates here.

    set_move(x, y, COMP)                            # The CPU's move is set on the board.

    check_to_2D(converting, x, y)                   # The CPU's move is converted into coordinates.

    converting = False
    CPU_Turn = False                                # The CPU's turn is over.

'''Some borrowed code from above is here.'''
def human_turn(c_choice, h_choice):
    # The Human plays choosing a valid move.

    global x, y
    
    depth = len(empty_cells(minimaxBoard))
    if depth == 0 or game_over(minimaxBoard):
        return
    
    # Dictionary of valid moves
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    coord = moves[move]
    can_move = set_move(coord[0], coord[1], PLAYER)

def winCheck():
    # The function checks if the player has won the game.

    # The global variables are called here.
    global won
     
    if checkBoard[0] == 1 and checkBoard[1] == 1 and checkBoard[2] == 1:    # Row 1
        redrawGameWindow()
        won = True
    
    if checkBoard[3] == 1 and checkBoard[4] == 1 and checkBoard[5] == 1:    # Row 2
        redrawGameWindow()
        won = True
    
    if checkBoard[6] == 1 and checkBoard[7] == 1 and checkBoard[8] == 1:    # Row 3
        redrawGameWindow()
        won = True

    if checkBoard[0] == 1 and checkBoard[3] == 1 and checkBoard[6] == 1:    # Column 1
        redrawGameWindow()
        won = True
    
    if checkBoard[1] == 1 and checkBoard[4] == 1 and checkBoard[7] == 1:    # Column 2
        redrawGameWindow()
        won = True
    
    if checkBoard[2] == 1 and checkBoard[5] == 1 and checkBoard[8] == 1:    # Column 3
        redrawGameWindow()
        won = True
    
    if checkBoard[0] == 1 and checkBoard[4] == 1 and checkBoard[8] == 1:    # Diagonal 1
        redrawGameWindow()
        won = True
    
    if checkBoard[2] == 1 and checkBoard[4] == 1 and checkBoard[6] == 1:    # Diagonal 2
        redrawGameWindow()
        won = True

def loseCheck():
    # The function checks if the CPU has won the game.

    # The global variables are called here.
    global lost

    if checkBoard[0] == 2 and checkBoard[1] == 2 and checkBoard[2] == 2:    # Row 1
        redrawGameWindow()
        lost = True
    
    if checkBoard[3] == 2 and checkBoard[4] == 2 and checkBoard[5] == 2:    # Row 2
        redrawGameWindow()
        lost = True
    
    if checkBoard[6] == 2 and checkBoard[7] == 2 and checkBoard[8] == 2:    # Row 3
        redrawGameWindow()
        lost = True
    
    if checkBoard[0] == 2 and checkBoard[3] == 2 and checkBoard[6] == 2:    # Column 1
        redrawGameWindow()
        lost = True
    
    if checkBoard[1] == 2 and checkBoard[4] == 2 and checkBoard[7] == 2:    # Column 2
        redrawGameWindow()
        lost = True
    
    if checkBoard[2] == 2 and checkBoard[5] == 2 and checkBoard[8] == 2:    # Column 3
        redrawGameWindow()
        lost = True
    
    if checkBoard[0] == 2 and checkBoard[4] == 2 and checkBoard[8] == 2:    # Diagonal 1
        redrawGameWindow()
        lost = True
    
    if checkBoard[2] == 2 and checkBoard[4] == 2 and checkBoard[6] == 2:    # Diagonal 2
        redrawGameWindow()
        lost = True

def tieCheck():
    # The function checks if the game is tied.

    # The global variables are called here.
    global tied

    if checkBoard.count(0) == 0:
        tied = True
            
def clearBoard():
    # The function clears the game board.

    # The global variables are called here.
    global checkBoard, turn, tied

    refreshing = True           # The refreshing variable is set to True, to refresh the screen.

    sliding = -85                           # For the oscilations.
    dropDown = -0.000005 * (sliding ** 4) 

    while refreshing:           # While the screen is refreshing, the following code is executed.

        dropDown = -0.000005 * (sliding ** 4)

        for event in pygame.event.get():        # Safety loop.
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)

        sliding += 1            # Control value.

        redrawGameWindow()      # The game window is redrawn.

        pygame.display.update() # and updated.

        if sliding > 85:        # If the screen has refreshed, the refreshing variable is set to False.
            refreshing = False
            break

def RGB_Cycle():
    # The function cycles through the RGB values to create a rainbow effect.

    if RGB[0] == 255 and RGB[1] < 255 and RGB[2] == 0:
        while RGB[0] == 255:
            RGB[1] += 1
            
            if RGB[1] == 256:
                break
        
            return RGB
    elif RGB[0] <= 255 and RGB[0] > 0 and RGB[1] == 255 and RGB[2] == 0:
        while RGB[1] == 255:
            RGB[0] += -1
            
            if RGB[0] == -1:
                break
        
            return RGB
    elif RGB[0] == 0 and RGB[1] == 255 and RGB[2] < 255:
        while RGB[1] == 255:
            RGB[2] += 1
            
            if RGB[2] == 256:
                break
        
            return RGB
    elif RGB[0] == 0 and RGB[1] <= 255 and RGB[1] > 0 and RGB[2] == 255:
        while RGB[2] == 255:
            RGB[1] += -1
            
            if RGB[1] == -1:
                break
        
            return RGB
    elif RGB[0] < 255 and RGB[1] == 0 and RGB[2] == 255:
        while RGB[2] == 255:
            RGB[0] += 1
            
            if RGB[0] == 256:
                break
        
            return RGB
    elif RGB[0] == 255 and RGB[1] == 0 and RGB[2] <= 255 and RGB[2] > 0:
        while RGB[0] == 255:
            RGB[2] += -1
            
            if RGB[2] == -1:
                break
        
            return RGB

def transparent_filter():
    # The function creates a transparent filter for the post game screen.

    postBG[0].set_alpha(transparency)

    postText[0].set_alpha(transparentText1)
    postText[1].set_alpha(transparentText2)
    postText[2].set_alpha(transparentText3)

    win.blit(postBG[0], (0,0))

    if transparency > 120:
        win.blit(pygame.transform.scale(postText[0], (573, 110)), (14, 245))
        win.blit(pygame.transform.scale(postText[1], (557, 314)), (22, 143))
        win.blit(pygame.transform.scale(postText[2], (539, 137)), (31, 232))
        # win.blit(postText[3], (50,400))
        # win.blit(postText[4], (50,500))

def completeCheck():
    # The function checks if the player has completed the game.

    if globalWon >= 10 and globalLost >= 10 and globalTied >= 10:       # Criteria for completion.
        if easyLosses >= 3 and hardWins >= 10 and backTruth:
            if purchase_1 and purchase_2 and purchase_3 and purchase_4 and purchase_5 and purchase_6:
                if bonusLevel:
                    if W1 and W2 and W3 and W4 and W5:
                        if L1 and L2 and L3 and L4 and L5:
                            if T1 and T2 and T3 and T4 and T5:
                                return True
    
    return False

def grantAll():
    # The function grants the player all the achievements if the player presses the correct "secret" keys.

    global globalWon, globalLost, globalTied, easyLosses, hardWins, backTruth
    global purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6 
    global bonusLevel, W1, W2, W3, W4, W5, L1, L2, L3, L4, L5, T1, T2, T3, T4, T5
    global postGame, selected, track, checking, minimax_check, minimaxSC, gameComplete
    global bonusLevel, money

    money = 99

    globalWon = 99
    globalLost = 99
    globalTied = 99
    easyLosses = 99
    hardWins = 99

    purchase_1 = True
    purchase_2 = True
    purchase_3 = True
    purchase_4 = True
    purchase_5 = True
    purchase_6 = True

    W1 = True
    W2 = True
    W3 = True
    W4 = True
    W5 = True

    L1 = True
    L2 = True
    L3 = True
    L4 = True
    L5 = True

    T1 = True
    T2 = True
    T3 = True
    T4 = True
    T5 = True

    bonusLevel = True

    selected = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    track = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    checking = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    minimax_check = [1,1,1,1]
    minimaxSC = [1,1,1,1,1]

    gameComplete = True
    
    godSound.play()

transparency = 2            # For the transparent filter.
transparentText1 = 0
transparentText2 = 0
transparentText3 = 0

major = True
while major:                # The main loop of the game.

    music = pygame.mixer.music.load('title.mp3')        # The music is loaded here.
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    sliding = -85                                       # For the oscilations.

    run = True                                          # The run variable is set to True, to run the game.
    if choice == 15:
        run = False
            
    if choice == 5:
        run = False
    while run:                                          # The title screen loop.

        clock.tick(30)  # The game's FPS (Frames Per Second).

        keys = pygame.key.get_pressed()                 # The keys pressed on the keyboard are recorded here. 

        mouse = pygame.mouse.get_pos()                  # The mouse's position is recorded here.

        hover_Quit = False                              # For hovering effects (changing colour)
        hover_Play = False

        for event in pygame.event.get():                # The event loop is executed here.
            if event.type == pygame.QUIT:               # If the player closes the game window, the game is exited.
                run = False
                pygame.display.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:            # Secret keys to grant all achievements.
                if event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_UP:
                    up_pressed = True
                if event.key == pygame.K_DOWN and up_pressed:
                    down_pressed = True
                if event.key == pygame.K_LEFT and up_pressed and down_pressed:
                    left_pressed = True
                if event.key == pygame.K_RIGHT and up_pressed and down_pressed and left_pressed:
                    right_pressed = True
                    grantAll()

        # The following code is executed if the player hovers over the "Quit" button.
        if mouse[0] > 8 and mouse[0] < 8 + 150 and mouse[1] > 260 + 10 * math.sin(osc) and mouse[1] < 260 + 10 * math.sin(osc) + 75:
            hover_Quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit(0)

        # The following code is executed if the player hovers over the "Play" button.
        if mouse[0] > 438 and mouse[0] < 438 + 150 and mouse[1] > 260 + 10 * math.sin(osc) and mouse[1] < 260 + 10 * math.sin(osc) + 75:
            hover_Play = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

        osc += 0.05     # Oscilations for the buttons.

        redrawGameWindow()          # The game window is redrawn.
    
    music = pygame.mixer.music.load('menu_ttt.mp3')     # The music is loaded here.
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

    osc = 0             # Oscilations for the buttons.

    if completeCheck() == True:         # If the player has completed the game, the post game screen is displayed.
        gameComplete = True

    if gameComplete:                    # If the game is complete, the 100% completion music is played.
        music = pygame.mixer.music.load('completeBG.mp3')
        pygame.mixer.music.play(-1)

    delay = 0                           # Control value.
    menu = True                         # The menu variable is set to True, to display the Main Menu.
    if choice == 5:                     
        menu = False
    while menu:                         # The Main Menu loop.

        clock.tick(30)                  # The game's FPS (Frames Per Second).

        # Causes a delay whenever the game goes back to the Main Menu.
        if delay == 0:
            time.sleep(0.5)
            delay = 1

        mouse = pygame.mouse.get_pos()  # The mouse's position is recorded here.

        redrawGameWindow()              # The game window is redrawn.    
    
        hover_1 = False                 # For hovering effects (changing colour)
        hover_2 = False
        hover_3 = False
        hover_4 = False
        hover_S = False

        hover_5 = False                 
        hover_M = False

        hover_Menu = False
        hover_Quit = False

        quest = False
        hover_Quest = False

        hover_A = False
        accomplish = False

        hover_easy = False
        hover_hard = False

        for event in pygame.event.get():            # The event loop is executed here.
            if event.type == pygame.QUIT:           # If the player closes the game window, the game is exited.
                menu  = False
                major = False
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)

        # The following code is executed if the player hovers over the "Music Room" button.
        if mouse[0] > 30 and mouse[0] < 70 and mouse[1] > 375 and mouse[1] < 415:       
            hover_M = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                soundtrack = True

        # The following code is executed if the player hovers over the "Achievements" button.
        if mouse[0] > 30 and mouse[0] < 70 and mouse[1] > 535 and mouse[1] < 575:
            hover_A = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                accomplish = True

        # The following code is executed if the player hovers over the "Quest" button.
        if mouse[0] > 30 and mouse[0] < 75 and mouse[1] > 455 and mouse[1] < 495:
            hover_5 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                shopping = True

        # The following code is executed if the player hovers over the Neon stage button.
        if mouse[0] > 95 and mouse[0] < 95 + 400 and mouse[1] > 145 + 10 * math.sin(osc) and mouse[1] < 145 + 10 * math.sin(osc) + 75:
            hover_1 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                choice = 1
                menu = False
        
        # The following code is executed if the player hovers over the Egypt stage button.
        if mouse[0] > 95 and mouse[0] < 95 + 400 and mouse[1] > 245 + 10 * math.sin(osc) and mouse[1] < 245 + 10 * math.sin(osc) + 75:
            hover_2 = True
            if event.type == pygame.MOUSEBUTTONDOWN and purchase_1:
                choice = 2
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not purchase_1:
                errorSound.play()

        # The following code is executed if the player hovers over the Western stage button.
        if mouse[0] > 95 and mouse[0] < 95 + 400 and mouse[1] > 345 + 10 * math.sin(osc) and mouse[1] < 345 + 10 * math.sin(osc) + 75:
            hover_3 = True
            if event.type == pygame.MOUSEBUTTONDOWN and purchase_2:
                choice = 3
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not purchase_2:
                errorSound.play()

        # The following code is executed if the player hovers over the Ice stage button.
        if mouse[0] > 95 and mouse[0] < 95 + 400 and mouse[1] > 445 + 10 * math.sin(osc) and mouse[1] < 445 + 10 * math.sin(osc) + 75:
            hover_4 = True
            if event.type == pygame.MOUSEBUTTONDOWN and purchase_3:
                choice = 4
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not purchase_3:
                errorSound.play()
        
        # The following code is executed if the player hovers over the "Back" button.
        if mouse[0] > 20 and mouse[0] < 80 and mouse[1] > 20 and mouse[1] < 80:
            hover_Menu = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = False
                backTruth = True
                choice = 10
        
        # The following code is executed if the player hovers over the "Quit" button.
        if mouse[0] > 520 and mouse[0] < 580 and mouse[1] > 20 and mouse[1] < 80:
            hover_Quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit(0)

        # The following code is executed if the player hovers over the "Quest" button.
        if quest_complete and not bonusLevel and purchase_4:
            if mouse[0] > 535 and mouse[0] < 575 and mouse[1] > 535 -int(bounce) and mouse[1] < 575 -int(bounce):
                hover_Quest = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quest = True
        
        # The following code is executed if the player hovers over the Special stage button.
        if bonusLevel:
            if mouse[0] > 535 and mouse[0] < 575 and mouse[1] > 425 and mouse[1] < 475:
                hover_S = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    choice = 6
                    menu = False

        # To take the player to the quest screen.
        if not quest_complete and purchase_4:
            if mouse[0] > 535 and mouse[0] < 575 and mouse[1] > 535 and mouse[1] < 575:
                hover_Quest = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quest = True
        
        # To take the player to the quest screen, post game.
        if quest_complete and bonusLevel:
            if mouse[0] > 535 and mouse[0] < 575 and mouse[1] > 535 and mouse[1] < 575:
                hover_Quest = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quest = True

        # To set the game to easy mode.   
        if mouse[0] > 150 and mouse[0] < 150 + 279//2.1 and mouse[1] > 525 and mouse[1] < 525 + 175 //2.1:
            hover_easy = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                choseEasy = True
                choseHard = False
        
        # To set the game to hard mode.
        if mouse[0] > 300 and mouse[0] < 300 + 316//2.1 and mouse[1] > 525 and mouse[1] < 525 + 175 //2.1:
            hover_hard = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                choseHard = True
                choseEasy = False
        
        osc += 0.05     # Oscilations for the buttons.

        # The following code is executed if the player clicks on the Quest button.
        if quest:
            music = pygame.mixer.music.load('tictacquestoe.mp3')
            pygame.mixer.music.play(-1)

            pygame.mixer.music.set_volume(0.5)

            move_1 = -600
            move_2 = -1500

            track[4] = 1
        while quest:        # The Quest loop.

            mouse = pygame.mouse.get_pos()      # The mouse's position is recorded here.

            RGB_Cycle()                         # The RGB values are cycled here.

            hover_Menu = False                  # For hovering effects (changing colour)

            win.blit(minimax[0], (0, move_1))   # The minimax quest background is displayed here.
            win.blit(minimax[1], (move_2, 15))

            questFont = pygame.font.SysFont("impact", 34)       # The font is set here.

            for event in pygame.event.get():    # The event loop is executed here: if the player exits the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)

            go_back = questFont.render("Let the Quest Begin!", True, ("white"))     # The text is rendered here.
            finishedQuest = questFont.render("Quest Completed!", True, ("white"))

            pygame.draw.rect(win, (0,0,1), (100,520 - 3 * move_2, 60, 60), 10, border_radius=1)     # The buttons are drawn here.
            pygame.draw.rect(win, (0,0,1), (220,520 - 3 * move_2, 60, 60), 10, border_radius=1)
            pygame.draw.rect(win, (0,0,1), (340,520 - 3 * move_2, 60, 60), 10, border_radius=1)
            pygame.draw.rect(win, (0,0,1), (460,520 - 3 * move_2, 60, 60), 10, border_radius=1)
        
            if move_2 >= 3 and bonusLevel:                              # The back button is drawn here.
                win.blit(pygame.image.load("backShop.png"), (0,0))

            if mouse[0] > 0 and mouse[0] < 110 and mouse[1] > 0 and mouse[1] < 71 and bonusLevel and move_2 >= 3:   # Hovering effects.
                win.blit(pygame.image.load("backShopC.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(0.3)
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.6)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)
                    quest = False

            if mouse[0] > 155 and mouse[0] < 445 and mouse[1] > 20 + 2 * move_2 and mouse[1] < 100 + 2 * move_2:    # Hovering effects.
                hover_Menu = True
                if event.type == pygame.MOUSEBUTTONDOWN and not quest_complete:
                    quest = False
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)

            pygame.draw.rect(win, ("black"), (150, 20 + 2 * move_2, 300 ,80))       # The buttons are drawn here.
            pygame.draw.rect(win, ("gold"), (155, 25 + 2 * move_2, 290 ,70))
            if hover_Menu:
                pygame.draw.rect(win, (0,255,0), (155, 25 + 2 * move_2, 290 ,70))
            if hover_Menu and quest_complete:
                pygame.draw.rect(win, (0,0,1), (150, 20 + 2 * move_2, 300 ,80))
                pygame.draw.rect(win, (RGB[0],RGB[1],RGB[2]), (155, 25 + 2 * move_2, 290 ,70))

            if not quest_complete:                                                  # The text is rendered here.
                win.blit(go_back, (162, 35 + 2 * move_2))
            elif quest_complete:
                win.blit(finishedQuest, (175, 35 + 2 * move_2))

            move_1 += 2                 # The movement values are incremented here for oscilations.
            move_2 += 2.5

            if move_1 >= 0:
                move_1 = 0
            
            if move_2 >= 3:
                move_2 = 3
            
            # These if statements check for the player's progress in the quests.
            if minimax_check[0] == 1:
                win.blit(pygame.transform.scale(minimax[2], (320//5, 304//5)), (110, 510 - 3 * move_2))

            if minimax_check[1] == 1:
                win.blit(pygame.transform.scale(minimax[2], (320//5, 304//5)), (230, 510 - 3 * move_2))

            if minimax_check[2] == 1:
                win.blit(pygame.transform.scale(minimax[2], (320//5, 304//5)), (350, 510 - 3 * move_2))

            if minimax_check[3] == 1:
                win.blit(pygame.transform.scale(minimax[2], (320//5, 304//5)), (470, 510 - 3 * move_2))
            
            # For the hovering effects.
            if mouse[0] > 155 and mouse[0] < 445 and mouse[1] > 20 + 2 * move_2 and mouse[1] < 100 + 2 * move_2:
                hover_Menu = True
                if event.type == pygame.MOUSEBUTTONDOWN and quest_complete and not bonusLevel:  
                    selectedSound.play()                                         
                    minimaxPrelude = True
                    quest = False
                    menu = False
                    choice = 99
                elif event.type == pygame.MOUSEBUTTONDOWN and quest_complete and bonusLevel:  
                    time.sleep(0.3)
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.6)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)
                    quest = False

            pygame.display.update()         # The game window is updated.

        # The following code is executed if the player clicks on the "Achievements" button.
        if accomplish:
            music = pygame.mixer.music.load('achievements.mp3')
            pygame.mixer.music.play(-1)
            hover_1 = True
            hover_2 = False
            hover_3 = False
            hover_4 = False
            hover_5 = False
            hover_6 = False
            track[3] = 1
        while accomplish:                   # The Achievements loop.

            if completeCheck() == True:     # If the player has completed the game, the post game effects are displayed.
                gameComplete = True

            mouse = pygame.mouse.get_pos()  # The mouse's position is recorded here.

            hover_Menu = False              # For hovering effects (changing colour)

            for event in pygame.event.get():    # The event loop is executed here: if the player exits the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)
            
            # The following code is executed if the player hovers over the "1" button.
            if hover_1:
                win.blit(selectA[0], (0,0))
                win.blit(blankA[0], (0,0))

                if globalWon >= 1:
                    win.blit(rowA[0], (0,0))
                
                if globalLost >= 1:
                    win.blit(rowB[0], (0,0))

                if globalTied >= 1:
                    win.blit(rowC[0], (0,0))
            elif hover_2:       # The following code is executed if the player hovers over the "2" button.
                win.blit(selectA[1], (0,0))
                win.blit(blankA[1], (0,0))

                if globalWon >= 5:
                    win.blit(rowA[1], (0,0))
                
                if globalLost >= 5:
                    win.blit(rowB[1], (0,0))

                if globalTied >= 5:
                    win.blit(rowC[1], (0,0))
            elif hover_3:      # The following code is executed if the player hovers over the "3" button.
                win.blit(selectA[2], (0,0))
                win.blit(blankA[2], (0,0))

                if globalWon >= 10:
                    win.blit(rowA[2], (0,0))
                
                if globalLost >= 10:
                    win.blit(rowB[2], (0,0))

                if globalTied >= 10:
                    win.blit(rowC[2], (0,0))
            elif hover_4:       # The following code is executed if the player hovers over the "4" button.
                win.blit(selectA[3], (0,0))
                win.blit(blankA[3], (0,0))

                if easyLosses >= 3:
                    win.blit(rowA[3], (0,0))
                
                if hardWins >= 10:
                    win.blit(rowB[3], (0,0))

                if backTruth:
                    win.blit(rowC[3], (0,0))
            elif hover_5:      # The following code is executed if the player hovers over the "5" button.
                win.blit(selectA[4], (0,0))
                win.blit(blankA[4], (0,0))

                if purchase_6:
                    win.blit(rowA[4], (0,0))

                if purchase_1 and purchase_2 and purchase_3 and purchase_4 and purchase_5 and purchase_6:
                    win.blit(rowB[4], (0,0))

                if bonusLevel:
                    win.blit(rowC[4], (0,0))
            elif hover_6:       # The following code is executed if the player hovers over the "6" button.
                win.blit(selectA[5], (0,0))
                win.blit(blankA[5], (0,0))

                if W1 and W2 and W3 and W4 and W5:
                    win.blit(rowA[5], (0,0))
                
                if L1 and L2 and L3 and L4 and L5:
                    win.blit(rowB[5], (0,0))
                
                if T1 and T2 and T3 and T4 and T5:
                    win.blit(rowC[5], (0,0))

            # The following code is executed if the player hovers over the "Back" button.
            if mouse[0] > 0 and mouse[0] < 71 and mouse[1] > 0 and mouse[1] < 71:
                win.blit(pygame.image.load("backAcheive.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(0.3)
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)
                    accomplish = False
            
            # The following code is executed if the player hovers over the "1" button.
            if mouse[0] > 93 and mouse[0] < 93 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_1:
                win.blit(achieve[2], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = True
                    hover_2 = False
                    hover_3 = False
                    hover_4 = False
                    hover_5 = False
                    hover_6 = False
            
            # The following code is executed if the player hovers over the "2" button.
            if mouse[0] > 158 and mouse[0] < 158 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_2:
                win.blit(achieve[3], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = True
                    hover_3 = False
                    hover_4 = False
                    hover_5 = False
                    hover_6 = False
            
            # The following code is executed if the player hovers over the "3" button.
            if mouse[0] > 229 and mouse[0] < 229 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_3:
                win.blit(achieve[4], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = True
                    hover_4 = False
                    hover_5 = False
                    hover_6 = False
            
            # The following code is executed if the player hovers over the "4" button.
            if mouse[0] > 300 and mouse[0] < 300 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_4:
                win.blit(achieve[5], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = False
                    hover_4 = True
                    hover_5 = False
                    hover_6 = False

            # The following code is executed if the player hovers over the "5" button.
            if mouse[0] > 365 and mouse[0] < 365 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_5:
                win.blit(achieve[6], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = False
                    hover_4 = False
                    hover_5 = True
                    hover_6 = False
            
            # The following code is executed if the player hovers over the "6" button.
            if mouse[0] > 436 and mouse[0] < 436 + 71 and mouse[1] > 510 and mouse[1] < 510 + 71 and not hover_6:
                win.blit(achieve[7], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = False
                    hover_4 = False
                    hover_5 = False
                    hover_6 = True

            # If the game is complete, the 100% completion badge is displayed.
            if gameComplete:
                win.blit(pygame.image.load("completeBadge.png"), (0,0))
                    
            pygame.display.update()     # The game window is updated.

        # The following code is executed if the player clicks on the "Shop" button.
        if shopping:
            music = pygame.mixer.music.load('shop.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
            track[2] = 1
            sliding = -85
        while shopping:             # The Shop loop.

            if completeCheck() == True:         # If the player has completed the game, the post game effects are displayed.
                gameComplete = True

            mouse = pygame.mouse.get_pos()      # The mouse's position is recorded here.

            hover_Menu = False                  # For hovering effects (changing colour)

            moneyFont = pygame.font.SysFont("impact", 50)       # The font is set here.
            moneyTotal = moneyFont.render(str(money), True, (255,255,255))

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)

            win.blit(pygame.image.load("shop.jpg"), (0,0))      # The shop background is displayed here.
            win.blit(pygame.image.load("backShop.png"), (0,0))

            # The following code is executed if the player hovers over the "Back" button.
            if mouse[0] > 0 and mouse[0] < 110 and mouse[1] > 0 and mouse[1] < 71:  
                win.blit(pygame.image.load("backShopC.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(0.3)
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.6)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)
                    shopping = False

            # The following code is executed if the player has enough coins to purchase the first item.
            if mouse[0] > 92 and mouse[0] < 295 and mouse[1] > 214 and mouse[1] < 298:
                win.blit(shopOne[0], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_1 and money >= 2:
                        purchaseSound.play()
                        money += -2
                        purchase_1 = True
                    elif not purchase_1 and money < 2:
                        errorSound.play()
            
            # The following code is executed if the player has enough coins to purchase the second item.
            if mouse[0] > 305 and mouse[0] < 505 and mouse[1] > 214 and mouse[1] < 298:
                win.blit(shopOne[1], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_2 and money >= 2:
                        purchaseSound.play()
                        money += -2
                        purchase_2 = True
                    elif not purchase_2 and money < 2:
                        errorSound.play()
            
            # The following code is executed if the player has enough coins to purchase the third item.
            if mouse[0] > 92 and mouse[0] < 295 and mouse[1] > 305 and mouse[1] < 390:
                win.blit(shopOne[2], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_3 and money >= 2:
                        purchaseSound.play()
                        money += -2
                        purchase_3 = True
                    elif not purchase_3 and money < 2:
                        errorSound.play()
            
            # The following code is executed if the player has enough coins to purchase the fourth item.
            if mouse[0] > 305 and mouse[0] < 505 and mouse[1] > 305 and mouse[1] < 390:
                win.blit(shopOne[3], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_4 and money >= 5:
                        purchaseSound.play()
                        money += -5
                        purchase_4 = True
                    elif not purchase_4 and money < 5:
                        errorSound.play()

            # The following code is executed if the player has enough coins to purchase the fifth item.
            if mouse[0] > 92 and mouse[0] < 295 and mouse[1] > 395 and mouse[1] < 480:
                win.blit(shopOne[4], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_5 and money >= 8:
                        purchaseSound.play()
                        money += -8
                        purchase_5 = True
                    elif not purchase_5 and money < 8:
                        errorSound.play()
            
            # The following code is executed if the player has enough coins to purchase the sixth item.
            if mouse[0] > 305 and mouse[0] < 505 and mouse[1] > 395 and mouse[1] < 480:
                win.blit(shopOne[5], (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not purchase_6 and money >= 10:
                        purchaseSound.play()
                        money += -10
                        purchase_6 = True
                    elif not purchase_6 and money < 10:
                        errorSound.play()
            
            win.blit(moneyTotal, (350,525))     # The total money is displayed here.

            # The following code is executed if the player has purchased the first item.
            if purchase_1:
                win.blit(shopBought[0], (0,0))
                win.blit(pygame.image.load("purchased.png"), (200, 225))
            
            # The following code is executed if the player has purchased the second item.
            if purchase_2:
                win.blit(shopBought[1], (0,0))
                win.blit(pygame.image.load("purchased.png"), (400, 225))

            # The following code is executed if the player has purchased the third item.
            if purchase_3:
                win.blit(shopBought[2], (0,0))
                win.blit(pygame.image.load("purchased.png"), (200, 315))

            # The following code is executed if the player has purchased the fourth item.
            if purchase_4:
                win.blit(shopBought[3], (0,0))
                win.blit(pygame.image.load("purchased.png"), (400, 315))
            
            # The following code is executed if the player has purchased the fifth item.
            if purchase_5:
                win.blit(shopBought[4], (0,0))
                win.blit(pygame.image.load("purchased.png"), (200, 410))
                track[18] = 1
            
            # The following code is executed if the player has purchased the sixth item.
            if purchase_6:
                win.blit(shopBought[5], (0,0))
                win.blit(pygame.image.load("purchased.png"), (400, 410))

            # For an achievement effect.
            if purchase_6 and checking[12] == 0:

                dropDown = -0.000005 * (sliding ** 4)

                win.blit(pygame.image.load("E1.png"), (0, 25 + int(dropDown)))

                if int(dropDown) == -2 and sliding < 0:
                    trophySound.play()

                sliding += 2.2

                if sliding > 100:
                    checking[12] = 1
                    sliding = -85
            elif purchase_1 and purchase_2 and purchase_3 and purchase_4 and purchase_5 and purchase_6 and checking[13] == 0:
                # For an achievement effect again.

                dropDown = -0.000005 * (sliding ** 4)

                win.blit(pygame.image.load("E2.png"), (0, 25 + int(dropDown)))

                if int(dropDown) == -3 and sliding < 0:
                    trophySound.play()

                sliding += 3

                if sliding > 100:
                    checking[13] = 1
                    sliding = -85

            pygame.display.update()     # The game window is updated.

        # The following code is executed if the player clicks on the "Music Player" button.
        if soundtrack:
            pygame.mixer.music.stop()
            hover_1 = True
            hover_2 = False
            hover_3 = False
            hover_4 = False
            playing = False
            selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        while soundtrack:           # The Music Player loop.

            if completeCheck() == True:     # If the player has completed the game, the post game effects are displayed.
                gameComplete = True

            if gameComplete:                # If the game is complete, the complete background music is unlocked.
                track[19] = 1

            mouse = pygame.mouse.get_pos()  # The mouse's position is recorded here.

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            
            # For the hovering effects.
            if hover_1:
                win.blit(musicPlayer[0], (0,0))
            elif hover_2:
                win.blit(musicPlayer[1], (0,0))
            elif hover_3:
                win.blit(musicPlayer[2], (0,0))
            elif hover_4:
                win.blit(musicPlayer[3], (0,0))
            
            win.blit(pygame.image.load("backShop.png"), (0,0))  # The back arrow is blitted onto the screen.

            # The following code is executed if the player hovers over the "Back" button.
            if mouse[0] > 0 and mouse[0] < 110 and mouse[1] > 0 and mouse[1] < 71:
                win.blit(pygame.image.load("backShopC.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(0.3)
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.6)
                    if gameComplete:
                        music = pygame.mixer.music.load('completeBG.mp3')
                        pygame.mixer.music.play(-1)
                    soundtrack = False

            # The following code is executed if the player hovers over the "1" button.
            if mouse[0] > 140 and mouse[0] < 170 and mouse[1] > 550 and mouse[1] < 588 and not hover_1:
                win.blit(pygame.image.load("musicHover1.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = True
                    hover_2 = False
                    hover_3 = False
                    hover_4 = False
            
            # The following code is executed if the player hovers over the "2" button.
            if mouse[0] > 235 and mouse[0] < 275 and mouse[1] > 550 and mouse[1] < 588 and not hover_2:
                win.blit(pygame.image.load("musicHover2.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = True
                    hover_3 = False
                    hover_4 = False
            
            # The following code is executed if the player hovers over the "3" button.
            if mouse[0] > 335 and mouse[0] < 370 and mouse[1] > 550 and mouse[1] < 588 and not hover_3:
                win.blit(pygame.image.load("musicHover3.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = True
                    hover_4 = False
            
            # The following code is executed if the player hovers over the "4" button.
            if mouse[0] > 430 and mouse[0] < 470 and mouse[1] > 550 and mouse[1] < 588 and not hover_4:
                win.blit(pygame.image.load("musicHover4.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover_1 = False
                    hover_2 = False
                    hover_3 = False
                    hover_4 = True
            
            # If music is playing, the play button is displayed.
            if playing:
                win.blit(pygame.image.load("freePlaying.png"), (0,0))
            
            # To determine which track is going to be played, from here:
            if hover_1:
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 74 and mouse[1] < 132 and track[0] == 1:
                    pygame.draw.rect(win, ("orange"), (80,70, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 155 and mouse[1] < 215 and track[1] == 1:
                    pygame.draw.rect(win, ("orange"), (80,151, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 240 and mouse[1] < 300 and track[2] == 1:
                    pygame.draw.rect(win, ("orange"), (80,236, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 325 and mouse[1] < 385 and track[3] == 1:
                    pygame.draw.rect(win, ("orange"), (80,321, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 405 and mouse[1] < 465 and track[4] == 1:
                    pygame.draw.rect(win, ("orange"), (80,401, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
            if hover_2:
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 74 and mouse[1] < 132 and track[5] == 1:
                    pygame.draw.rect(win, ("orange"), (80,70, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 155 and mouse[1] < 215 and track[6] == 1:
                    pygame.draw.rect(win, ("orange"), (80,151, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 240 and mouse[1] < 300 and track[7] == 1:
                    pygame.draw.rect(win, ("orange"), (80,236, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 325 and mouse[1] < 385 and track[8] == 1:
                    pygame.draw.rect(win, ("orange"), (80,321, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 405 and mouse[1] < 465 and track[9] == 1:
                    pygame.draw.rect(win, ("orange"), (80,401, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
            
            if hover_3:
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 74 and mouse[1] < 132 and track[10] == 1:
                    pygame.draw.rect(win, ("orange"), (80,70, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 155 and mouse[1] < 215 and track[11] == 1:
                    pygame.draw.rect(win, ("orange"), (80,151, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 240 and mouse[1] < 300 and track[12] == 1:
                    pygame.draw.rect(win, ("orange"), (80,236, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 325 and mouse[1] < 385 and track[13] == 1:
                    pygame.draw.rect(win, ("orange"), (80,321, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 405 and mouse[1] < 465 and track[14] == 1:
                    pygame.draw.rect(win, ("orange"), (80,401, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

            if hover_4:
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 74 and mouse[1] < 132 and track[15] == 1:
                    pygame.draw.rect(win, ("orange"), (80,70, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 155 and mouse[1] < 215 and track[16] == 1:
                    pygame.draw.rect(win, ("orange"), (80,151, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 240 and mouse[1] < 300 and track[17] == 1:
                    pygame.draw.rect(win, ("orange"), (80,236, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 325 and mouse[1] < 385 and track[18] == 1:
                    pygame.draw.rect(win, ("orange"), (80,321, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
                
                if mouse[0] > 85 and mouse[0] < 515 and mouse[1] > 405 and mouse[1] < 465 and track[19] == 1:
                    pygame.draw.rect(win, ("orange"), (80,401, 515-75, 135-65), 8, border_radius=1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

            if mouse[0] > 270 and mouse[0] < 330 and mouse[1] > 475 and mouse[1] < 540:
                win.blit(pygame.image.load("hoverPlay.png"), (0,0))
                if event.type == pygame.MOUSEBUTTONDOWN and selected[0] == 1:
                    playing = True
                    music = pygame.mixer.music.load('title.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[1] == 1:
                    playing = True
                    music = pygame.mixer.music.load('menu_ttt.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[2] == 1:
                    playing = True
                    music = pygame.mixer.music.load('shop.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[3] == 1:
                    playing = True
                    music = pygame.mixer.music.load('achievements.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[4] == 1:
                    playing = True
                    music = pygame.mixer.music.load('tictacquestoe.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[5] == 1:
                    playing = True
                    music = pygame.mixer.music.load('neon.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[6] == 1:
                    playing = True
                    music = pygame.mixer.music.load('egypt.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[7] == 1:
                    playing = True
                    music = pygame.mixer.music.load('western.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[8] == 1:
                    playing = True
                    music = pygame.mixer.music.load('snow.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[9] == 1:
                    playing = True
                    music = pygame.mixer.music.load('bonus.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[10] == 1:
                    playing = True
                    music = pygame.mixer.music.load('hooray.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[11] == 1:
                    playing = True
                    music = pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[12] == 1:
                    playing = True
                    music = pygame.mixer.music.load('tie_theme.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[13] == 1:
                    playing = True
                    music = pygame.mixer.music.load('minimax.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[14] == 1:
                    playing = True
                    music = pygame.mixer.music.load('hurrah.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[15] == 1:
                    playing = True
                    music = pygame.mixer.music.load('postMinimax.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[16] == 1:
                    playing = True
                    music = pygame.mixer.music.load('defeatedMM.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[17] == 1:
                    playing = True
                    music = pygame.mixer.music.load('creditsTheme.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[18] == 1:
                    playing = True
                    music = pygame.mixer.music.load('storeSecret.mp3')
                    pygame.mixer.music.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected[19] == 1:
                    playing = True
                    music = pygame.mixer.music.load('completeBG.mp3')
                    pygame.mixer.music.play()
            # To here.

            # To change the colour of the selected track, from here:
            if hover_1:
                if selected[0] == 1:
                    pygame.draw.rect(win, ("gold"), (80,70, 515-75, 135-65), 8, border_radius=1)
                
                if selected[1] == 1:
                    pygame.draw.rect(win, ("gold"), (80,151, 515-75, 135-65), 8, border_radius=1)

                if selected[2] == 1:
                    pygame.draw.rect(win, ("gold"), (80,236, 515-75, 135-65), 8, border_radius=1)

                if selected[3] == 1:
                    pygame.draw.rect(win, ("gold"), (80,321, 515-75, 135-65), 8, border_radius=1)

                if selected[4] == 1:
                    pygame.draw.rect(win, ("gold"), (80,401, 515-75, 135-65), 8, border_radius=1)
                
                if track[2] == 0:
                    win.blit(unknownTrack[2], (0,0))
                
                if track[3] == 0:
                    win.blit(unknownTrack[3], (0,0))
                
                if track[4] == 0:
                    win.blit(unknownTrack[4], (0,0))
            
            if hover_2:
                if selected[5] == 1:
                    pygame.draw.rect(win, ("gold"), (80,70, 515-75, 135-65), 8, border_radius=1)
                
                if selected[6] == 1:
                    pygame.draw.rect(win, ("gold"), (80,151, 515-75, 135-65), 8, border_radius=1)

                if selected[7] == 1:
                    pygame.draw.rect(win, ("gold"), (80,236, 515-75, 135-65), 8, border_radius=1)

                if selected[8] == 1:
                    pygame.draw.rect(win, ("gold"), (80,321, 515-75, 135-65), 8, border_radius=1)

                if selected[9] == 1:
                    pygame.draw.rect(win, ("gold"), (80,401, 515-75, 135-65), 8, border_radius=1)
                
                if track[5] == 0:
                    win.blit(unknownTrack[0], (0,0))
                
                if track[6] == 0:
                    win.blit(unknownTrack[1], (0,0))
                
                if track[7] == 0:
                    win.blit(unknownTrack[2], (0,0))
                
                if track[8] == 0:
                    win.blit(unknownTrack[3], (0,0))
                
                if track[9] == 0:
                    win.blit(unknownTrack[4], (0,0))
            
            if hover_3:
                if selected[10] == 1:
                    pygame.draw.rect(win, ("gold"), (80,70, 515-75, 135-65), 8, border_radius=1)
                
                if selected[11] == 1:
                    pygame.draw.rect(win, ("gold"), (80,151, 515-75, 135-65), 8, border_radius=1)

                if selected[12] == 1:
                    pygame.draw.rect(win, ("gold"), (80,236, 515-75, 135-65), 8, border_radius=1)

                if selected[13] == 1:
                    pygame.draw.rect(win, ("gold"), (80,321, 515-75, 135-65), 8, border_radius=1)

                if selected[14] == 1:
                    pygame.draw.rect(win, ("gold"), (80,401, 515-75, 135-65), 8, border_radius=1)
                
                if track[10] == 0:
                    win.blit(unknownTrack[0], (0,0))
                
                if track[11] == 0:
                    win.blit(unknownTrack[1], (0,0))
                
                if track[12] == 0:
                    win.blit(unknownTrack[2], (0,0))
                
                if track[13] == 0:
                    win.blit(unknownTrack[3], (0,0))
                
                if track[14] == 0:
                    win.blit(unknownTrack[4], (0,0))

            if hover_4:
                if selected[15] == 1:
                    pygame.draw.rect(win, ("gold"), (80,70, 515-75, 135-65), 8, border_radius=1)
                
                if selected[16] == 1:
                    pygame.draw.rect(win, ("gold"), (80,151, 515-75, 135-65), 8, border_radius=1)

                if selected[17] == 1:
                    pygame.draw.rect(win, ("gold"), (80,236, 515-75, 135-65), 8, border_radius=1)

                if selected[18] == 1:
                    pygame.draw.rect(win, ("gold"), (80,321, 515-75, 135-65), 8, border_radius=1)

                if selected[19] == 1:
                    pygame.draw.rect(win, ("gold"), (80,401, 515-75, 135-65), 8, border_radius=1)
                
                if track[15] == 0:
                    win.blit(unknownTrack[0], (0,0))
                
                if track[16] == 0:
                    win.blit(unknownTrack[1], (0,0))
                
                if track[17] == 0:
                    win.blit(unknownTrack[2], (0,0))
                
                if track[18] == 0:
                    win.blit(unknownTrack[3], (0,0))
                
                if track[19] == 0:
                    win.blit(unknownTrack[4], (0,0))
            # To here.

            pygame.display.update()     # The game window is updated.

        pygame.display.update()         # The game window is updated.

        scorePlayer = 0                 # The player's score is set to 0.
        scoreCPU = 0                    # The CPU's score is set to 0.

    running = False                     # The game menus are stopped, as a sanity check.
    if choice != 10:                    # If the player has not selected the "Exit" button, the game is started.
        running = True
        if choice == 99:
            running = False
    while running:                      # The game loop is executed here.

        checkBoard = [0,0,0,0,0,0,0,0,0]        # The board is cleared.
        
        # Chooses which music to play depending on which board was selected.
        if choice == 1:
            music = pygame.mixer.music.load('neon.mp3')
            pygame.mixer.music.play(-1)
            if purchase_4:
                minimax_check[1] = 1
            track[5] = 1
        elif choice == 2:
            music = pygame.mixer.music.load('egypt.mp3')
            pygame.mixer.music.play(-1)
            track[6] = 1
        elif choice == 3:
            music = pygame.mixer.music.load('western.mp3')
            pygame.mixer.music.play(-1)
            track[7] = 1
        elif choice == 4:
            music = pygame.mixer.music.load('snow.mp3')
            pygame.mixer.music.play(-1)
            track[8] = 1
        elif choice == 5:
            music = pygame.mixer.music.load('minimax.mp3')
            pygame.mixer.music.play(-1)
        elif choice == 6:
            music = pygame.mixer.music.load('bonus.mp3')
            pygame.mixer.music.play(-1)
            track[9] = 1

        game = True             # The game is set to True.
        CPU_Turn = False        # The CPU's turn is set to False.
        paused = 0              # The game is not paused once the game is started.
        turn = 0                # Resets the "turn" counter.
        if choice == 5:         # If the player has selected the "Minimax" button, the minimax algorithm is executed.
            scorePlayer = 99    # Changes "Score" to "Lives".
            scoreCPU = 3        # The CPU's lives are set to 3.
            slippedUp = 0       # Random value selected to make the AI "slip up", i.e. go from the minimax algorithm to hard mode.
        while game:             # The game loop is executed here.

            mouse = pygame.mouse.get_pos()          # The mouse's position is recorded here.

            hover_Play = False                      # The "Play" button is not hovered over.

            for event in pygame.event.get():        # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0) 
                # For the move to be set by the player. From here:
                if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 60 and mouse[1] < 170 and checkBoard[0] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[0] = 1
                        turn += 1
                        move = 1
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True

                if mouse[0] > 235 and mouse[0] < 355 and mouse[1] > 60 and mouse[1] < 170 and checkBoard[1] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[1] = 1
                        turn += 1 
                        move = 2
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 390 and mouse[0] < 495 and mouse[1] > 60 and mouse[1] < 170 and checkBoard[2] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[2] = 1
                        turn += 1
                        move = 3
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 200 and mouse[1] < 305 and checkBoard[3] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[3] = 1
                        turn += 1
                        move = 4
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 235 and mouse[0] < 355 and mouse[1] > 200 and mouse[1] < 305 and checkBoard[4] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[4] = 1
                        turn += 1
                        move = 5
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 390 and mouse[0] < 495 and mouse[1] > 200 and mouse[1] < 305 and checkBoard[5] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[5] = 1
                        turn += 1
                        move = 6
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 350 and mouse[1] < 450 and checkBoard[6] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[6] = 1
                        turn += 1
                        move = 7
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 235 and mouse[0] < 355 and mouse[1] > 350 and mouse[1] < 450 and checkBoard[7] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[7] = 1
                        turn += 1
                        move = 8
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                
                if mouse[0] > 390 and mouse[0] < 495 and mouse[1] > 350 and mouse[1] < 450 and checkBoard[8] == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        checkBoard[8] = 1
                        turn += 1
                        move = 9
                        human_turn(c_choice, h_choice)
                        CPU_Turn = True
                # To here.
            # The following code is executed if the player hovers over the pause button.
            if mouse[0] > 262.5 and mouse[0] < 265.2 + 75 and mouse[1] > 510 and mouse[1] < 505 + 75 and choice != 5:
                hover_Play = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.set_volume(0.25)
                    paused = 1
            if mouse[0] > 262.5 and mouse[0] < 265.2 + 75 and mouse[1] > 510 and mouse[1] < 505 + 75 and choice == 5:
                hover_Play = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(0,9):
                        checkBoard[i] = 0

            redrawGameWindow()      # The game window is redrawn.

            oneDraw = 5             # The game window is redrawn 5 times for the transparency effect.
            while paused:           # The game is paused here.
                game = False        # The game is set to False.

                hover_Play = False  # For hovering effects.
                hover_Quit = False
                hover_Menu = False

                mouse = pygame.mouse.get_pos()  # The mouse's position is recorded.

                for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        sys.exit(0)

                while oneDraw > 0:              # The game window is redrawn 5 times for the transparency effect.
                    win.blit(surface, (0,0))
                    results_screen()
                    oneDraw += -1

                # The following code is executed if the player hovers over the "Play" button.
                if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > 410 and mouse[1] < 410 + 100:
                    hover_Play = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.music.set_volume(1)
                        game = True
                        paused = False
                
                # The following code is executed if the player hovers over the "Back" button.
                if mouse[0] > 25 and mouse[0] < 125 and mouse[1] > 25 and mouse[1] < 125:
                    hover_Menu = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        running = False
                        game = False
                        won = False
                        lost = False
                        tied = False
                        paused = False
                        choice = 15
                
                # The following code is executed if the player hovers over the "Quit" button.
                if mouse[0] > 475 and mouse[0] < 575 and mouse[1] > 25 and mouse[1] < 125:
                    hover_Quit = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        sys.exit(0)

                redrawGameWindow()      # The game window is redrawn.
                        
            loseCheck()                 # The game checks if the player has lost.
            winCheck()                  # The game checks if the player has won.
            if turn != 0 and choice == 5:       # The game checks if the player has tied.
                tieCheck()
                turn = 0

            if won or lost or tied:     # If the game is over, the following effect is displayed.

                sliding = -85           # For oscillating effect.

                if won:                 # If the player has won, the total number of wins is incremented, as well as the "money" the player has earned.
                    globalWon += 1
                    money += 1
                
                if lost:                # If the player has lost, the total number of losses is incremented.
                    globalLost += 1
                
                if tied:                # If the player has tied, the total number of ties is incremented.
                    globalTied += 1

                if choseEasy and lost:  # If the player has lost on easy mode, the total number of easy losses is incremented.
                    easyLosses += 1
                
                if choseHard and won:   # If the player has won on hard mode, the total number of hard wins is incremented.
                    hardWins += 1

                if choice != 5:         # If the player has not selected the "Minimax" button, the following effect is displayed.
                    run = False
                    menu = False
                    game = False
                elif choice == 5:       # Otherwise, the following effect is displayed.

                    clearBoard()        # The board is cleared.

                    slippedUp = random.randint(0,6) # A random value is selected to determine if the AI will "slip up".
                    
                    for i in range(0,9):    # The board is cleared.
                        checkBoard[i] = 0

                    won = False         # Resets all values determining the game state.
                    lost = False
                    tied = False
                    CPU_Turn = False

            if CPU_Turn and choseEasy:  # If the player has selected easy mode, the AI follows the easy mode algorithm.
                if choice != 5:    
                    game_board()
            
            if CPU_Turn and choseHard:  # If the player has selected hard mode, the AI follows the hard mode algorithm.
                if choice != 5:
                    tough_board()

            if CPU_Turn and choice == 5 and slippedUp != 5: # If the player has selected the "Minimax" button and it has "slipped up", the AI follows the hard mode algorithm.
                hell_board(c_choice, h_choice)

            if CPU_Turn and choice == 5 and slippedUp == 5: # If the player has selected the "Minimax" button and it has not "slipped up", the AI follows the minimax algorithm.
                tough_board()

            if choice == 5 and scorePlayer == 0:        # If the player has selected the "Minimax" button and has lost, the following effect is displayed.
                waiting = 0
                spotlightSound.play()
                pygame.mixer.music.pause()
                while True:                             # The game window is displayed for ~ 5 seconds before the game is reset.

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.display.quit()
                            pygame.quit()
                            sys.exit(0) 

                    waiting += 0.1
                    pygame.draw.rect(win, ("black"), (0,0,600,600))
                    if waiting > 300:
                        game = False
                        running = False
                        won = False
                        lost = False
                        tied = False
                        choice = 0
                        break
                    pygame.display.update()

            if choice == 5 and scoreCPU == 0:       # If the player has selected the "Minimax" button and has won, the following effect is displayed.
                game = False
                won = True
                lost = False
                tied = False

            if won and choseHard and purchase_4:    # For a minimax quest achievement.
                if choice == 2:
                    minimax_check[0] = 1

        if won and choice != 5:                     # Winning effect for all stages but the minimax one.
            music = pygame.mixer.music.load('hooray.mp3')
            pygame.mixer.music.play(-1)
            scorePlayer += 1
            track[10] = 1

            # For achievements.
            if choice == 1:
                W1 = True
            
            if choice == 2:
                W2 = True
            
            if choice == 3:
                W3 = True

            if choice == 4:
                W4 = True

            if choice == 6:
                W5 = True

        if won and choice == 5:     # The victory music is played for the minimax stage.
            music = pygame.mixer.music.load("hurrah.mp3")
            pygame.mixer.music.play(-1)

        if lost:                    # Losing effect for all stages but the minimax one.
            music = pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play(-1)
            scoreCPU += 1
            track[11] = 1

            # For achievements.
            if choice == 4 and purchase_4:
                minimax_check[2] = 1
            
            if choice == 1:
                L1 = True
            
            if choice == 2:
                L2 = True
            
            if choice == 3:
                L3 = True

            if choice == 4:
                L4 = True

            if choice == 6:
                L5 = True
        
        if tied:                    # Tying effect for all stages but the minimax one.
            music = pygame.mixer.music.load('tie_theme.mp3')
            pygame.mixer.music.play(-1)
            track[12] = 1

            if choice == 3 and purchase_4:  # For a minimax quest achievement.
                minimax_check[3] = 1
            
            # For achievements.
            if choice == 1:
                T1 = True
            
            if choice == 2:
                T2 = True
            
            if choice == 3:
                T3 = True

            if choice == 4:
                T4 = True

            if choice == 6:
                T5 = True
        
        oneDraw = 5     # The game window is redrawn 5 times for the transparency effect.
        if choice != 5:    
            time.sleep(0.3)
            oneTime = True
        
        while won and choice != 5:      # The following code is executed if the player has won and has not selected the "Minimax" stage.

            hover_Play = False          # For hovering effects.
            hover_Quit = False
            hover_Menu = False

            mouse = pygame.mouse.get_pos()      # The mouse's position is recorded.

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)

            while oneDraw > 0:                  # The game window is redrawn 5 times for the transparency effect.
                win.blit(surface, (0,0))
                results_screen()
                oneDraw += -1

            # The following code is executed if the player hovers over the "Play" button.
            if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > 410 and mouse[1] < 410 + 100:
                hover_Play = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[0] = 1
                    if globalWon >= 5:
                        checking[3] = 1
                    if globalWon >= 10:
                        checking[6] = 1
                    if hardWins >= 10:
                        checking[10] = 1
                    if W1 and W2 and W3 and W4 and W5:
                        checking[15] = 1
                    if minimax_check[0] == 1:
                        minimaxSC[0] = 1
                    game = False
                    won = False
                    lost = False
                    tied = False
            
            # The following code is executed if the player hovers over the "Menu" button.
            if mouse[0] > 25 and mouse[0] < 125 and mouse[1] > 25 and mouse[1] < 125:
                hover_Menu = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[0] = 1
                    if globalWon >= 5:
                        checking[3] = 1
                    if globalWon >= 10:
                        checking[6] = 1
                    if hardWins >= 10:
                        checking[10] = 1
                    if W1 and W2 and W3 and W4 and W5:
                        checking[15] = 1
                    if minimax_check[0] == 1:
                        minimaxSC[0] = 1
                    running = False
                    game = False
                    won = False
                    lost = False
                    tied = False
                    choice = 15
            
            # The following code is executed if the player hovers over the "Quit" button.
            if mouse[0] > 475 and mouse[0] < 575 and mouse[1] > 25 and mouse[1] < 125:
                hover_Quit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit(0)

            redrawGameWindow()      # The game window is redrawn.

            # Control "if statement" to ensure no screen glitches occur while achievement animations are displayed.
            if oneTime:
                screencopy = win.copy()
                oneTime = False

        while won and choice == 5:  # The following code is executed if the player has won and has selected the "Minimax" stage.

            hover_Play = False      # For hovering effects.

            mouse = pygame.mouse.get_pos()  # The mouse's position is recorded.

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)

            while oneDraw > 0:          # The game window is redrawn 5 times for the transparency effect.
                win.blit(surface, (0,0))
                results_screen()
                oneDraw += -1

            if oneDraw == 0:            # The game window is redrawn 5 times for the transparency effect.
                RGB_Cycle()             # The RGB cycle is executed.

                font = pygame.font.SysFont("impact", 60)        # The font is set to "impact" and the size is set to 60.

                Next = font.render("Next", True, (255,255,255)) # The "Next" button is rendered.
                pygame.draw.rect(win, (RGB[0],RGB[1],RGB[2]), (145, 405, 310, 110))    
                pygame.draw.rect(win, (0,0,1), (150, 410, 300, 100))
                
                win.blit(Next, (240, 425))                      # The "Next" button is displayed.

            # The following code is executed if the player hovers over the "Next" button.
            if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > 410 and mouse[1] < 410 + 100:
                pygame.draw.rect(win, (247,224,161), (150, 400 + 10, 300, 100))
                win.blit(Next, (240, 425))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = False
                    won = False
                    lost = False
                    tied = False
                    running = False
                    epilogue = True

            redrawGameWindow()          # The game window is redrawn.

        while lost:                     # The following code is executed if the player has lost.

            hover_Play = False          # For hovering effects.
            hover_Quit = False
            hover_Menu = False

            mouse = pygame.mouse.get_pos()  # The mouse's position is recorded.

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)
            
            while oneDraw > 0:      # The game window is redrawn 5 times for the transparency effect.
                win.blit(surface, (0,0))
                results_screen()
                oneDraw += -1
            
            osc += 0.03             # For oscillating effect.

            if osc >= 50:           # Control "if statement" to ensure no screen glitches occur while the animation is displayed.
                osc = -150

            # The following code is executed if the player hovers over the "Play" button.
            if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > 410 and mouse[1] < 410 + 100:
                hover_Play = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[1] = 1
                    if globalLost >= 5:
                        checking[4] = 1
                    if globalLost >= 10:
                        checking[7] = 1
                    if easyLosses >= 3:
                        checking[9] = 1
                    if L1 and L2 and L3 and L4 and L5:      # For achievements.
                        checking[16] = 1
                    if minimax_check[2] == 1:               # For achievements.
                        minimaxSC[2] = 1
                    game = False                            # Results statuses are reset.
                    won = False
                    lost = False
                    tied = False

            # The following code is executed if the player hovers over the "Menu" button.
            if mouse[0] > 25 and mouse[0] < 125 and mouse[1] > 25 and mouse[1] < 125:
                hover_Menu = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[1] = 1
                    if globalLost >= 5:
                        checking[4] = 1
                    if globalLost >= 10:
                        checking[7] = 1
                    if easyLosses >= 3:
                        checking[9] = 1
                    if L1 and L2 and L3 and L4 and L5:      # For achievements.
                        checking[16] = 1
                    if minimax_check[2] == 1:               # For achievements.
                        minimaxSC[2] = 1
                    running = False                         # Results statuses are reset.
                    game = False
                    won = False
                    lost = False
                    tied = False
                    choice = 15

            # The following code is executed if the player hovers over the "Quit" button.
            if mouse[0] > 475 and mouse[0] < 575 and mouse[1] > 25 and mouse[1] < 125:
                hover_Quit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit(0)

            redrawGameWindow()          # The game window is redrawn.

            if oneTime:                 # Control "if statement" to ensure no screen glitches occur while achievement animations are displayed.
                screencopy = win.copy()
                oneTime = False
        
        while tied:                     # The following code is executed if the player has tied.

            hover_Play = False          # For hovering effects.
            hover_Quit = False
            hover_Menu = False

            mouse = pygame.mouse.get_pos()      # The mouse's position is recorded.

            for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)
            
            while oneDraw > 0:                  # The game window is redrawn 5 times for the transparency effect.
                win.blit(surface, (0,0))
                results_screen()
                oneDraw += -1
        
            osc += 0.03                         # For oscillating effect.

            if osc >= 50:                       # Control "if statement" to ensure no screen glitches occur while the animation is displayed.
                osc = -150
            
            # The following code is executed if the player hovers over the "Play" button.
            if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > 410 and mouse[1] < 410 + 100:
                hover_Play = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[2] = 1
                    if globalTied >= 5:
                        checking[5] = 1
                    if globalTied >= 10:
                        checking[8] = 1
                    if T1 and T2 and T3 and T4 and T5:      # For achievements.
                        checking[17] = 1
                    if minimax_check[3] == 1:               # For achievements.
                        minimaxSC[3] = 1
                    game = False                            # Results statuses are reset.
                    won = False
                    lost = False
                    tied = False

            # The following code is executed if the player hovers over the "Menu" button.
            if mouse[0] > 25 and mouse[0] < 125 and mouse[1] > 25 and mouse[1] < 125:
                hover_Menu = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    checking[2] = 1
                    if globalTied >= 5:
                        checking[5] = 1
                    if globalTied >= 10:
                        checking[8] = 1
                    if T1 and T2 and T3 and T4 and T5:      # For achievements.
                        checking[17] = 1
                    if minimax_check[3] == 1:               # For achievements.
                        minimaxSC[3] = 1
                    running = False                         # Results statuses are reset.
                    game = False
                    won = False
                    lost = False
                    tied = False
                    choice = 15
            
            # The following code is executed if the player hovers over the "Quit" button.
            if mouse[0] > 475 and mouse[0] < 575 and mouse[1] > 25 and mouse[1] < 125:
                hover_Quit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit(0)

            redrawGameWindow()                              # The game window is redrawn.

            if oneTime:                                     # Control "if statement" to ensure no screen glitches occur while achievement animations are displayed.
                screencopy = win.copy()
                oneTime = False
        
        if minimax_check == [1,1,1,1]:                      # If the player has completed the minimax quest, the following effect is displayed.
            quest_complete = True
        
    doubleCheck1 = False                                    # Control variables.
    doubleCheck2 = False
    prelude = False
    stopCount = False
    if choice == 99:                                        # To take the player to the screen before the minimax stage.

        prelude = True
        music = pygame.mixer.music.load('prelude.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(20)

        clock = pygame.time.Clock()
        start = pygame.time.get_ticks()
    while prelude:                  # The following code is executed if the player has selected the "Minimax" button.

        mouse = pygame.mouse.get_pos()          # The mouse's position is recorded.

        hover_Quit = False                      # For hovering effects.
        hover_Play = False

        for event in pygame.event.get():        # The event loop is executed here: if the player closes the game, the game is exited.
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)

        questFont = pygame.font.SysFont("impact", 34)       # The font is set to "impact" and the size is set to 34.

        regret = questFont.render("Retreat.", True, ("white"))              # The "Retreat" button is rendered.
        fight = questFont.render("Challenge it.", True, ("white"))          # The "Challenge it" button is rendered.

        regret_hover = questFont.render("Retreat.", True, ("orange"))       # The "Retreat" button is rendered.
        fight_hover = questFont.render("Challenge it.", True, ("orange"))   # The "Challenge it" button is rendered.

        if not stopCount:                       # If the player has not selected a button, the following effect is displayed.

            pygame.draw.rect(win, ("black"), (0, 0, 600, 600))      # The screen is blacked out.

            if doubleCheck1:                                        # If the player has selected the "Retreat" button, the following effect is displayed.
                win.blit(minimax[4], minimax[4].get_rect(center = win.get_rect().center))
            
            if doubleCheck2:                                        # If the player has selected the "Challenge it" button, the following effect is displayed.
                win.blit(minimax[5], minimax[5].get_rect(center = win.get_rect().center))

            for i in range(0,2):                                    # The following code is executed if the player hovers over a button.
                clock.tick(30)
        
            finish = pygame.time.get_ticks()                        # The time is recorded.
            
            savedTime = finish - start                              # The time is saved.
        elif stopCount:                                             # If the player has selected a button, the following effect is displayed.
            savedTime = 0                                           # The time is reset.

            pygame.draw.rect(win, ("white"), (45, 495, 210, 90))    # The "Retreat" button is rendered.
            pygame.draw.rect(win, ("black"), (50, 500, 200, 80))    

            pygame.draw.rect(win, ("white"), (345, 495, 210, 90))   # The "Challenge it" button is rendered.
            pygame.draw.rect(win, ("black"), (350, 500, 200, 80))

            win.blit(regret, (95, 520))                             # Blitted onto the screen apprpriately.
            win.blit(fight, (362, 520))

        if savedTime//1000 >= 5:                                    # If the player has not selected a button within 5 seconds, the following effect is displayed.
            if not doubleCheck1 and not doubleCheck2:
                spotlightSound.play()
                win.blit(minimax[3], (0,0))
                stopCount = True
            elif doubleCheck1:
                prelude = False
            elif doubleCheck2:
                choice = 5
                prelude = False
        
        # The following code is executed if the player hovers over a button.
        if mouse[0] > 50 and mouse[0] < 250 and mouse[1] > 500 and mouse[1] < 580 and stopCount:
            hover_Quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                spotlightSound.play()
                hover_Quit = False
                stopCount = False
                doubleCheck1 = True
                clock = pygame.time.Clock()
                start = pygame.time.get_ticks()

        # The following code is executed if the player hovers over a button.
        if mouse[0] > 350 and mouse[0] < 550 and mouse[1] > 500 and mouse[1] < 580 and stopCount:
            hover_Play = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                spotlightSound.play()
                hover_Play = False
                stopCount = False
                doubleCheck2 = True
                clock = pygame.time.Clock()
                start = pygame.time.get_ticks()

        # The following code is executed if the player hovers over the quit button.
        if hover_Quit:
            pygame.draw.rect(win, ("orange"), (45, 495, 210, 90))
            pygame.draw.rect(win, ("black"), (50, 500, 200, 80))
            win.blit(regret_hover, (95, 520))
        
        # The following code is executed if the player hovers over the play button.
        if hover_Play:
            pygame.draw.rect(win, ("orange"), (345, 495, 210, 90))
            pygame.draw.rect(win, ("black"), (350, 500, 200, 80))
            win.blit(fight_hover, (362, 520))

        pygame.display.update()

    # The following code is executed if the player has selected the "Minimax" button and has won.
    if epilogue:
        music = pygame.mixer.music.load("postMinimax.mp3")
        pygame.mixer.music.play(-1)
        down1 = False
        down2 = False
        down3 = False
    while epilogue:     # Loop for the screen after the minimax stage.

        for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit(0)

        win.blit(screen, (0,0))             # The screen is blitted onto the window.

        transparency += 0.5                 # The transparency is incremented.
        transparent_filter()

        if transparency > 155:              # The following code is executed if the transparency is greater than 155.
            transparency = 155
            transparency += -0.01

        if transparency > 145:              # The following code is executed if the transparency is greater than 145.
            transparentText1 += 0.5
            if down1:
                transparentText1 += -3.5
                                            # This range keeps the transparency of the text at a certain level.
        if transparentText1 < 0:
            transparentText2 += 0.5
            if down2:
                transparentText2 += -3.5
        
        if transparentText2 < 0:
            transparentText3 += 0.5
            if down3:
                transparentText3 += -3.5

        if transparentText1 > 350:
            down1 = True       

        if transparentText2 > 350:
            down2 = True   
        
        if transparentText3 > 350:
            down3 = True

        if transparentText3 < -50:
            epilogue = False
            trophy = True
                                # The same idea applies to all text on the "epilogue" screen.
        pygame.display.update() # The game window is updated.
    
    creditSeq = False           # Control variables.
    if trophy:                  # If the player has passed the epilogue, the following effect is displayed.
        spotlightSound.play()
        music = pygame.mixer.music.load("defeatedMM.mp3")
        pygame.mixer.music.play(-1)
    while trophy:               # The following loop is executed if the player has passed the epilogue.

        mouse = pygame.mouse.get_pos()      # The mouse's position is recorded.

        for event in pygame.event.get():    # The event loop is executed here: if the player closes the game, the game is exited.
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit(0)
        
        win.blit(pygame.image.load("champ.jpg"), (0,0))     # The trophy screen is blitted onto the window.

        win.blit(postText[3], (215,475))                    # The "Continue" button is rendered.

        # The following code is executed if the player hovers over the "Continue" button.
        if mouse[0] > 215 and mouse[0] < 215 + 176 and mouse[1] > 490 and mouse[1] < 490 + 136:
            win.blit(postText[4], (215,475))
            if event.type == pygame.MOUSEBUTTONDOWN:
                trophy = False
                creditSeq = True
        
        pygame.display.update()     # The game window is updated.

    if creditSeq:                   # If the player has passed the trophy screen, the following effect is displayed.
        spotlightSound.play()
        movingUp = 0
        music = pygame.mixer.music.load("creditsTheme.mp3")
        pygame.mixer.music.play()
    while creditSeq:                # The credits sequence is displayed.

        win.blit(pygame.image.load("creditsRoll.jpg"), (0, movingUp))       # The credits screen is blitted onto the window.

        mouse = pygame.mouse.get_pos()      # The mouse's position is recorded.
        keys = pygame.key.get_pressed()     # The keys are recorded.

        for event in pygame.event.get():        # The event loop is executed here: if the player closes the game, the game is exited.
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:        # The following code is executed if the player presses the "Enter" key.
                if event.key == pygame.K_RETURN:    
                    choice = 0                      # The choice is reset, skipping the credits.
                    bonusLevel = True
                    for i in range(13,18):          # Unlocks a range of tracks.
                        track[i] = 1
                    creditSeq = False
                    postGame = True
                    clock = pygame.time.Clock()
                    start = pygame.time.get_ticks()
        
        movingUp += -1          # The credits screen moves up.

        if movingUp < -4096 + 600:  # Stops the credit rolling sequence.
            movingUp += 1

        RGB_Cycle()                 # The RGB cycle is executed twice for faster colour changes.
        RGB_Cycle()

        creditFont = pygame.font.SysFont("impact", 55)      # The font is set to "impact" and the size is set to 55.
        creditEnd = creditFont.render("Awesome!", True, ("white"))  # The "Awesome!" text is rendered.

        pygame.draw.rect(win, (RGB[0], RGB[1], RGB[2]), (145, movingUp + 3945, 310, 100))   # The "Awesome!" button is displayed.
        pygame.draw.rect(win, ("black"), (150, movingUp + 3950, 300, 90))                   # The "Awesome!" button is displayed.
        win.blit(creditEnd, (180, movingUp + 3960))

        # The following code is executed if the player hovers over the "Awesome!" button.
        if mouse[0] > 150 and mouse[0] < 150 + 300 and mouse[1] > movingUp + 3950 and mouse[1] < movingUp + 3950 + 90:
            pygame.draw.rect(win, (54,194,54), (150, movingUp + 3950, 300, 90))
            win.blit(creditEnd, (180, movingUp + 3960))
            if event.type == pygame.MOUSEBUTTONDOWN:
                choice = 0
                bonusLevel = True
                for i in range(13,18):
                    track[i] = 1
                creditSeq = False
                postGame = True
                clock = pygame.time.Clock()
                start = pygame.time.get_ticks()

        pygame.display.update()

    if postGame:        # If the player has passed the credits sequence, the following effect is displayed.
        spotlightSound.play()
        sliding = -150
        pygame.mixer.music.stop()
    while postGame:     # For the "completed game" achievement animation.

        pygame.draw.rect(win, ("black"), (0,0,600,600)) # The screen is blacked out.

        for event in pygame.event.get():                # The event loop is executed here: if the player closes the game, the game is exited.
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit(0)
        
        dropDown = -0.000005 * (sliding ** 4)           # The drop down effect is calculated.

        win.blit(pygame.image.load("E3.png"), (0, 240 + int(dropDown)))     # The "completed game" achivement is blitted onto the window.

        if int(dropDown) == -2 and sliding < 0:         # Once the animation is hits the minimum of its path, the sound effect is played.
            trophySound.play()

        sliding += 0.4                                  # For the sliding effect.

        if sliding > 150:                               # The following code is executed if the sliding effect is greater than 150 to ensure it doesn't repeat.
            checking[13] = 1
            postGame = False

        pygame.display.update()         # The game window is updated.

pygame.quit()           # The game is exited.
sys.exit(0)             # All done! :)