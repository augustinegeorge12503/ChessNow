import pygame as p
import engine
import sys
from multiprocessing import Process, Queue
from constants import * 
from functions import *
from design import Design
from button import Button
from page import Page
from bot import ChessBot
from sound import Sound

def main():

    p.init()
    p.display.set_caption("ChessNow")
    screen = p.display.set_mode((BOARD_WIDTH + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    gameState = engine.GameState()
    validMoves = gameState.getValidMoves()
    moveMade = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    changePiece('classic') # do this only once before while loop
    squareSelected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    playerClicks = []  # this will keep track of player clicks (two tuples)
    gameOver = False
    aiThinking = False
    moveUndone = False
    moveFinderProcess = None
    moveLogFont = p.font.SysFont("Arial", 14, False, False)
    playerOne = True  # if a human is playing white, then this will be True, else False
    playerTwo = False  # if a human is playing white, then this will be True, else False
    gamePage = Page() # tracks the current page of game
    design = Design() # display the design of a page
    Bot = ChessBot() # game bot
    moveSound = Sound('assets/sounds/move.wav')
    captureSound = Sound('assets/sounds/capture.wav')

    # initializing all buttons
    # home
    playButtonHome = Button('Play', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 245), screen)
    settingsButtonHome = Button('Settings', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 335), screen)
    creditButtonHome = Button('Creators', design.smallFont, (0,0,0), (255,255,255), (200,50), (445,425), screen)
    
    # pva select
    playButtonFriendly = Button('Play', design.smallFont, ('#FF9600'), (0,0,0), (150,50), (105, 535), screen)
    playButtonEvil = Button('Play', design.smallFont, ('#92F1AA'), (0,0,0), (150,50), (275, 535), screen)
    playButtonAug = Button('Play', design.smallFont, ('#FF003B'), (0,0,0), (150,50), (445, 535), screen)
    playButtonArdit = Button('Play', design.smallFont, ('#00B6FF'), (0,0,0), (150,50), (615, 535), screen)
    playButtonAbby = Button('Play', design.smallFont, ('#F9EF4D'), (0,0,0), (150,50), (785, 535), screen)

    # creators
    backButtonCredit = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (785, 600), screen)
    
    # settings/back buttons
    backButtonSettings = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (785, 600), screen)
    pieceButtonSettings = Button('Piece', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 250), screen)
    boardButtonSettings = Button('Board', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 350), screen)
    backButtonBoard = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (785, 600), screen)
    backButtonPvaSelect = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (785, 600), screen)


    # piece
    backButtonPiece = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150,50), (785, 600), screen)
    classicButtonPiece = Button('classic', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 80), screen, selected=True)
    classicExample = p.image.load('assets/pieces/examples/classic_example.png')
    stupidButtonPiece = Button('stupid', design.smallFont, (0,0,0), (255,255,255), (200,50), (495,165), screen)
    stupidExample = p.image.load('assets/pieces/examples/stupid_example.png')
    simpleButtonPiece = Button('simple', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 250), screen)
    simpleExample = p.image.load('assets/pieces/examples/simple_example.png')
    chaturangaButtonPiece = Button('chaturanga', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 335), screen)
    chaturangaExample = p.image.load('assets/pieces/examples/chat_example.png')
    cyberButtonPiece = Button('cyber', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 420), screen)
    cyberExample = p.image.load('assets/pieces/examples/cyber_example.png')
    organicButtonPiece = Button('organic', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 505), screen)
    organicExample = p.image.load('assets/pieces/examples/organic_example.png')
    royalButtonPiece = Button('royal', design.smallFont, (0,0,0), (255,255,255), (200,50), (495, 590), screen)
    royalExample = p.image.load('assets/pieces/examples/royal_example.png')


    # boards column 1
    classicBoardButton = Button('classic', design.smallFont, (0,0,0), ('#9135F0'), (200,50), (300, 50), screen, selected=True)
    classicBoardExample = p.transform.smoothscale(BOARDS['classic'], (55,55))
    midnightBoardButton = Button('midnight', design.smallFont, (0,0,0), ('#11009E'), (200,50), (300, 130), screen)
    midnightBoardExample = p.transform.smoothscale(BOARDS['midnight'], (55,55))
    cafeBoardButton = Button('cafe', design.smallFont, (0,0,0), ('#B68860'), (200,50), (300, 210), screen)
    cafeBoardExample = p.transform.smoothscale(BOARDS['cafe'], (55,55))
    checkersBoardButton = Button('checkers', design.smallFont, (0,0,0), ('#CC1817'), (200,50), (300, 290), screen)
    checkersBoardExample = p.transform.smoothscale(BOARDS['checkers'], (55,55))
    grayBoardButton = Button('gray', design.smallFont, (0,0,0), ('#202B3F'), (200,50), (300, 370), screen)
    grayBoardExample = p.transform.smoothscale(BOARDS['gray'], (55,55))
    forestBoardButton = Button('forest', design.smallFont, (0,0,0), ('#0B666B'), (200,50), (300, 450), screen)
    forestBoardExample = p.transform.smoothscale(BOARDS['forest'], (55,55))
    tangerineBoardButton = Button('tangerine', design.smallFont, (0,0,0), ('#DD6200'), (200,50), (300, 530), screen)
    tangerineBoardExample = p.transform.smoothscale(BOARDS['tangerine'], (55,55))
    # second column of boards
    woodBoardButton = Button('wood', design.smallFont, (0,0,0), ('#833C1F'), (200,50), (550, 50), screen)
    woodBoardExample = p.transform.smoothscale(BOARDS['wood'], (55,55))
    marbleBoardButton = Button('marble', design.smallFont, (0,0,0), ('#D0CDC8'), (200,50), (550, 130), screen)
    marbleBoardExample = p.transform.smoothscale(BOARDS['marble'], (55,55))
    glassBoardButton = Button('glass', design.smallFont, (0,0,0), ('#768B96'), (200,50), (550, 210), screen)
    glassBoardExample = p.transform.smoothscale(BOARDS['glass'], (55,55))
    onyxBoardButton = Button('onyx', design.smallFont, (0,0,0), ('#0F3044'), (200,50), (550, 290), screen)
    onyxBoardExample = p.transform.smoothscale(BOARDS['onyx'], (55,55))
    greenhouseBoardButton = Button('greenhouse', design.smallFont, (0,0,0), ('#1E3222'), (200,50), (550, 370), screen)
    greenhouseBoardExample = p.transform.smoothscale(BOARDS['greenhouse'], (55,55))
    parchmentBoardButton = Button('parchment', design.smallFont, (0,0,0), ('#DBC08D'), (200,50), (550, 450), screen)
    parchmentBoardExample = p.transform.smoothscale(BOARDS['parchment'], (55,55))
    sweettoothBoardButton = Button('sweettooth', design.smallFont, (0,0,0), ('#FCA6C9'), (200,50), (550, 530), screen)
    sweettoothBoardExample = p.transform.smoothscale(BOARDS['sweettooth'], (55,55))

    # pva
    forefeitButtonPva = Button('Forefeit', design.smallFont, (0,0,0), (255,255,255), (250, 80), (765, 600), screen, square=True)

    # piece button list
    pieceButtonList = [classicButtonPiece, stupidButtonPiece, simpleButtonPiece, chaturangaButtonPiece, cyberButtonPiece, organicButtonPiece, royalButtonPiece]
    boardButtonList = [classicBoardButton, midnightBoardButton, cafeBoardButton, checkersBoardButton, grayBoardButton, 
                       forestBoardButton, tangerineBoardButton, woodBoardButton, marbleBoardButton, glassBoardButton, 
                       onyxBoardButton, greenhouseBoardButton, parchmentBoardButton, sweettoothBoardButton]

    while True:

        # home game page
        if gamePage.page == 'home':
            
            design.showPage(gamePage.page, screen)
            playButtonHome.draw()
            creditButtonHome.draw()
            settingsButtonHome.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(playButtonHome, gamePage, 'pva_select')
                    changePage(creditButtonHome, gamePage, 'credit')
                    changePage(settingsButtonHome, gamePage, 'settings')
        
        # key game page
        if gamePage.page == 'credit':

            design.showPage('credit', screen)
            backButtonCredit.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonCredit, gamePage, 'home')

        # settings game page
        if gamePage.page == 'settings':

            design.showPage('settings', screen)
            backButtonSettings.draw()
            pieceButtonSettings.draw()
            boardButtonSettings.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonSettings, gamePage, 'home')
                    changePage(pieceButtonSettings, gamePage, 'piece')
                    changePage(boardButtonSettings, gamePage, 'board')
        
        # piece game page
        if gamePage.page == 'piece':
            
            design.showPage('piece', screen)
            backButtonPiece.draw()
            classicButtonPiece.draw()
            screen.blit(classicExample, (265, 40))
            stupidButtonPiece.draw()
            screen.blit(stupidExample, (265, 120))
            simpleButtonPiece.draw()
            screen.blit(simpleExample, (265, 205))
            chaturangaButtonPiece.draw()
            screen.blit(chaturangaExample, (265, 290))
            cyberButtonPiece.draw()
            screen.blit(cyberExample, (265, 380))
            organicButtonPiece.draw()
            screen.blit(organicExample, (265, 470))
            royalButtonPiece.draw()
            screen.blit(royalExample, (265, 560))


            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonPiece, gamePage, 'settings')
                    # change piece in game
                    changePieceMenu(pieceButtonList, stupidButtonPiece)
                    changePieceMenu(pieceButtonList, classicButtonPiece)
                    changePieceMenu(pieceButtonList, simpleButtonPiece)
                    changePieceMenu(pieceButtonList, chaturangaButtonPiece)
                    changePieceMenu(pieceButtonList, cyberButtonPiece)
                    changePieceMenu(pieceButtonList, organicButtonPiece)
                    changePieceMenu(pieceButtonList, royalButtonPiece)
            
        if gamePage.page == 'board':
            design.showPage('board', screen)
            backButtonBoard.draw()
            classicBoardButton.draw()
            screen.blit(classicBoardExample, (120, 20))
            midnightBoardButton.draw()
            screen.blit(midnightBoardExample, (120, 100))
            cafeBoardButton.draw()
            screen.blit(cafeBoardExample, (120, 180))
            checkersBoardButton.draw()
            screen.blit(checkersBoardExample, (120, 260))
            grayBoardButton.draw()
            screen.blit(grayBoardExample, (120, 340))
            forestBoardButton.draw()
            screen.blit(forestBoardExample, (120, 420))
            tangerineBoardButton.draw()
            screen.blit(tangerineBoardExample, (120, 510))
            woodBoardButton.draw()
            screen.blit(woodBoardExample, (675, 20))
            marbleBoardButton.draw()
            screen.blit(marbleBoardExample, (675, 100))
            glassBoardButton.draw()
            screen.blit(glassBoardExample, (675, 180))
            onyxBoardButton.draw()
            screen.blit(onyxBoardExample, (675, 260))
            greenhouseBoardButton.draw()
            screen.blit(greenhouseBoardExample, (675, 340))
            parchmentBoardButton.draw()
            screen.blit(parchmentBoardExample, (675, 420))
            sweettoothBoardButton.draw()
            screen.blit(sweettoothBoardExample, (675, 500))


            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonBoard, gamePage, 'settings')
                    # these below are not functioning yet
                    changeBoardMenu(boardButtonList, classicBoardButton)
                    changeBoardMenu(boardButtonList, midnightBoardButton)
                    changeBoardMenu(boardButtonList, cafeBoardButton)
                    changeBoardMenu(boardButtonList, checkersBoardButton)
                    changeBoardMenu(boardButtonList, grayBoardButton)
                    changeBoardMenu(boardButtonList, forestBoardButton)
                    changeBoardMenu(boardButtonList, tangerineBoardButton)
                    changeBoardMenu(boardButtonList, woodBoardButton)
                    changeBoardMenu(boardButtonList, marbleBoardButton)
                    changeBoardMenu(boardButtonList, glassBoardButton)
                    changeBoardMenu(boardButtonList, onyxBoardButton)
                    changeBoardMenu(boardButtonList, greenhouseBoardButton)
                    changeBoardMenu(boardButtonList, parchmentBoardButton)
                    changeBoardMenu(boardButtonList, sweettoothBoardButton)

        # select AI opponent
        if gamePage.page == 'pva_select':
            design.showPage('pva_select', screen)
            backButtonPvaSelect.draw()
            playButtonFriendly.draw()
            playButtonEvil.draw()
            playButtonAug.draw()
            playButtonArdit.draw()
            playButtonAbby.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(playButtonFriendly, gamePage, 'pva')
                    if playButtonFriendly.checkCollision():
                        Bot.assignBot('beep')
                    changePage(playButtonEvil, gamePage, 'pva')
                    if playButtonEvil.checkCollision():
                        Bot.assignBot('boop')
                    changePage(playButtonAug, gamePage, 'pva')
                    if playButtonAug.checkCollision():
                        Bot.assignBot('augustine')
                    changePage(playButtonArdit, gamePage, 'pva')
                    if playButtonArdit.checkCollision():
                        Bot.assignBot('ardit')
                    changePage(playButtonAbby, gamePage, 'pva')
                    if playButtonAbby.checkCollision():
                        Bot.assignBot('abby')
                    changePage(backButtonPvaSelect, gamePage, 'home')

        # pva game page
        if gamePage.page == 'pva':

            # draws the back button
            design.showPage('pva', screen)
            forefeitButtonPva.draw()

            humanTurn = (gameState.whiteToMove and playerOne) or (not gameState.whiteToMove and playerTwo)

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()
                    # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    if forefeitButtonPva.checkCollision():
                        changePage(forefeitButtonPva, gamePage, 'home')
                        gameState = engine.GameState()
                        validMoves = gameState.getValidMoves()
                        squareSelected = ()
                        playerClicks = []
                        moveMade = False
                        animate = False
                        gameOver = False
                        if aiThinking:
                            moveFinderProcess.terminate()
                            aiThinking = False
                        moveUndone = True

                    if not gameOver:
                        location = p.mouse.get_pos()  # (x, y) location of the mouse
                        col = location[0] // SQUARE_SIZE
                        row = location[1] // SQUARE_SIZE
                        if squareSelected == (row, col) or col >= 8:  # user clicked the same square twice
                            squareSelected = ()  # deselect
                            playerClicks = []  # clear clicks
                        else:
                            squareSelected = (row, col)
                            playerClicks.append(squareSelected)  # append for both 1st and 2nd click
                        if len(playerClicks) == 2 and humanTurn:  # after 2nd click
                            move = engine.Move(playerClicks[0], playerClicks[1], gameState.board)
                            for i in range(len(validMoves)):
                                if move == validMoves[i]:
                                    gameState.makeMove(validMoves[i])
                                    playSound(move, moveSound, captureSound)
                                    moveMade = True
                                    animate = True
                                    squareSelected = ()  # reset user clicks
                                    playerClicks = []
                            if not moveMade:
                                playerClicks = [squareSelected]

                # key handler
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_z:  # undo when 'z' is pressed
                        gameState.undoMove()
                        moveMade = True
                        animate = False
                        gameOver = False
                        if aiThinking:
                            moveFinderProcess.terminate()
                            aiThinking = False
                        moveUndone = True
                    if e.key == p.K_r:  # reset the game when 'r' is pressed
                        gameState = engine.GameState()
                        validMoves = gameState.getValidMoves()
                        squareSelected = ()
                        playerClicks = []
                        moveMade = False
                        animate = False
                        gameOver = False
                        if aiThinking:
                            moveFinderProcess.terminate()
                            aiThinking = False
                        moveUndone = True

            # AI move finder
            if not gameOver and not humanTurn and not moveUndone:
                if not aiThinking:
                    aiThinking = True
                    returnQueue = Queue()
                    # Use AI to find the best move
                    moveFinderProcess = Process(target=Bot.findBestMove, args=(gameState, validMoves, returnQueue))
                    moveFinderProcess.start()

                if not moveFinderProcess.is_alive():
                    aiMove = returnQueue.get()
                    if aiMove is None:
                        aiMove = Bot.findRandomMove(validMoves)
                    gameState.makeMove(aiMove)
                    playSound(aiMove, moveSound, captureSound)
                    moveMade = True
                    animate = True
                    aiThinking = False

            if moveMade:
                if animate:
                    animateMove(gameState.moveLog[-1], screen, gameState.board, clock)
                validMoves = gameState.getValidMoves()
                moveMade = False
                animate = False
                moveUndone = False

            if not gameOver:
                drawMoveLog(screen, gameState, moveLogFont)
                drawGameState(screen, gameState, validMoves, squareSelected)

            if gameState.checkmate:
                gameOver = True
                if gameState.whiteToMove:
                    drawEndGameText(screen, "Black wins by CHECKMATE")
                else:
                    drawEndGameText(screen, "White wins by CHECKMATE")
            elif gameState.stalemate:
                gameOver = True
                drawEndGameText(screen, "Stalemate")

        p.display.flip()

if __name__ == "__main__":
    main()