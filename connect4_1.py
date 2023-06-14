from tkinter import RAISED, Tk,Label, Button, Frame, Canvas, SUNKEN,TOP,LEFT,RIGHT
ROW_SIZE=6
COLUMN_SIZE=7
board=[[' ']*COLUMN_SIZE for i in range(ROW_SIZE)] #initialization of the board
root = Tk() # create one main window
labels= [1, 2, 3, 4, 5, 6 ,7] # 7 button labels
player1 = 'A'
player2 = 'B'
messageA= "Connect-4: NEXT PLAYER: {}".format(player1)
messageB= "Connect-4: NEXT PLAYER: {}".format(player2)
box_up = Canvas(root) #top canvas on the window
box_big = Canvas(root) # left canvas on the window
box_buttons=Canvas(root) # right canvas on the window
box_up.pack(side=TOP)
box_big.pack(side=LEFT)    
box_buttons.pack(side=RIGHT)

for i in range(ROW_SIZE):
    for j in range(COLUMN_SIZE):
        label = Label(box_big,relief=RAISED,borderwidth=10, padx=10, text=board[i][j]) # create 6x7 text boxes. The text should be board[i][j]
        label.grid(row=i,column=j)

def print_board(next_player, last_row, last_column):
    ''' The variable next_player means the next player (A or B).The variables last_row, last_column means the spot whether the last player puts a stone.
    If next_player is ‘A’, that means ‘B’ just finished putting a stone onto the spot board[last_row][last_column]. This function displays the 6x7 board. If there are spots that A had
    chosen, the spots should be displayed with the text ‘A’ and background color ‘red’. If there are spots that B had chosen, the spots should be displayed with the text ‘B’ and
    background color ‘blue’.'''
    global current_player
    current_player = next_player
    global label
    label=Label(box_up, text="Connect-4: NEXT PLAYER: {}".format(current_player))
    label.pack()
        
    button = Button(box_buttons, text=labels[0],command=color_change1)
    button.grid(row=0, column=0)
    button = Button(box_buttons, text=labels[1],command=color_change2)
    button.grid(row=0, column=2)
    button = Button(box_buttons, text=labels[2],command=color_change3)
    button.grid(row=0, column=4)
    button = Button(box_buttons, text=labels[3],command=color_change4)
    button.grid(row=0, column=6)
    button = Button(box_buttons, text=labels[4],command=color_change5)
    button.grid(row=0, column=8)
    button = Button(box_buttons, text=labels[5],command=color_change6)
    button.grid(row=0, column=10)
    button = Button(box_buttons, text=labels[6],command=color_change7)
    button.grid(row=0, column=12)



def color_change1():
    ''' the function that changes the background color of the lowest cell that has not been chosen on the column 1. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1 
    while(board[i][0]!= ' '):
        i=i-1
    if current_player == player1:
        board[i][0]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,0)
        one_box=Label(box_big, background="red",padx=10,text=board[i][0]) 
        one_box.grid(row=i, column=0)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][0] = player2
        check_if_there_is_a_winner(player2,i,0)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][0]) 
        one_box.grid(row=i, column=0)
        label.config(text=messageA)
        current_player = player1
     

    
def color_change2():
    ''' the function that changes the background color of the lowest cell that has not been chosen on 2nd column. Students will complete  the function .For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][1]!= ' '):
        i=i-1
    if current_player == player1:
        board[i][1]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,1)
        one_box=Label(box_big, background="red",padx=10,text=board[i][1]) 
        one_box.grid(row=i, column=1)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][1] = player2
        check_if_there_is_a_winner(player2,i,1)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][1])
        one_box.grid(row=i, column=1)
        label.config(text=messageA)
        current_player = player1
    
def color_change3():
    '''the function that changes the background color of the lowest cell that has not been chosen on 3rd column. Students will complete the function. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][2]!= ' '):
	    i=i-1
    if current_player == player1:
        board[i][2]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,2)
        one_box=Label(box_big, background="red",padx=10,text=board[i][2]) 
        one_box.grid(row=i, column=2)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][2] = player2
        check_if_there_is_a_winner(player2,i,2)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][2])
        one_box.grid(row=i, column=2)
        label.config(text=messageA)
        current_player = player1
    
def color_change4():
    '''the function that changes the background color of the lowest cell that has not been chosen on 4th column. Students will complete the function. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][3]!= ' '):
	    i=i-1
    if current_player == player1:
        board[i][3]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,3)
        one_box=Label(box_big, background="red",padx=10,text=board[i][3]) 
        one_box.grid(row=i, column=3)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][3] = player2
        check_if_there_is_a_winner(player2,i,3)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][3])
        one_box.grid(row=i, column=3)
        label.config(text=messageA)
        current_player = player1
    
def color_change5():
    '''the function that changes the background color of the lowest cell that has not been chosen on 5th column. Students will complete the function. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][4]!= ' '):
	    i=i-1
    if current_player == player1:
        board[i][4]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,4)
        one_box=Label(box_big, background="red",padx=10,text=board[i][4]) 
        one_box.grid(row=i, column=4)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][4] = player2
        check_if_there_is_a_winner(player2,i,4)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][4])
        one_box.grid(row=i, column=4)
        label.config(text=messageA)
        current_player = player1
    
def color_change6():
    '''the function that changes the background color of the lowest cell that has not been chosen on 6th column. Students will complete the function. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][5]!= ' '):
	    i=i-1
    if current_player == player1:
        board[i][5]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,5)
        one_box=Label(box_big, background="red",padx=10,text=board[i][5]) 
        one_box.grid(row=i, column=5)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][5] = player2
        check_if_there_is_a_winner(player1,i,5)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][5])
        one_box.grid(row=i, column=5)
        label.config(text=messageA)
        current_player = player1
    
def color_change7():
    '''the function that changes the background color of the lowest cell that has not been chosen on 7th column. Students will complete the function. For simplicity, assume only player A puts a stone now.'''
    global current_player
    i=ROW_SIZE-1 # the bottom cell's row number. In this function you only check the column 1
    while(board[i][-1]!= ' '):
	    i=i-1
    if current_player == player1:
        board[i][-1]= player1 # the current  i is the row number of the lowest cell that has not been chosen before on the 1st column
        check_if_there_is_a_winner(player1,i,-1)
        one_box=Label(box_big, background="red",padx=10,text=board[i][-1]) 
        one_box.grid(row=i, column=6)
        label.config(text= messageB)  #the config function is used to change settings in a widget
        current_player = player2
    elif current_player == player2:
        board[i][-1] = player2
        check_if_there_is_a_winner(player2,i,-1)
        one_box=Label(box_big, background="blue",padx=10,text=board[i][-1])
        one_box.grid(row=i, column=6)
        label.config(text=messageA)
        current_player = player1
    
#THE FOLLOWING FUNCTIONS CHECKS FOR THE WINNER OF THE GAME
def check_if_there_is_a_winner(last_player,last_row, last_col):
    '''return True if last player put 4 stones in a row around board[last_row][last_col]. Otherwise, return False'''
    if(check_stones_horizontally(last_player, last_row, last_col) == True):
        print_winning_message(last_player)
    if(check_stones_vertically(last_player, last_row, last_col) == True):
        print_winning_message(last_player)
    if(check_stones_up_right_diagonally(last_player, last_row, last_col) == True):
        print_winning_message(last_player)
    if(check_stones_down_right_diagonally(last_player, last_row, last_col) == True):
        print_winning_message(last_player)
	   
                                              
def check_stones_horizontally(last_player, last_row, last_col):
    '''return True if  last player put 4 stones in a row horizontally including the spot board[last_row][last_col].  Otherwise, return False'''
    i = 1     # this is for the index of the column
    count = 1 #the board[last_row][last_col] has the last player's stone.                 
    while(last_col-i>=0 and board[last_row][last_col-i] == last_player):
        # count the same stones adjacently on the left side of the last spot
        i = i+1
        count = count+1
    j=1
    while(last_col+j<=(COLUMN_SIZE-1) and board[last_row][last_col+j] == last_player): # count the same stones adjacently on the right side of the last spot
        j = j+1
        count = count+1
    #print('the number of stones in chain horizontally including the spot board[{}][{}] is {}'.format(last_row, last_col, count))
    if count>=4:# there exists at least a chain of at least 4 stones horizontally
        return True
    else:
        return False

	
def check_stones_vertically(last_player, last_row, last_col):
    '''return True if last player put 4 stones in a row vertically including the spot board[last_row][last_col]. Otherwise, return False'''
    i = 1 #this is for th index of the row
    count = 1
    # The board[last_row][last_col] == last_player is confirming that the entered spot is the right one, the board[last_row][last_col] has the count last player's stone.
    while(last_row-i >= 0 and board[last_row-i][last_col] == last_player):
        # this while loop will count the same stones that are adjacently above (row-i) the last spot
        i=i+1
        count = count + 1
    j = 1
    while(last_row+j<=(ROW_SIZE - 1) and board[last_row+j][last_col] == last_player):
        # this while loop will count the same stones that are adjacently below (row+j) the last spot
        j = j+1
        count = count + 1
    #print('the number of stones in chain vertically including the spot board[{}][{}] is {}'.format(last_row, last_col, count))
    if count>=4:# there exists at least a chain of at least 4 stones vertically
        return True
    else:
        return False
    
    
    
def check_stones_down_right_diagonally(last_player, last_row, last_col):
    '''return True if last player put 4 stones in a row diagonally right including the spot board[last_row][last_col]. Otherwise, return False'''
    i = 1
    j = 1 # we're comparing both the row and the column
    count = 1
    while((last_row-i >= 0 and last_col-j >= 0) and board[last_row-i][last_col-j] == last_player):
        i = i + 1
        j = j + 1
        count = count + 1
    a = 1
    b = 1
    while((last_row+a <= (ROW_SIZE - 1) and last_col+b <= (COLUMN_SIZE-1) ) and board[last_row+a][last_col+b] == last_player):
        a = a + 1
        b = b + 1
        count = count+1
    #print('the number of stones in chain down  diagonally including the spot board[{}][{}] is {}'.format(last_row, last_col, count))
    if count>=4:
        return True
    else:
        return False  
    

def check_stones_up_right_diagonally(last_player, last_row, last_col):
    '''return True if last player put 4 stones in a row diagonally right including the spot board[last_row][last_col]. Otherwise, return False'''
    i = 1
    j = 1 # we're comparing both the row and the column
    count = 1
    while((last_row-i >= 0 and last_col+j >= 0) and board[last_row-i][last_col+j] == last_player):
        i = i + 1
        j = j + 1
        count = count + 1
    a = 1
    b = 1
    while((last_row+a <= (ROW_SIZE - 1) and last_col-b <= (COLUMN_SIZE-1) ) and board[last_row+a][last_col-b] == last_player):
        a = a + 1
        b = b + 1
        count = count+1
    #print('the number of stones in chain up right diagonally including the spot board[{}][{}] is {}'.format(last_row, last_col, count))
    if count>=4:
        return True
    else:
        return False

def print_winning_message(winner):
    '''print winning message for the winner. winner can be 'A' or 'B'. Depends on which player gets the condition in check_if_there_is_a_winner() function.'''
    if winner == player1:
        label.destroy()
        winner_A = Label(box_up, text='Connect-4: ****A WON!!!****' ,background='yellow')
        winner_A.pack()
        #winner_A = 'Connect-4: ****A WON!!!****'
        #label.config(text= winner_A ,background='yellow')
    elif winner == player2:
        label.destroy()
        winner_B = Label(box_up, text='Connect-4: ****B WON!!!****',background='yellow')
        winner_B.pack()
        #winner_B = 'Connect-4: ****B WON!!!****'
        #label.config(text=winner_B,background='yellow')

    
print_board(player1, 0, 0)

root.mainloop()
