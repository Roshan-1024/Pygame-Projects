import pygame
import sys
import random

#settings
BOARD_WIDTH, BOARD_HEIGHT = 626, 626
WINDOW_WIDTH, WINDOW_HEIGHT = BOARD_WIDTH+300, BOARD_HEIGHT
DICE_X, DICE_Y = WINDOW_WIDTH-175, WINDOW_HEIGHT-125
colors = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
coordinates = []
players = {1: "Blue", 2: "Red"}
player1Locked = True #when True, player-1 start moving
player2Locked = True #when True, player-2 start moving
moveNumber = [0, 0]

#set coordinates for blue (Player 1)
for i in range(10):
    if i % 2 == 0:  #L->R
        for j in range(10):
            coordinates.append((50 + 54 * j, WINDOW_HEIGHT-90 - 54 * i))
    else:   #R->L
        for j in range(9, -1, -1):
            coordinates.append((50 + 54 * j, WINDOW_HEIGHT-90 - 54 * i))


#print coordinates of blue
# for i in range(100):
#     print(coordinates[i], end = " ")
#     if (i+1) % 10 == 0:
#         print()

def bgMusic():
    pass

def bgImg():
    url = "Images/background.png"
    return pygame.image.load(url)

def playerImg(player):
    url = "Images/blue.png" if player == 1 else "Images/red.png"
    img = pygame.image.load(url)
    img = pygame.transform.scale(img, (25, 25))
    return img

def die_images():
    # Load the sprite sheet
    dice_sheet = pygame.image.load('Images/die.png')

    # Dimensions of each die face (assuming 6 faces in a horizontal row)
    die_face_width = dice_sheet.get_width() // 6
    die_face_height = dice_sheet.get_height()

    # Extract each die face
    dice_faces = []
    for i in range(6):
        rect = pygame.Rect(i * die_face_width, 0, die_face_width, die_face_height)
        img = dice_sheet.subsurface(rect)
        resized_img = pygame.transform.scale(img, (90, 60))   #new width, new height
        dice_faces.append(resized_img)
    return dice_faces

def diceRoll(window, dice_index, randomNum):
    if dice_index < randomNum:
        dice = die_images()
        window.blit(dice[dice_index], (DICE_X, DICE_Y))  #dice position
        dice_index+=1
    return dice_index

def showDice(window, currentFace):
    dice = die_images()
    window.blit(dice[currentFace-1], (DICE_X, DICE_Y))   #dice position


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake and Ladder")
    clock = pygame.time.Clock()
    font_h1 = pygame.font.Font("Fonts/Roboto-Regular.ttf", 36)
    font_h2 = pygame.font.Font("Fonts/Roboto-Regular.ttf", 20)
    fps = 10
    dice_index = 0
    running = True
    dice_roll_animation = False
    background_img = bgImg()
    diceFace = 1
    currentPlayer = 1   #1 and 2
    gameStarted = False #Game starts when spacebar is pressed for the first time
    player1Number = 1  #default number where they are standing
    player2Number = 1
    global player1Locked
    global player2Locked
    player1GotFirstSix = False
    player2GotFirstSix = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameStarted:
                        gameStarted = True
                    dice_roll_animation = True

                    diceFace = random.randint(1, 6) #random dice number generator

                    print(f"Player-{currentPlayer}({players[currentPlayer]}): {diceFace}")   #prints the players' moves

                    #Change player turn if diceFace != 6
                    if not diceFace == 6:
                        currentPlayer = 1 if currentPlayer == 2 else 2

                    #First 6 logic
                    if currentPlayer == 1 and diceFace == 6 and player1Locked:
                        player1GotFirstSix = True
                    elif currentPlayer == 2 and diceFace == 6 and player2Locked:
                        player2GotFirstSix = True
                    
                    #Unlock players
                    if currentPlayer == 1 and player1Locked and diceFace == 6:
                        player1Locked = False
                    elif currentPlayer == 2 and player2Locked and diceFace == 6:
                        player2Locked = False
                    
                    #Change players' position
                    if not player1Locked and i != 1 and currentPlayer == 1:
                        player1Number += -1 + diceFace
                    if not player2Locked and j != 1 and currentPlayer == 2:
                        player2Number += -1 + diceFace
                    
        
        #Background Image
        window.fill(colors["white"])
        window.blit(background_img, (0, 0))

        #text
        text = font_h1.render(f"Player-{currentPlayer}({players[currentPlayer]})", True, colors["black"])
        window.blit(text, (WINDOW_WIDTH - 250, 50))
        if not gameStarted:
            text = font_h2.render(f"Press Spacebar to start", True, colors["black"])
            window.blit(text, (WINDOW_WIDTH - 250, 125))
        
        #default position of players
        
        


        #Gameplay
        # window.blit(playerImg(1), coordinates[player1Number-1])
        # window.blit(playerImg(2), (coordinates[player2Number-1][0]+10, coordinates[player2Number-1][1]+20))
        #gameLogic(window, player1Locked, player2Locked, currentPlayer, diceFace, player1Number, player2Number)
        
        window.blit(playerImg(1), coordinates[player1Number-1])
        window.blit(playerImg(2), (coordinates[player2Number-1][0]+10, coordinates[player2Number-1][1]+20))
        
        #dice
        if dice_roll_animation:
            dice_index = diceRoll(window, dice_index, diceFace)
            if dice_index >= diceFace:
                dice_index = 0
                dice_roll_animation = False

        #retain dice number
        if not dice_roll_animation:
            showDice(window, diceFace)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()