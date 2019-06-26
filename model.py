# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:48:50 2019

@author: ravi9
"""

""" 
One of the key objectives of this chapter is to learn to write programs in the  Model-View-Controller (MVC) architecture. 
Some of the central aspects of the  MVC architecture are as follows: 
    •	A model handles backend data and logic 
    •	A view handles the frontend presentation 
    •	The model and view never interact directly 
    •	Whenever the view needs to access backend data, it requests the controller to intervene with the model and fetch the required data 
"""
from configrations import *
import pieces



captured_pieces = { 'white': [], 'black': [] }
player_turn = None
halfmove_clock = 0
fullmove_number = 1
history = []

class Model(dict):    #we are making model a child oof dict class
    def __init__(self):
        pass
    
    def get_piece_at(self, position):
        return self.get(position)
    
    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])
        
    def is_on_board(self, rowcol):
        row, col = rowcol
        return 0 <= row <= 7 and 0 <= col <= 7
    
    def reset_game_data(self):
        captured_pieces = {'white': [], 'black': []}        
        player_turn = None        
        halfmove_clock = 0        
        fullmove_number = 1        
        history = []
         
    def reset_to_initial_locations(self):         
        self.clear()         
        for position, value in START_PIECES_POSITION.items():           
            self[position] = pieces.create_piece(value)  # color argument is added just for testing           
            #self[position].keep_reference(self)         
        self.player_turn = 'white' 
    
    def test(self):
        print("it's working")
 