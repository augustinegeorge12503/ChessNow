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
        image = p.image.load(imagePath)
        imageDict[piece] = image
    return imageDict

CLASSIC = preLoadImages('classic')
SIMPLE = preLoadImages('simple')
STUPID = preLoadImages('stupid')
CHATURANGA = preLoadImages('chaturanga')
CYBER = preLoadImages('cyber')
ORGANIC = preLoadImages('organic')
ROYAL = preLoadImages('royal')

IMAGEDICT = {
    'classic': CLASSIC,
    'simple': SIMPLE,
    'stupid': STUPID,
    'chaturanga': CHATURANGA,
    'cyber': CYBER,
    'organic': ORGANIC,
    'royal': ROYAL
}

# preloading boards
BOARDS = {}

boardList = ['abbys_fav', 'cafe', 'checkers', 'classic', 'forest', 'glass', 'gray', 'marble', 'midnight', 'onyx', 'tangerine', 'wood', 'greenhouse', 'parchment', 'sweettooth']
for board in boardList:
    image = p.image.load(f'assets/boards/{board}_board.png')
    BOARDS[board] = image
