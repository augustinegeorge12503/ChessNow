"""
Main File ChessNow
"""
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
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """
    p.init()
    p.display.set_caption("ChessNow")
    screen = p.display.set_mode((BOARD_WIDTH + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    gameState = ChessEngine.GameState()
    validMoves = gameState.getValidMoves()
    moveMade = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages()  # do this only once before while loop
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

    while True:

        # home game page
        if gamePage.page == 'home':
            
            design.showPage(gamePage.page, screen)
            playButton = Button('Play', design.smallFont, (0,0,0), (255,255,255), (200,50), (376, 200), screen)
            playButton.draw()

            keyButton = Button('Key', design.smallFont, (0,0,0), (255,255,255), (200,50), (376, 290), screen)
            keyButton.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    if playButton.checkCollision():
                        gamePage.changePage('pva')
                    if keyButton.checkCollision():
                        gamePage.changePage('key')
        
        # key game page
        if gamePage.page == 'key':

            design.showPage('key', screen)
            backButton = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (640, 470), screen)
            backButton.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    if backButton.checkCollision():
                        gamePage.changePage('home')

        # pva game page
        if gamePage.page == 'pva':

            # draws the back button
            backButton = Button('Back', design.smallFont, (0,0,0), (255,255,255), (150, 50), (640, 470), screen)
            backButton.draw()

            humanTurn = (gameState.whiteToMove and playerOne) or (not gameState.whiteToMove and playerTwo)

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()
                    # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    if backButton.checkCollision():
                        gamePage.changePage('home')
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