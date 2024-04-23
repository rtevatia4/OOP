import PlayingPiece

class Player:
    def __init__(self, name, playing_piece: PlayingPiece):
        self.name = name
        self.playing_piece = playing_piece
    
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
    
    def get_playing_piece(self) -> PlayingPiece:
        return self.playing_piece

    def set_playing_piece(self, piece):
        self.playing_piece = piece