import random

class ChessBot:

    def __init__(self) -> None:
        self.bot = ''
    
    def assignBot(self, botName):
        if botName == 'beep':
            self.bot = 'beep'
            self.pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

            self.knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

            self.bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

            self.rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                        [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

            self.queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

            self.pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                        [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                        [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                        [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
                        [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
                        [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

            self.piecePositionScores = {"wN": self.knightScores,
                                    "bN": self.knightScores[::-1],
                                    "wB": self.bishopScores,
                                    "bB": self.bishopScores[::-1],
                                    "wQ": self.queenScores,
                                    "bQ": self.queenScores[::-1],
                                    "wR": self.rookScores,
                                    "bR": self.rookScores[::-1],
                                    "wp": self.pawnScores,
                                    "bp": self.pawnScores[::-1]}

            self.CHECKMATE = 1000
            self.STALEMATE = 0
            self.DEPTH = 2

        elif botName == 'boop':
            self.bot = 'boop'
            self.pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

            self.knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

            self.bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

            self.rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                        [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

            self.queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.8, 0.8, 0.5, 0.8, 0.5, 0.5, 0.8, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

            self.pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                        [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                        [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                        [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
                        [0.25, 0.15, 0.24, 0.2, 0.2, 0.1, 0.15, 0.25],
                        [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

            self.piecePositionScores = {"wN": self.knightScores,
                                    "bN": self.knightScores[::-1],
                                    "wB": self.bishopScores,
                                    "bB": self.bishopScores[::-1],
                                    "wQ": self.queenScores,
                                    "bQ": self.queenScores[::-1],
                                    "wR": self.rookScores,
                                    "bR": self.rookScores[::-1],
                                    "wp": self.pawnScores,
                                    "bp": self.pawnScores[::-1]}

            self.CHECKMATE = 1000
            self.STALEMATE = 0
            self.DEPTH = 2

        elif botName == 'augustine':
            self.bot = 'augustine'
            self.pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

            self.knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

            self.bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

            self.rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                        [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

            self.queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

            self.pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                        [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                        [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                        [0.2, 0.2, 0.2, 2, 2, 0.2, 0.2, 0.2],
                        [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
                        [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

            self.piecePositionScores = {"wN": self.knightScores,
                                    "bN": self.knightScores[::-1],
                                    "wB": self.bishopScores,
                                    "bB": self.bishopScores[::-1],
                                    "wQ": self.queenScores,
                                    "bQ": self.queenScores[::-1],
                                    "wR": self.rookScores,
                                    "bR": self.rookScores[::-1],
                                    "wp": self.pawnScores,
                                    "bp": self.pawnScores[::-1]}

            self.CHECKMATE = 1000
            self.STALEMATE = 0
            self.DEPTH = 3

        elif botName == 'ardit':
            self.bot = 'ardit'
            self.pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

            self.knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                            [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

            self.bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

            self.rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                        [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

            self.queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

            self.pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                        [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                        [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                        [0.2, 0.2, 0.2, 2, 2, 0.2, 0.2, 0.2],
                        [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
                        [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

            self.piecePositionScores = {"wN": self.knightScores,
                                    "bN": self.knightScores[::-1],
                                    "wB": self.bishopScores,
                                    "bB": self.bishopScores[::-1],
                                    "wQ": self.queenScores,
                                    "bQ": self.queenScores[::-1],
                                    "wR": self.rookScores,
                                    "bR": self.rookScores[::-1],
                                    "wp": self.pawnScores,
                                    "bp": self.pawnScores[::-1]}

            self.CHECKMATE = 1000
            self.STALEMATE = 0
            self.DEPTH = 3

        elif botName == 'abby':
            self.bot = 'abby'
            self.pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

            self.knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                            [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                            [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                            [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                            [0.2, 0.5, 0.60, 0.7, 0.7, 0.60, 0.5, 0.2],
                            [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                            [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                            [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

            self.bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                            [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                            [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                            [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                            [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                            [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                            [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                            [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

            self.rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                        [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                        [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

            self.queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

            self.pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                        [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                        [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                        [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                        [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
                        [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
                        [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

            self.piecePositionScores = {"wN": self.knightScores,
                                    "bN": self.knightScores[::-1],
                                    "wB": self.bishopScores,
                                    "bB": self.bishopScores[::-1],
                                    "wQ": self.queenScores,
                                    "bQ": self.queenScores[::-1],
                                    "wR": self.rookScores,
                                    "bR": self.rookScores[::-1],
                                    "wp": self.pawnScores,
                                    "bp": self.pawnScores[::-1]}

            self.CHECKMATE = 1000
            self.STALEMATE = 0
            self.DEPTH = 3

    def findBestMove(self, gameState, validMoves, returnQueue):
        global nextMove
        nextMove = None
        random.shuffle(validMoves)
        self.findMoveNegaMaxAlphaBeta(gameState, validMoves, self.DEPTH, -self.CHECKMATE, self.CHECKMATE,
                                1 if gameState.whiteToMove else -1)
        returnQueue.put(nextMove)
    
    def findMoveNegaMaxAlphaBeta(self, gameState, validMoves, depth, alpha, beta, turn_multiplier):
        global nextMove
        if depth == 0:
            return turn_multiplier * self.scoreBoard(gameState)
        # move ordering - implement later //TODO
        max_score = -self.CHECKMATE
        for move in validMoves:
            gameState.makeMove(move)
            nextMoves = gameState.getValidMoves()
            score = -self.findMoveNegaMaxAlphaBeta(gameState, nextMoves, depth - 1, -beta, -alpha, -turn_multiplier)
            if score > max_score:
                max_score = score
                if depth == self.DEPTH:
                    nextMove = move
            gameState.undoMove()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score

    def scoreBoard(self, gameState):
        """
        Score the board. A positive score is good for white, a negative score is good for black.
        """
        if gameState.checkmate:
            if gameState.whiteToMove:
                return -self.CHECKMATE  # black wins
            else:
                return self.CHECKMATE  # white wins
        elif gameState.stalemate:
            return self.STALEMATE
        score = 0
        for row in range(len(gameState.board)):
            for col in range(len(gameState.board[row])):
                piece = gameState.board[row][col]
                if piece != "--":
                    piecePositionScore = 0
                    if piece[1] != "K":
                        piecePositionScore = self.piecePositionScores[piece][row][col]
                    if piece[0] == "w":
                        score += self.pieceScore[piece[1]] + piecePositionScore
                    if piece[0] == "b":
                        score -= self.pieceScore[piece[1]] + piecePositionScore

        return score

    def findRandomMove(self, validMoves):
        """
        Picks and returns a random valid move.
        """
        return random.choice(validMoves)
