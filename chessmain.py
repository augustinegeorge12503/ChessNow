"""
Main File ChessNow
"""
import pygame as p
import ChessEngine, ChessAI
import sys
from multiprocessing import Process, Queue




BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 25
IMAGES = {}




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
  pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
  for piece in pieces:
      image_path = "images/" + piece + ".png"
      original_image = p.image.load(image_path)
      scaled_image = p.transform.smoothscale(original_image, (SQUARE_SIZE, SQUARE_SIZE))
      IMAGES[piece] = scaled_image












def main():
  """
  The main driver for our code.
  This will handle user input and updating the graphics.
  """
  p.init()
  p.display.set_caption("ChessNow")
  screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
  clock = p.time.Clock()
  screen.fill(p.Color("white"))
  game_state = ChessEngine.GameState()
  valid_moves = game_state.getValidMoves()
  move_made = False  # flag variable for when a move is made
  animate = False  # flag variable for when we should animate a move
  loadImages()  # do this only once before while loop
  running = True
  square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
  player_clicks = []  # this will keep track of player clicks (two tuples)
  game_over = False
  ai_thinking = False
  move_undone = False
  move_finder_process = None
  move_log_font = p.font.SysFont("Arial", 14, False, False)
  player_one = True  # if a human is playing white, then this will be True, else False
  player_two = False  # if a hyman is playing white, then this will be True, else False
  in_main_menu = True
  in_game = False




  while True:
      if in_main_menu:
           drawMainMenu(screen)
           for event in p.event.get():
               if event.type == p.QUIT:
                   p.quit()
                   sys.exit()
               elif event.type == p.MOUSEBUTTONDOWN:
                   play_button = p.Rect(291, 206, 180, 50)
                   if play_button.collidepoint(event.pos):
                       in_main_menu = False
                       in_game = True
           p.display.update()
      human_turn = (game_state.white_to_move and player_one) or (not game_state.white_to_move and player_two)
      for e in p.event.get():
          if e.type == p.QUIT:
              p.quit()
              sys.exit()
          # mouse handler
          elif e.type == p.MOUSEBUTTONDOWN:
              if not game_over:
                  location = p.mouse.get_pos()  # (x, y) location of the mouse
                  col = location[0] // SQUARE_SIZE
                  row = location[1] // SQUARE_SIZE
                  if square_selected == (row, col) or col >= 8:  # user clicked the same square twice
                      square_selected = ()  # deselect
                      player_clicks = []  # clear clicks
                  else:
                      square_selected = (row, col)
                      player_clicks.append(square_selected)  # append for both 1st and 2nd click
                  if len(player_clicks) == 2 and human_turn:  # after 2nd click
                      move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                      for i in range(len(valid_moves)):
                          if move == valid_moves[i]:
                              game_state.makeMove(valid_moves[i])
                              move_made = True
                              animate = True
                              square_selected = ()  # reset user clicks
                              player_clicks = []
                      if not move_made:
                          player_clicks = [square_selected]



          # key handler
          elif e.type == p.KEYDOWN:
              if e.key == p.K_z:  # undo when 'z' is pressed
                  game_state.undoMove()
                  move_made = True
                  animate = False
                  game_over = False
                  if ai_thinking:
                      move_finder_process.terminate()
                      ai_thinking = False
                  move_undone = True
              if e.key == p.K_r:  # reset the game when 'r' is pressed
                  game_state = ChessEngine.GameState()
                  valid_moves = game_state.getValidMoves()
                  square_selected = ()
                  player_clicks = []
                  move_made = False
                  animate = False
                  game_over = False
                  if ai_thinking:
                      move_finder_process.terminate()
                      ai_thinking = False
                  move_undone = True




      # AI move finder
      if not game_over and not human_turn and not move_undone:
          if not ai_thinking:
              ai_thinking = True
              return_queue = Queue()
             # Use AI to find the best move
              move_finder_process = Process(target=ChessAI.findBestMove, args=(game_state, valid_moves, return_queue))
              move_finder_process.start()
             



          if not move_finder_process.is_alive():
              ai_move = return_queue.get()
              if ai_move is None:
                  ai_move = ChessAI.findRandomMove(valid_moves)
              game_state.makeMove(ai_move)
              move_made = True
              animate = True
              ai_thinking = False




      if move_made:
          if animate:
              animateMove(game_state.move_log[-1], screen, game_state.board, clock)
          valid_moves = game_state.getValidMoves()
          move_made = False
          animate = False
          move_undone = False


      if in_main_menu == False:
       drawGameState(screen, game_state, valid_moves, square_selected)




      if not game_over and in_main_menu == False:
          drawMoveLog(screen, game_state, move_log_font)




      if game_state.checkmate:
          game_over = True
          if game_state.white_to_move:
              drawEndGameText(screen, "Black wins by checkmate")
          else:
              drawEndGameText(screen, "White wins by checkmate")




      elif game_state.stalemate:
          game_over = True
          drawEndGameText(screen, "Stalemate")




      clock.tick(MAX_FPS)
      p.display.flip()
      mouse_pos = p.mouse.get_pos()
      play_button_rect = p.Rect(291, 206, 180, 50)
      playwithai_button_rect = p.Rect(291, 266, 180, 50)
      settings_button_rect = p.Rect(291, 326, 180, 50)
      
      if play_button_rect.collidepoint(mouse_pos) and in_main_menu == True:
           p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)  # Change cursor to hand
      elif playwithai_button_rect.collidepoint(mouse_pos) and in_main_menu == True:
           p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)  # Change cursor to hand
      elif settings_button_rect.collidepoint(mouse_pos) and in_main_menu == True:
           p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)  # Change cursor to hand
      else:
            p.mouse.set_cursor(p.SYSTEM_CURSOR_ARROW)  # Change cursor to arrow




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



if __name__ == "__main__":
  main()