## -*- coding: utf-8 -*-
#"""
#Created on Mon Jun 17 22:51:02 2019
#
#@author: ravi9
#"""
from configrations import *
import controller
import tkinter as tk
from tkinter import *
#
class View():
    
    images = {}
    board_color_1 = BOARD_COLOR_1
    board_color_2 = BOARD_COLOR_2
    
    def __init__(self):
        self.view_chess_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.controller = controller.Controller()
        self.start_new_game()
        
    
    
    def view_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()
    
    def create_top_menu(self):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open", command=None)
        filemenu.add_command(label="Save", command=None)
        filemenu.add_command(label="Save as...", command=None)
        filemenu.add_command(label="Close", command=None)
        
        filemenu.add_separator()
#        
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)


        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=None)
        
        editmenu.add_separator()
        
        editmenu.add_command(label="Cut", command=None)
        editmenu.add_command(label="Copy", command=None)
        editmenu.add_command(label="Paste", command=None)
        editmenu.add_command(label="Delete", command=None)
        editmenu.add_command(label="Select All", command=None)
        
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=None)
        helpmenu.add_command(label="About...", command=None)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        root.config(menu=menubar)
        
        
    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE        
        self.canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")        
        self.canvas.pack(padx=8, pady=8) 
        
    def draw_board(self):        
        current_color = BOARD_COLOR_2        
        for row in range(NUMBER_OF_ROWS):            
            current_color = self.get_alternate_color(current_color)            
            for col in range(NUMBER_OF_COLUMNS):                
                x1, y1 = self.get_x_y_coordinate(row, col)                
                x2= x1 + DIMENSION_OF_EACH_SQUARE
                y2 =  y1 + DIMENSION_OF_EACH_SQUARE                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=current_color)
                current_color =self.get_alternate_color(current_color)
#    
    def get_x_y_coordinate(self, row, col):
        x = (col * DIMENSION_OF_EACH_SQUARE)        
        y = ((7 - row) * DIMENSION_OF_EACH_SQUARE)        
        return (x, y)
#    
    def get_alternate_color(self, current_color):        
        if current_color == BOARD_COLOR_2:            
            next_color = BOARD_COLOR_1        
        else:            
            next_color = BOARD_COLOR_2        
        
        return next_color

        
    def create_bottom_frame(self):

        self.bottom_frame = Frame(root, height=64)
        self.info_label = Label(self.bottom_frame, text="   White to Start the Game  ", fg="black")
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")
        
    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        print("Hey you clicked on : ", clicked_row, clicked_column)
        
    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = event.y // row_size
        return(clicked_row, clicked_column)
        
    def draw_single_piece(self, position, piece):

        x, y = self.controller.get_numeric_notation(position)
        if piece:
            filename = "pieces_image/{}_{}.png".format(
                piece.name.lower(), piece.color)
            if filename not in self.images:
                self.images[filename] = PhotoImage(file=filename)
            x0, y0 = self.calculate_piece_coordinate(x, y)
            self.canvas.create_image(x0, y0, image=self.images[
                                     filename], tags=("occupied"), anchor="c")


            
    def calculate_piece_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + int(DIMENSION_OF_EACH_SQUARE/2)
        y0 = ((7-row) * DIMENSION_OF_EACH_SQUARE) + int(DIMENSION_OF_EACH_SQUARE/2)
        return (x0, y0)
    
    def draw_all_pieces(self):        
        self.canvas.delete("occupied")        
        for position, piece in self.controller.get_all_peices_on_chess_board():            
            self.draw_single_piece(position, piece) 
    
    def start_new_game(self): 
        self.controller.reset_game_data()
        self.controller.reset_to_initial_locations()        
        self.draw_all_pieces()
        
        
# if __init__ == __main__:
root = tk.Tk()
root.geometry('800x800')
View()
root.mainloop()
