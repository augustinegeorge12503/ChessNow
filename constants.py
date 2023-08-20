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


# messages

MESSAGES = {
    'augustine': ['Do you even know how to play?', 'Your moves are rook-ie', 'Take that!', 'Resign and save your dignity',
                   'LOL', 'Did you learn chess today?', 'Your pieces need glasses', 'Your pieces need therapy', 'Knightmare moves',
                     'Could\'ve done better', 'Castle this, buddy', 'This is not even a challenge', 'You\'re a pawn in life', 
                    'You\'re a natural...disaster', 'Are you a secret NPC boss?', 'Give me a challenge', ],
    'augustineStart': 'Another day, another easy mate',
    'augustineWon': 'What did you expect?',
    'augustineLost': 'You\'re better than I thought',


    'boop': ['Wow, not bad', 'Brilliant!', 'Take that!', 'You\'re pretty good!',
                   'Are you sure about that?', 'Good move', 'Great move!',
                     'That\'s interesting!', '...Sorry!', 'Have you met BEEP? Scary...', 'Let\'s have a great game'],
    'boopStart': 'I am BOOP! Hi friend!',
    'boopWon': 'Good try!',
    'boopLost': 'You\'ve beaten me! Impressive!',


    'beep': ['I am not amused...', 'Do all humans play like this?', 
             'Why do you waste my time?', 'Don\'t quit your day job.', 'You\'re the reason we have BOOP.', 'How cute.'],
    'beepStart': 'I am the all-powerful BEEP!',
    'beepWon': 'All according to my programming.',
    'beepLost': 'You\'ll regret this, human!',


    'ardit': ['Wow, not bad', 'Brilliant!', 'Take that!', 'You\'re pretty good!',
                   'Are you sure about that?', 'Is that supposed to be a joke?', 'Good move', 'Great move!',
                     'You may want to take that back...'],
    'arditStart': 'Hello, my name is Ardit!',
    'arditWon': 'I win!',
    'arditLost': 'Wow. I can\'t believe this.',


    'abby': ['It\'s okay, you\'re still learning!', 
             'My friend played a move like that once! They lost.', 'Exciting!', 'Are you trying to lose?', 
             'I\'ve seen this line before...', 'Hurry up and lose already!', 'Resigning is always an option.',
             'Oh. You\'re still playing?', 'Don\'t be shy - I don\'t bite!', 'Quite bold.'],
    'abbyStart': 'Will you give me a good game?',
    'abbyWon': 'As expected.',
    'abbyLost': '@#?$%! I mean - good game.'
}