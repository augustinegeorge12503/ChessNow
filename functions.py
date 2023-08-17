"""
holds all game functions
"""
from constants import *
import pygame as p

def drawGameState(screen, gameState, validMoves, squareSelected):
    drawCustomBoard(BOARD, screen)
    highlightSquares(screen, gameState, validMoves, squareSelected)
    drawPieces(screen, gameState.board)  # draw pieces on top of those squares

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
    colors = [p.Color("white"), p.Color("gray")]
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
        drawCustomBoard(BOARD, screen)
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

def resetButtonSelection(pieceButtonList, selectedButton):
    for pieceButton in pieceButtonList:
        if pieceButton != selectedButton:
            pieceButton.selected = False

def changePiece(newPieceSet):
    global IMAGES
    IMAGES = IMAGEDICT[newPieceSet]

def changeBoard(newBoard):
    global BOARD
    BOARD = newBoard

def changePieceMenu(pieceButtonList, selectedButton):
    if selectedButton.checkCollision():
        resetButtonSelection(pieceButtonList, selectedButton)
        selectedButton.changeSelection()
        selectedButton.playClickSound()
        changePiece(selectedButton.text)

def changeBoardMenu(boardButtonList, selectedButton):
    if selectedButton.checkCollision():
        resetButtonSelection(boardButtonList, selectedButton)
        selectedButton.changeSelection()
        selectedButton.playClickSound()
        changeBoard(selectedButton.text)

def changePage(button, gamePage, page):
    if button.checkCollision():
        button.playClickSound()
        gamePage.changePage(page)

def drawCustomBoard(newBoard, screen):
    screen.blit(BOARDS[newBoard], (0,0))

def playSound(move, moveSound, captureSound):
    if move.isCapture:
        captureSound.play()
    else:
        moveSound.play()