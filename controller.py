# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:51:11 2019

@author: ravi9
"""
from configrations import *
import pieces
import model

class Controller():
    def __init__(self):
        self.init_model()
    
    """Note that since the Controller class needs to fetch data from the Model class,
    we instantiated a new Model class from within the Controller class.
    This now provides us a way to fetch data from the Model class as and when needed. """   
    
    def init_model(self):
        self.model = model.Model()
        
    def get_numeric_notation(self, position):        
        return pieces.get_numeric_notation(position) 
    
    def get_all_peices_on_chess_board(self):        
        return self.model.items() 
    
    def reset_game_data(self):        
        self.model.reset_game_data()
    
    def reset_to_initial_locations(self):        
        self.model.reset_to_initial_locations()
        
    
        
