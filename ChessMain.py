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
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    game_state = ChessEngine.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages()  # do this only once before while loop
    square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False
    ai_thinking = False
    move_undone = False
    move_finder_process = None
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    player_one = True  # if a human is playing white, then this will be True, else False
    player_two = False  # if a human is playing white, then this will be True, else False
    game_page = Page() # tracks the current page of game
    design = Design() # display the design of a page

    while True:

        # home game page
        if game_page.page == 'home':
            
            design.show_page(game_page.page, screen)
            play_button = Button('Play', design.small_font, (0,0,0), (255,255,255), (200,50), (376, 200), screen)
            play_button.draw()

            key_button = Button('Key', design.small_font, (0,0,0), (255,255,255), (200,50), (376, 290), screen)
            key_button.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    if play_button.check_collision():
                        game_page.change_page('pva')
                    if key_button.check_collision():
                        game_page.change_page('key')
        
        # key game page
        if game_page.page == 'key':

            design.show_page('key', screen)
            back_button = Button('Back', design.small_font, (0,0,0), (255,255,255), (150, 50), (640, 470), screen)
            back_button.draw()

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    if back_button.check_collision():
                        game_page.change_page('home')

        # pva game page
        if game_page.page == 'pva':

            # draws the back button
            back_button = Button('Back', design.small_font, (0,0,0), (255,255,255), (150, 50), (640, 470), screen)
            back_button.draw()

            human_turn = (game_state.white_to_move and player_one) or (not game_state.white_to_move and player_two)

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()
                    # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    if back_button.check_collision():
                        game_page.change_page('home')
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

            if not game_over:
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
                
            drawGameState(screen, game_state, valid_moves, square_selected)

        p.display.flip()

if __name__ == "__main__":
    main()