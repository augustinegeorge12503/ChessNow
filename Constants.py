"""
holds game constants
"""
import pygame as p

BOARD_WIDTH = BOARD_HEIGHT = 640
MOVELOG_PANEL_WIDTH = 250
MOVELOG_PANEL_HEIGHT = BOARD_HEIGHT - 80 
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 25
IMAGES = {}
BOARD = 'classic'

# preloading pieces
def preLoadImages(pieceset):
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    imageDict = {}
    for piece in pieces:
        imagePath = f"assets/pieces/{pieceset}/{piece}.png"
        original_image = p.image.load(imagePath)
        scaled_image = p.transform.smoothscale(original_image, (SQUARE_SIZE, SQUARE_SIZE))
        imageDict[piece] = scaled_image
    return imageDict

CBURNETT = preLoadImages('cburnett')
CLASSIC = preLoadImages('classic')
SIMPLE = preLoadImages('simple')
STUPID = preLoadImages('stupid')
CHATURANGA = preLoadImages('chaturanga')
CYBER = preLoadImages('cyber')

IMAGEDICT = {
    'cburnett': CBURNETT,
    'classic': CLASSIC,
    'simple': SIMPLE,
    'stupid': STUPID,
    'chaturanga': CHATURANGA,
    'cyber': CYBER
}

# preloading boards
BOARDS = {}

boardList = ['abbys_fav', 'cafe', 'checkers', 'classic', 'forest', 'glass', 'gray', 'marble', 'midnight', 'onyx', 'tangerine', 'wood', 'greenhouse', 'parchment', 'sweettooth']
for board in boardList:
    image = p.transform.scale(p.image.load(f'assets/boards/{board}_board.png'), (BOARD_WIDTH, BOARD_HEIGHT))
    BOARDS[board] = image
