
class Box:
    def __init__(self, piece: Piece, x : int, y: int): # type: ignore
        self.__piece = piece
        self.__x = x
        self.__y = y