"""
holds all game functions
"""
from Constants import *
import pygame as p
import sys

def drawGameState(screen, game_state, valid_moves, square_selected):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(screen)  # draw squares on the board
    highlightSquares(screen, game_state, valid_moves, square_selected)
    drawPieces(screen, game_state.board)  # draw pieces on top of those squares

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
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_circle(surface, color, center, radius, alpha):
    """
    Draw a small centered circle on the surface with the given color and transparency.
    """
    s = p.Surface((SQUARE_SIZE, SQUARE_SIZE), p.SRCALPHA)  # Create a surface with alpha (transparency) support
    p.draw.circle(s, color + (alpha,), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), radius)  # Draw a centered circle
    surface.blit(s, (center[1] * SQUARE_SIZE, center[0] * SQUARE_SIZE))  # Blit the circle on the main surface

def draw_square(surface, color, row, col, alpha):
    """
    Draw a small centered square on the surface with the given color and transparency.
    """
    s = p.Surface((SQUARE_SIZE, SQUARE_SIZE), p.SRCALPHA)  # Create a surface with alpha (transparency) support
    s.fill(color + (alpha,))
    surface.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))  # Blit the square on the main surface

def highlightSquares(screen, game_state, valid_moves, square_selected):
    """
    Highlight square selected and moves for piece selected.
    """
    def get_square_color(row, col):
        """
        Determine the color of the square based on row and column indices.
        """
        return (row + col) % 2  # 0 for white square, 1 for black square
    
    if (len(game_state.move_log)) > 0:
        last_move = game_state.move_log[-1]
        draw_square(screen, (0, 0, 255), last_move.end_row, last_move.end_col, 100)  # Blue square with alpha=100
    if square_selected != ():
        row, col = square_selected
        if game_state.board[row][col][0] == (
                'w' if game_state.white_to_move else 'b'):  # square_selected is a piece that can be moved
        
            # Determine the color of the selected square
            square_color = get_square_color(row, col)
            alpha = 170  # Default alpha value for the square overlay
        
            # If the square is black, increase transparency (lower alpha)
            if square_color == 1:
                alpha = 130
        
            # Highlight selected square with a blue box
            draw_square(screen, (0, 0, 255), row, col, alpha)
            # Highlight moves from that square with circles
            for move in valid_moves:
                if move.start_row == row and move.start_col == col:
                    draw_circle(screen, (0, 0, 0), (move.end_row, move.end_col), 8, 50)  # Yellow circle with alpha=100

def drawMoveLog(screen, game_state, font):
    """
    Draws the move log.
    """
    move_log_rect = p.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), move_log_rect)
    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
        if i + 1 < len(move_log):
            move_string += str(move_log[i + 1]) + "  "
        move_texts.append(move_string)

    moves_per_row = 3
    padding = 5
    line_spacing = 2
    text_y = padding
    for i in range(0, len(move_texts), moves_per_row):
        text = ""
        for j in range(moves_per_row):
            if i + j < len(move_texts):
                text += move_texts[i + j]

        text_object = font.render(text, True, p.Color('white'))
        text_location = move_log_rect.move(padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height() + line_spacing

def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    text_object = font.render(text, False, p.Color("gray"))
    text_location = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - text_object.get_width() / 2,
                                                                BOARD_HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, False, p.Color('black'))
    screen.blit(text_object, text_location.move(2, 2))

def animateMove(move, screen, board, clock):
    """
    Animating a move
    """
    global colors
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    frames_per_square = 5  # frames to move one square
    if move.piece_moved[1] == 'B'or 'Q':  # Check if the piece moved is a bishop
        frames_per_square = 2
    if move.piece_moved[1] == 'N': # Check if the piece moved is a knight
        frames_per_square = 3 # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    for frame in range(frame_count + 1):
        row, col = (move.start_row + d_row * frame / frame_count, move.start_col + d_col * frame / frame_count)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if move.piece_captured != '--':
            if move.is_enpassant_move:
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * SQUARE_SIZE, enpassant_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            screen.blit(IMAGES[move.piece_captured], end_square)
        # draw moving piece
        screen.blit(IMAGES[move.piece_moved], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)

def handleMainMenuEvents():
   for event in p.event.get():
       if event.type == p.QUIT:
           p.quit()
           sys.exit()
       elif event.type == p.MOUSEBUTTONDOWN:
           play_button = p.Rect(150, 200, 180, 50)
           if play_button.collidepoint(event.pos):
               return False  # Return False to indicate that we should exit the main menu
   return True

def drawMainMenu(screen):
   screen.fill(p.Color("white"))
   font = p.font.SysFont("Arial", 28, True)
  
   # Play button
   play_button = p.Rect(291, 206, 180, 50)
   p.draw.rect(screen, p.Color("green"), play_button)
   text_surface = font.render("Play", True, p.Color("white"))
   text_rect = text_surface.get_rect()
   text_rect.center = play_button.center
   screen.blit(text_surface, text_rect)
  
   # Play with AI button
   play_ai_button = p.Rect(291, 266, 180, 50)
   p.draw.rect(screen, p.Color("blue"), play_ai_button)
   text_surface = font.render("Play with AI", True, p.Color("white"))
   text_rect = text_surface.get_rect()
   text_rect.center = play_ai_button.center
   screen.blit(text_surface, text_rect)
  
   # Settings button
   settings_button = p.Rect(291, 326, 180, 50)
   p.draw.rect(screen, p.Color("orange"), settings_button)
   text_surface = font.render("Settings", True, p.Color("white"))
   text_rect = text_surface.get_rect()
   text_rect.center = settings_button.center
   screen.blit(text_surface, text_rect)
  
   p.display.flip()  # Update the display after drawing everything

def drawSettingsButtons(screen):
    '''settings_button = p.Rect(150, 260, 180, 50)
    p.draw.rect(screen, p.Color("blue"), settings_button)  # Draw the settings button
    font = p.font.SysFont("Arial", 28, True)
    text_surface = font.render("Settings", True, p.Color("white"))
    text_rect = text_surface.get_rect()
    text_rect.center = settings_button.center
    screen.blit(text_surface, text_rect)  # Blit the text onto the settings button
    p.display.flip()'''

def loadImages():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    # to change pieces, rename the file to directory name
    piece_set = 'old'
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        image_path = f"assets/pieces/{piece_set}/{piece}.png"
        original_image = p.image.load(image_path)
        scaled_image = p.transform.smoothscale(original_image, (SQUARE_SIZE, SQUARE_SIZE))
        IMAGES[piece] = scaled_image
