from PieceType import PieceType
from PlayingPiece import PlayingPiece

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
