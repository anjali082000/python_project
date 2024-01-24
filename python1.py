#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = [' ']*10


# In[2]:


board[0] = '$'


# In[3]:


board


# In[4]:


from IPython.display import clear_output 
def display_board(board):
    clear_output()
    print(f'{board[1]} |{board[2]} | {board[3]}')
    print(f'{board[4]} |{board[5]} | {board[6]}')
    print(f'{board[7]} |{board[8]} | {board[9]}')


# In[5]:


def check_win(player):
    if board[1]==board[2]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    elif board[3]==board[6]==board[9] and board[3]!=' ':
        return True
    elif board[1]==board[5]==board[9] and board[1]!=' ':
        return True
    elif board[3]==board[5]==board[7] and board[3]!=' ':
        return True
    else: 
        return False


# In[6]:


current_player = 'X'   


# In[7]:


while  True:
    display_board(board)
    
    move = int(input(f"{current_player} Enter a number"))
    if board[move]!=' ':
        print("Space occupied")
        move=int(input("enter a number between 1-9 for {current_player}"))
    board[move] = current_player
    
    if check_win(current_player):
        print(f'{current_player} wins')
        break
    if ' ' not in board:
        print('Draw')
        break

        
    
    if current_player == 'X':
        current_player='O'
    else:
        current_player='X'
    


# In[ ]:




