# ----*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:59:39 2019

@author: ravi9
"""

NUMBER_OF_ROWS = 8 
NUMBER_OF_COLUMNS = 8 
DIMENSION_OF_EACH_SQUARE = 100 # denoting 64 pixels 
BOARD_COLOR_1 =  "#DDB88C" 
BOARD_COLOR_2 = "#A66D4F"

X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H') 
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7, 8)

SHORT_NAME = {
'R':'Rook', 'N':'Knight', 'B':'Bishop',
'Q':'Queen', 'K':'King', 'P':'Pawn'
}

START_PIECES_POSITION = {"A8": "r", "B8": "n", "C8": "b", "D8": "q", "E8": "k", "F8": "b", "G8": "n", "H8": "r",    
                         "A7": "p", "B7": "p", "C7": "p", "D7": "p", "E7": "p", "F7": "p", "G7": "p", "H7": "p",    
                         "A2": "P", "B2": "P", "C2": "P", "D2": "P", "E2": "P", "F2": "P", "G2": "P", "H2": "P",    
                         "A1": "R", "B1": "N", "C1": "B", "D1": "Q", "E1": "K", "F1": "B", "G1": "N", "H1": "R" }

"""To make these constant values available to all the files, let's import it in model.py, view.py,
 and controller.py folder (see code 4.01). """
 
