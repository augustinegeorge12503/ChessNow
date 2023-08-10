"""
holds all game functions
"""
from Constants import *
import pygame as p
import sys

def drawGameState(screen, gameState, validMoves, squareSelected):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(screen)  # draw squares on the board
    highlightSquares(screen, gameState, validMoves, squareSelected)
    drawPieces(screen, gameState.board)  # draw pieces on top of those squares

def drawBoard(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current gameState.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawCircle(surface, color, center, radius, alpha):
    """
    Draw a small centered circle on the surface with the given color and transparency.
    """
    s = p.Surface((SQUARE_SIZE, SQUARE_SIZE), p.SRCALPHA)  # Create a surface with alpha (transparency) support
    p.draw.circle(s, color + (alpha,), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), radius)  # Draw a centered circle
    surface.blit(s, (center[1] * SQUARE_SIZE, center[0] * SQUARE_SIZE))  # Blit the circle on the main surface

def drawSquare(surface, color, row, col, alpha):
    """
    Draw a small centered square on the surface with the given color and transparency.
    """
    s = p.Surface((SQUARE_SIZE, SQUARE_SIZE), p.SRCALPHA)  # Create a surface with alpha (transparency) support
    s.fill(color + (alpha,))
    surface.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))  # Blit the square on the main surface

def highlightSquares(screen, gameState, validMoves, squareSelected):
    """
    Highlight square selected and moves for piece selected.
    """
    def get_squareColor(row, col):
        """
        Determine the color of the square based on row and column indices.
        """
        return (row + col) % 2  # 0 for white square, 1 for black square
    
    if (len(gameState.moveLog)) > 0:
        lastMove = gameState.moveLog[-1]
        drawSquare(screen, (0, 0, 255), lastMove.endRow, lastMove.endCol, 100)  # Blue square with alpha=100
    if squareSelected != ():
        row, col = squareSelected
        if gameState.board[row][col][0] == (
                'w' if gameState.whiteToMove else 'b'):  # squareSelected is a piece that can be moved
        
            # Determine the color of the selected square
            squareColor = get_squareColor(row, col)
            alpha = 170  # Default alpha value for the square overlay
        
            # If the square is black, increase transparency (lower alpha)
            if squareColor == 1:
                alpha = 130
        
            # Highlight selected square with a blue box
            drawSquare(screen, (0, 0, 255), row, col, alpha)
            # Highlight moves from that square with circles
            for move in validMoves:
                if move.startRow == row and move.startCol == col:
                    drawCircle(screen, (0, 0, 0), (move.endRow, move.endCol), 8, 50)  # Yellow circle with alpha=100

def drawMoveLog(screen, gameState, font):
    """
    Draws the move log.
    """
    moveLogRect = p.Rect(BOARD_WIDTH, 0, MOVELOG_PANEL_WIDTH, MOVELOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), moveLogRect)
    moveLog = gameState.moveLog
    moveTexts = []
    for i in range(0, len(moveLog), 2):
        moveString = str(i // 2 + 1) + '. ' + str(moveLog[i]) + " "
        if i + 1 < len(moveLog):
            moveString += str(moveLog[i + 1]) + "  "
        moveTexts.append(moveString)

    movesPerRow = 3
    padding = 5
    lineSpacing = 2
    textY = padding
    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i + j]

        textObject = font.render(text, True, p.Color('white'))
        textLocation = moveLogRect.move(padding, textY)
        screen.blit(textObject, textLocation)
        textY += textObject.get_height() + lineSpacing

def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    textObject = font.render(text, False, p.Color("gray"))
    textLocation = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - textObject.get_width() / 2,
                                                                BOARD_HEIGHT / 2 - textObject.get_height() / 2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, False, p.Color('black'))
    screen.blit(textObject, textLocation.move(2, 2))

def animateMove(move, screen, board, clock):
    """
    Animating a move
    """
    global colors
    dRow = move.endRow - move.startRow
    dCol = move.endCol - move.startCol
    framesPerSquare = 5  # frames to move one square
    if move.pieceMoved[1] == 'B'or 'Q':  # Check if the piece moved is a bishop
        framesPerSquare = 2
    if move.pieceMoved[1] == 'N': # Check if the piece moved is a knight
        framesPerSquare = 3 # frames to move one square
    frameCount = (abs(dRow) + abs(dCol)) * framesPerSquare
    for frame in range(frameCount + 1):
        row, col = (move.startRow + dRow * frame / frameCount, move.startCol + dCol * frame / frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol * SQUARE_SIZE, move.endRow * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, endSquare)
        # draw captured piece onto rectangle
        if move.pieceCaptured != '--':
            if move.isEnpassantMove:
                enpassantRow = move.endRow + 1 if move.pieceCaptured[0] == 'b' else move.endRow - 1
                endSquare = p.Rect(move.endCol * SQUARE_SIZE, enpassantRow * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        # draw moving piece
        screen.blit(IMAGES[move.pieceMoved], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)

def handleMainMenuEvents():
   for event in p.event.get():
       if event.type == p.QUIT:
           p.quit()
           sys.exit()
       elif event.type == p.MOUSEBUTTONDOWN:
           playButtonHome = p.Rect(150, 200, 180, 50)
           if playButtonHome.collidepoint(event.pos):
               return False  # Return False to indicate that we should exit the main menu
   return True

def drawMainMenu(screen):
   
   screen.fill(p.Color("white"))
   font = p.font.SysFont("Arial", 28, True)
  
   # Play button
   playButtonHome = p.Rect(291, 206, 180, 50)
   p.draw.rect(screen, p.Color("green"), playButtonHome)
   textSurface = font.render("Play", True, p.Color("white"))
   textRect = textSurface.get_rect()
   textRect.center = playButtonHome.center
   screen.blit(textSurface, textRect)
  
   # Play with AI button
   playAiButton = p.Rect(291, 266, 180, 50)
   p.draw.rect(screen, p.Color("blue"), playAiButton)
   textSurface = font.render("Play with AI", True, p.Color("white"))
   textRect = textSurface.get_rect()
   textRect.center = playAiButton.center
   screen.blit(textSurface, textRect)
  
   # Settings button
   settingsButtonHome = p.Rect(291, 326, 180, 50)
   p.draw.rect(screen, p.Color("orange"), settingsButtonHome)
   textSurface = font.render("Settings", True, p.Color("white"))
   textRect = textSurface.get_rect()
   textRect.center = settingsButtonHome.center
   screen.blit(textSurface, textRect)
  
   p.display.flip()  # Update the display after drawing everything

def drawSettingsButtons(screen):
    '''settingsButtonHome = p.Rect(150, 260, 180, 50)
    p.draw.rect(screen, p.Color("blue"), settingsButtonHome)  # Draw the settings button
    font = p.font.SysFont("Arial", 28, True)
    textSurface = font.render("Settings", True, p.Color("white"))
    textRect = textSurface.get_rect()
    textRect.center = settingsButtonHome.center
    screen.blit(textSurface, textRect)  # Blit the text onto the settings button
    p.display.flip()'''

def loadImages(pieceSet):
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    # to change pieces, rename the file to directory name
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        imagePath = f"assets/pieces/{pieceSet}/{piece}.png"
        original_image = p.image.load(imagePath)
        scaled_image = p.transform.smoothscale(original_image, (SQUARE_SIZE, SQUARE_SIZE))
        IMAGES[piece] = scaled_image

def resetButtonSelection(pieceButtonList, selectedButton):
    for pieceButton in pieceButtonList:
        if pieceButton != selectedButton:
            pieceButton.selected = False

def changePiece(newPieceSet):
    loadImages(newPieceSet)

def changePieceMenu(pieceButtonList, selectedButton):
    if selectedButton.checkCollision():
        resetButtonSelection(pieceButtonList, selectedButton)
        selectedButton.changeSelection()
        if selectedButton.isSelected():
            changePiece(selectedButton.text)
        else:
            changePiece('default')

def changePage(button, gamePage, page):
    if button.checkCollision():
        gamePage.changePage(page)