# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:37:50 2019

@author: ravi9
"""

from configrations import *
import model
import exceptions

class Piece():
    
    def __init__(self, color = "white"):
        self.name = self.__class__.__name__.lower()
        if color == 'black':
            self.name = self.name.lower()
        elif color == 'white':
            self.name = self.name.upper()
        
        self.color = color
        
        
    def keep_reference(self, model):
        self.model = model
        

        
def get_numeric_notation(rowcol):    
    row, col = rowcol    
    return int(col)-1, X_AXIS_LABELS.index(row) 

def create_piece (piece, color='white'):

    if isinstance(piece, str):
        if piece.upper() in SHORT_NAME.keys():
            color = "white" if piece.isupper() else "black"
            piece = SHORT_NAME[piece.upper()]
        piece = piece.capitalize()
        if piece in SHORT_NAME.values():
            return eval("{classname}(color)".format(classname=piece))
    raise exceptions.ChessError("invalid piece name: '{}'".format(piece))


class King(Piece):
    pass


class Queen(Piece):
    pass


class Rook(Piece):
    pass

class Bishop(Piece):
    pass


class Knight(Piece):
    pass

class Pawn(Piece):
    pass

            
            