from tkinter import *
from numpy import *
from random import *
from tkinter import messagebox
import os
    






def check_win(player):
    if(board[0][0]==board[1][1]==board[2][2]==player):
        return player,"win"
    if(board[0][2]==board[1][1]==board[2][0]==player):
        return player,"win"
    for i in range(0,3):
        if(board[0][i]==board[1][i]==board[2][i]==player):
            return player,"win"
    for i in range(0,3):
        if(board[i][0]==board[i][1]==board[i][2]==player):
            return player,"win"
    return player,"no"



def check_computer_mark():
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==0):
                if(i==0 and j==0):
                     btn00["text"]="0"
                     btn00.configure(state=DISABLED)
                if(i==0 and j==1):
                     btn01["text"]="0"
                     btn01.configure(state=DISABLED)
                if(i==0 and j==2):
                     btn02["text"]="0"
                     btn02.configure(state=DISABLED)
                if(i==1 and j==0):
                     btn10["text"]="0"
                     btn10.configure(state=DISABLED)
                if(i==1 and j==1):
                     btn11["text"]="0"
                     btn11.configure(state=DISABLED)
                if(i==1 and j==2):
                     btn12["text"]="0"
                     btn12.configure(state=DISABLED)
                if(i==2 and j==0):
                     btn20["text"]="0"
                     btn20.configure(state=DISABLED)
                if(i==2 and j==1):
                     btn21["text"]="0"
                     btn21.configure(state=DISABLED)
                if(i==2 and j==2):
                     btn22["text"]="0"
                     btn22.configure(state=DISABLED)


             

def computerPlayer():
    try:
        index1 = randint(0,2)
        index2 = randint(0,2)
        if(board[index1][index2]==5):
            board[index1][index2]=0
            check_computer_mark()
        else:
            computerPlayer()
    except:
        MsgBox = messagebox.askquestion ('Match Draw','Match Draw \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
        


def btn00Pressed():
    board[0][0]=1
    btn00["text"]="X"
    btn00.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()

        
    



def btn01Pressed():
    board[0][1]=1
    btn01["text"]="X"
    btn01.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
        
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()


    
def btn02Pressed():
    board[0][2]=1
    btn02["text"]="X"
    btn02.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()


    
def btn10Pressed():
    board[1][0]=1
    btn10["text"]="X"
    btn10.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()

    
def btn11Pressed():
    board[1][1]=1
    btn11["text"]="X"
    btn11.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()
    
def btn12Pressed():
    board[1][2]=1
    btn12["text"]="X"
    btn12.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()


def btn20Pressed():
    board[2][0]=1
    btn20["text"]="X"
    btn20.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()
    
def btn21Pressed():
    board[2][1]=1
    btn21["text"]="X"
    btn21.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()
    
def btn22Pressed():
    board[2][2]=1
    btn22["text"]="X"
    btn22.configure(state=DISABLED)
    plyr,status=check_win(1)
    if(status=="win"):
        MsgBox = messagebox.askquestion ('Winner','Player X Wins \nDo Want To Play Again ?',icon = 'warning')
        if MsgBox == 'yes':
            main.destroy()
            os.system('python Tic_Tac_Toe.py') 
        else:
            main.destroy()
    else:
        computerPlayer()
        plyr,status=check_win(0)
        if(status=="win"):
            MsgBox = messagebox.askquestion ('Winner','Player 0 Wins \nDo Want To Play Again ?',icon = 'warning')
            if MsgBox == 'yes':
                main.destroy()
                os.system('python Tic_Tac_Toe.py') 
            else:
                main.destroy()

board=array([[5,5,5],[5,5,5],[5,5,5]])




main = Tk()
frame=Frame(main)
frame.pack() 
topframe = Frame(main) 
topframe.pack() 
main.title("Tic Tac Toe")
btn00=Button(topframe, text='', width=10, height=5, command=btn00Pressed) 
btn00.pack(side=LEFT)
btn01=Button(topframe, text='', width=10, height=5, command=btn01Pressed) 
btn01.pack(side=LEFT)
btn02=Button(topframe, text='', width=10, height=5, command=btn02Pressed) 
btn02.pack(side=LEFT)
midleframe = Frame(main) 
midleframe.pack() 
btn10=Button(midleframe, text='', width=10, height=5, command=btn10Pressed) 
btn10.pack(side=LEFT)
btn11=Button(midleframe, text='', width=10, height=5, command=btn11Pressed) 
btn11.pack(side=LEFT)
btn12=Button(midleframe, text='', width=10, height=5, command=btn12Pressed) 
btn12.pack(side=LEFT)
bottomframe = Frame(main) 
bottomframe.pack()
btn20=Button(bottomframe, text='', width=10, height=5, command=btn20Pressed) 
btn20.pack(side=LEFT)
btn21=Button(bottomframe, text='', width=10, height=5, command=btn21Pressed) 
btn21.pack(side=LEFT)
btn22=Button(bottomframe, text='', width=10, height=5, command=btn22Pressed) 
btn22.pack(side=LEFT)

main.mainloop()
