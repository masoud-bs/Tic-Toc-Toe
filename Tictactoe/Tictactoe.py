
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import numpy as np
import ctypes
import pygame
from pygame.locals import *
from tkinter import messagebox





# class MainUi(QMainWindow):
#     def __init__(self):
#         super(MainUi, self).__init__() # Call the inherited classes __init__ method
#         uic.loadUi("Images/menubar.ui", self) # Load the .ui file
        
#         self.actionNew_Game.triggered.connect(self.newPressed)
#     def newPressed(self):
#         print('hi')
  
#Draw Board
def draw_board(board):
    for row in range(6):
        for col in range(6):
            if board[row][col] == 'X':
                screen.blit(p1_img, ((col * 100) + 5 , (row * 100) ))

            elif board[row][col] == 'O':
                screen.blit(p2_img, ((col * 100) + 11 , (row * 100) + 10))

#Fotos as Icon Hinzufügen
def check(player, y, x):
        if player == 1:
            boardlist[y][x] = 'X'
            check_win_HV(boardlist, 'X')
        else:
            boardlist[y][x] = 'O'
            check_win_HV(boardlist, 'O')

#Check Winner
def check_win_HV(boardlist, element):
    arindex = []
    #Horizontal
    for i in range(6):
        for j in range(3):
            if (boardlist[i][j] == boardlist[i][j+1] == boardlist[i][j+2] == boardlist[i][j+3] == element):
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 1, element)
    #Vertikal
    for i in range(3):
        for j in range(6):            
            if (boardlist[i][j] == boardlist[i+1][j] == boardlist[i+2][j] == boardlist[i+3][j] == element):
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 2, element)   

    #Diagonal --->>>               
    for i in range(3):
        for j in range(3):
            # Check diagonal from top-left to bottom-right
            if (boardlist[i][j] == boardlist[i+1][j+1] == boardlist[i+2][j+2] == boardlist[i+3][j+3]) and boardlist[i][j] == element:
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 3, element)
                
            # Check diagonal from bottom-left to top-right
            if (boardlist[i+3][j] == boardlist[i+2][j+1] == boardlist[i+1][j+2] == boardlist[i][j+3]) and boardlist[i+3][j] == element:
                ind1 = [i+3,j]
                arindex.append(ind1) 
                farbe(arindex, 4, element)
                

def farbe(indexx, num, element):
    
    if num == 1:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row +  50)), ((col + x + 100) , (row + 50)), 101)

    if num == 2:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + 100) , (row + x +  50)), ((col) , (row + x + 50)), 101)

    if num == 3:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row + x + 50)), ((col + x + 100) , (row + x + 50)), 101)

    if num == 4:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row - x + 50)), ((col + x + 100) , (row - x + 50)), 101)
    
    update_break(element)

#PopUp
def popup(element):
    messageBox = ctypes.windll.user32.MessageBoxW
    if element == 'end':
        a = 'Gamedraw : Niemand hat gewonnen'
    else:
        a =  element + " hat gewonnen"
    
    returnValue = messageBox(None, a,"Game Over",0x70 | 0x0)


    if returnValue == 1:
        #Muss Hauptmenu ------>>>>>>>>>>>>>>>>>
        print("Game Over")
        pygame.quit()
        sys.exit()

#Update Screen and Break   
def update_break(element):
    draw_board(boardlist)
    pygame.display.update()
    finish(element)


def finish(element):
    popup(element)
    pygame.display.update()
    

pygame.init()      
#Fenster Große
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Fenster erstellen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg_img = pygame.image.load('Images/BG_tic2.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe 6x6')

#Images
screen.blit(bg_img, (0, 0))
p1_img = pygame.image.load('Images/x1.png')
p1_img = pygame.transform.scale(p1_img, (90, 90))

p2_img = pygame.image.load('Images/o.jpg')
p2_img = pygame.transform.scale(p2_img, (80, 80))

#Main Array
boardlist = np.array([
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-']])
    

# app = QApplication(sys.argv)
# ui = MainUi()
# ui.show()
# app.exec_()

#tart = loop_tictoctor()   
player = 1
count_draw = 0
while True:
    draw_board(boardlist)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                b = pygame.mouse.get_pos()
                x = int(b[0] / 100)
                y = int(b[1] / 100)
                if boardlist[y][x] == '-':
                    check(player, y, x)
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                    count_draw += 1
                    if count_draw == 36:
                        draw_board(boardlist)
                        pygame.display.update()
                        popup('end')
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                messageBox = ctypes.windll.user32.MessageBoxW
                value = messageBox(None, 'Exit ? ',"Pause",0x70 | 0x2)
                if value == 5:
                    print('NIchts')
                elif value == 4:
                    print('Restart')
                elif value == 3:
                    print('Hauptmenu')
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()