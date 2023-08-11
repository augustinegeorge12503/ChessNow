import pygame as p
import ChessEngine, ChessAI
import sys
from multiprocessing import Process, Queue
from Constants import * 
from GameFunctions import *
from Design import Design
from Button import Button
from Page import Page

def main():

    p.init()
    p.display.set_caption("ChessNow")
    screen = p.display.set_mode((BOARD_WIDTH + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    gameState = ChessEngine.GameState()
    validMoves = gameState.getValidMoves()
    moveMade = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages('classic')  # do this only once before while loop
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

    # initializing all buttons
    # home
    playButtonHome = Button('Play', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 200), screen)
    keyButtonHome = Button('Key', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 290), screen)
    settingsButtonHome = Button('Settings', design.smallFont, (0,0,0), (255,255,255), (200,50), (445,380), screen)
    
    # key
    backButtonKey = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (770, 600), screen)
    
    # settings
    backButtonSettings = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (770, 600), screen)
    pieceButtonSettings = Button('Piece', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 200), screen)
    boardButtonSettings = Button('Board', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 290), screen)
    backButtonBoard = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (770, 600), screen)
    backgroundButtonSettings = Button('Background', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 380), screen)
    backButtonBackground = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (770, 600), screen)

    # piece
    backButtonPiece = Button('Back', design.smallFont, (0,0,0), (255,255,255), (200,50), (770, 600), screen)
    classicButtonPiece = Button('classic', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 100), screen)
    classicExample = p.transform.smoothscale(p.image.load('assets/pieces/classic/wR.png'), (55, 55))
    stupidButtonPiece = Button('stupid', design.smallFont, (0,0,0), (255,255,255), (200,50), (445,160), screen)
    stupidExample = p.transform.smoothscale(p.image.load('assets/pieces/stupid/wR.png'), (55, 55))
    simpleButtonPiece = Button('simple', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 220), screen)
    simpleExample = p.transform.smoothscale(p.image.load('assets/pieces/simple/wR.png'), (55, 55))
    chaturangaButtonPiece = Button('chaturanga', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 280), screen)
    chaturangaExample = p.transform.smoothscale(p.image.load('assets/pieces/chaturanga/wR.png'), (55, 55))
    cyberButtonPiece = Button('cyber', design.smallFont, (0,0,0), (255,255,255), (200,50), (445, 340), screen)
    cyberExample = p.transform.smoothscale(p.image.load('assets/pieces/cyber/wR.png'), (55, 55))
    
    # boards column 1
    classicBoardButton = Button('classic', design.smallFont, (0,0,0), ('#9135F0'), (200,50), (300, 100), screen)
    classicBoardExample = p.transform.smoothscale(p.image.load('assets/boards/classic_board.png'), (55, 55))
    midnightBoardButton = Button('midnight', design.smallFont, (0,0,0), ('#11009E'), (200,50), (300, 180), screen)
    midnightBoardExample = p.transform.smoothscale(p.image.load('assets/boards/midnight_board.png'), (55, 55))
    cafeBoardButton = Button('cafe', design.smallFont, (0,0,0), ('#B68860'), (200,50), (300, 260), screen)
    cafeBoardExample = p.transform.smoothscale(p.image.load('assets/boards/cafe_board.png'), (55, 55))
    checkersBoardButton = Button('checkers', design.smallFont, (0,0,0), ('#CC1817'), (200,50), (300, 340), screen)
    checkersBoardExample = p.transform.smoothscale(p.image.load('assets/boards/checkers_board.png'), (55, 55))
    grayBoardButton = Button('gray', design.smallFont, (0,0,0), ('#202B3F'), (200,50), (300, 420), screen)
    grayBoardExample = p.transform.smoothscale(p.image.load('assets/boards/gray_board.png'), (55, 55))
    forestBoardButton = Button('forest', design.smallFont, (0,0,0), ('#0B666B'), (200,50), (300, 500), screen)
    forestBoardExample = p.transform.smoothscale(p.image.load('assets/boards/forest_board.png'), (55, 55))
    tangerineBoardButton = Button('tangerine', design.smallFont, (0,0,0), ('#DD6200'), (200,50), (300, 580), screen)
    tangerineBoardExample = p.transform.smoothscale(p.image.load('assets/boards/tangerine_board.png'), (55, 55))
    # second column of boards
    woodBoardButton = Button('wood', design.smallFont, (0,0,0), ('#833C1F'), (200,50), (550, 100), screen)
    woodBoardExample = p.transform.smoothscale(p.image.load('assets/boards/wood_board.png'), (55, 55))
    marbleBoardButton = Button('marble', design.smallFont, (0,0,0), ('#D0CDC8'), (200,50), (550, 180), screen)
    marbleBoardExample = p.transform.smoothscale(p.image.load('assets/boards/marble_board.png'), (55, 55))
    glassBoardButton = Button('glass', design.smallFont, (0,0,0), ('#768B96'), (200,50), (550, 260), screen)
    glassBoardExample = p.transform.smoothscale(p.image.load('assets/boards/glass_board.png'), (55, 55))
    onyxBoardButton = Button('onyx', design.smallFont, (0,0,0), ('#0F3044'), (200,50), (550, 340), screen)
    onyxBoardExample = p.transform.smoothscale(p.image.load('assets/boards/onyx_board.png'), (55, 55))

    # pva
    backButtonPva = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (770, 600), screen)

    # piece button list
    pieceButtonList = [classicButtonPiece, stupidButtonPiece, simpleButtonPiece, chaturangaButtonPiece, cyberButtonPiece]
    boardButtonList = [classicBoardButton, midnightBoardButton, cafeBoardButton, checkersBoardButton, grayBoardButton, 
                       forestBoardButton, tangerineBoardButton, woodBoardButton, marbleBoardButton, glassBoardButton, 
                       onyxBoardButton]
    
    # settings check mark - currently unused
    check = p.transform.smoothscale(p.image.load('assets/checks/check3.png'), (40, 40))

    while True:

        # home game page
        if gamePage.page == 'home':
            
            design.showPage(gamePage.page, screen)
            playButtonHome.draw()
            keyButtonHome.draw()
            settingsButtonHome.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(playButtonHome, gamePage, 'pva')
                    changePage(keyButtonHome, gamePage, 'key')
                    changePage(settingsButtonHome, gamePage, 'settings')
        
        # key game page
        if gamePage.page == 'key':

            design.showPage('key', screen)
            backButtonKey.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonKey, gamePage, 'home')

        # settings game page
        if gamePage.page == 'settings':

            design.showPage('settings', screen)
            backButtonSettings.draw()
            pieceButtonSettings.draw()
            boardButtonSettings.draw()
            backgroundButtonSettings.draw()

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
            screen.blit(classicExample, (250, 70))
            stupidButtonPiece.draw()
            screen.blit(stupidExample, (250, 130))
            simpleButtonPiece.draw()
            screen.blit(simpleExample, (250, 190))
            chaturangaButtonPiece.draw()
            screen.blit(chaturangaExample, (250, 250))
            cyberButtonPiece.draw()
            screen.blit(cyberExample, (250, 310))

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
            
        if gamePage.page == 'board':
            design.showPage('board', screen)
            backButtonBoard.draw()
            classicBoardButton.draw()
            screen.blit(classicBoardExample, (120, 70))
            midnightBoardButton.draw()
            screen.blit(midnightBoardExample, (120, 150))
            cafeBoardButton.draw()
            screen.blit(cafeBoardExample, (120, 230))
            checkersBoardButton.draw()
            screen.blit(checkersBoardExample, (120, 310))
            grayBoardButton.draw()
            screen.blit(grayBoardExample, (120, 390))
            forestBoardButton.draw()
            screen.blit(forestBoardExample, (120, 470))
            tangerineBoardButton.draw()
            screen.blit(tangerineBoardExample, (120, 560))
            woodBoardButton.draw()
            screen.blit(woodBoardExample, (675, 70))
            marbleBoardButton.draw()
            screen.blit(marbleBoardExample, (675, 150))
            glassBoardButton.draw()
            screen.blit(glassBoardExample, (675, 230))
            onyxBoardButton.draw()
            screen.blit(onyxBoardExample, (675, 310))


            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonBoard, gamePage, 'settings')
                    # these below are not functioning yet
                    changeBoardMenu(boardButtonList, classicBoardButton)
                    changeBoardMenu(boardButtonList, midnightBoardButton)

        # pva game page
        if gamePage.page == 'pva':

            # draws the back button
            backButtonPva.draw()

            humanTurn = (gameState.whiteToMove and playerOne) or (not gameState.whiteToMove and playerTwo)

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()
                    # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    changePage(backButtonPva, gamePage, 'home')
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
                            move = ChessEngine.Move(playerClicks[0], playerClicks[1], gameState.board)
                            for i in range(len(validMoves)):
                                if move == validMoves[i]:
                                    gameState.makeMove(validMoves[i])
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
                        gameState = ChessEngine.GameState()
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
                    moveFinderProcess = Process(target=ChessAI.findBestMove, args=(gameState, validMoves, returnQueue))
                    moveFinderProcess.start()

                if not moveFinderProcess.is_alive():
                    aiMove = returnQueue.get()
                    if aiMove is None:
                        aiMove = ChessAI.findRandomMove(validMoves)
                    gameState.makeMove(aiMove)
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

            if gameState.checkmate:
                gameOver = True
                if gameState.whiteToMove:
                    drawEndGameText(screen, "Black wins by checkmate")
                else:
                    drawEndGameText(screen, "White wins by checkmate")
            elif gameState.stalemate:
                gameOver = True
                drawEndGameText(screen, "Stalemate")
                
            drawGameState(screen, gameState, validMoves, squareSelected)

        p.display.flip()

if __name__ == "__main__":
    main()