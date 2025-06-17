from tkinter import  *
from tkinter import  messagebox
import random


class Tictactoe(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x300')
        self.title('TicTacToes')
        self.mainframe=Frame(self,width=300,height=300)

        self.fixed_state = {'A1': '', 'A2': '', 'A3': '',
                      'B1': '', 'B2': '', 'B3': '',                                             #unplayed state of the board
                      'C1': '', 'C2': '', 'C3': ''}


        self.state=self.fixed_state.copy()                                                     #played stated of the board is stored here



        self.A1=Button(self.mainframe,text='',command=lambda: self.userinput(self.A1,vari='A1'),padx=40,pady=40)
        self.A2=Button(self.mainframe,text='',command=lambda: self.userinput(self.A2,vari='A2'),padx=40,pady=40)
        self.A3=Button(self.mainframe,text='',command=lambda: self.userinput(self.A3,vari='A3'),padx=40,pady=40)
        self.B1=Button(self.mainframe,text='',command=lambda: self.userinput(self.B1,vari='B1'),padx=40,pady=40)
        self.B2=Button(self.mainframe,text='',command=lambda: self.userinput(self.B2,vari='B2'),padx=40,pady=40)
        self.B3=Button(self.mainframe,text='',command=lambda: self.userinput(self.B3,vari='B3'),padx=40,pady=40)
        self.C1=Button(self.mainframe,text='',command=lambda: self.userinput(self.C1,vari='C1'),padx=40,pady=40)
        self.C2=Button(self.mainframe,text='',command=lambda: self.userinput(self.C2,vari='C2'),padx=40,pady=40)
        self.C3=Button(self.mainframe,text='',command=lambda: self.userinput(self.C3,vari='C3'),padx=40,pady=40)

        self.fixed_computer_playable = {self.A1: 'A1', self.A2: 'A2', self.A3: 'A3', self.B1: 'B1', self.B2: 'B2',
                                  self.B3: 'B3', self.C1: 'C1', self.C2: 'C2', self.C3: 'C3'}
        self.computer_playable=self.fixed_computer_playable.copy()




        self.A1.grid(row=0,column=0)
        self.A2.grid(row=0, column=1)
        self.A3.grid(row=0, column=2)
        self.B1.grid(row=1, column=0)
        self.B2.grid(row=1, column=1)
        self.B3.grid(row=1, column=2)
        self.C1.grid(row=2, column=0)
        self.C2.grid(row=2, column=1)
        self.C3.grid(row=2, column=2)



        self.mainframe.pack()
    def userinput(self,button,vari):
        button.config(text='x',state="disabled")
        self.state[vari]='x'
        self.computer_playable.pop(button)                                                                  #selected user button operation

        self.check()
        self.computer()
    def computer(self):
        random_button=random.choice(list(self.computer_playable.items()))
        (x,y)=random_button
        x.config(text='o',state="disabled")                                                                 #computer turn (random button pick)
        self.state[y]='o'
        self.check()
        self.computer_playable.pop(x)


    def check(self):
        
        if (( self.state['A1']=='x' and self.state['A2']=='x' and self.state['A3']=='x')
                or (self.state['B1']=='x' and self.state['B2']=='x' and self.state['B3']=='x')
                or (self.state['C1']=='x' and self.state['C2']=='x' and self.state['C3']=='x')
                or ( self.state['A1']=='x' and self.state['B1']=='x' and self.state['C1']=='x')           #checks if player has combined any rows or columns of diagonal with crosses
                or (self.state['A2']=='x' and self.state['B2']=='x' and self.state['C2']=='x')
                or ( self.state['A3']=='x' and self.state['B3']=='x' and self.state['C3']=='x')
                or (self.state['A1']=='x' and self.state['B2']=='x' and self.state['C3']=='x')
                or ( self.state['A3']=='x' and self.state['B2']=='x' and self.state['C1']=='x')):
            messagebox.showinfo('result', 'player wins')
            self.state=self.fixed_state.copy()
            self.computer_playable = self.fixed_computer_playable.copy()
            for i in self.fixed_computer_playable:

                i.config(state='normal',text='')

        elif(( self.state['A1']=='o' and self.state['A2']=='o' and self.state['A3']=='o')
                or (self.state['B1']=='o' and self.state['B2']=='o' and self.state['B3']=='o')
                or (self.state['C1']=='o' and self.state['C2']=='o' and self.state['C3']=='o')
                or ( self.state['A1']=='o' and self.state['B1']=='o' and self.state['C1']=='o')         #checks if computer has combined any rows or columns of diagonal with 'o's
                or (self.state['A2']=='o' and self.state['B2']=='o' and self.state['C2']=='o')
                or ( self.state['A3']=='o' and self.state['B3']=='o' and self.state['C3']=='o')
                or (self.state['A1']=='o' and self.state['B2']=='o' and self.state['C3']=='o')
                or ( self.state['A3']=='o' and self.state['B2']=='o' and self.state['C1']=='o')):
            messagebox.showinfo('result', 'computer wins')
            self.state = self.fixed_state.copy()
            self.computer_playable = self.fixed_computer_playable.copy()
            for i in self.fixed_computer_playable:
                i.config(state='normal', text='')

        elif(self.state['A1']!='' and self.state['A2']!='' and self.state['A3']!=''
             and self.state['B1']!='' and self.state['B2']!='' and self.state['B3']!=''
             and self.state['C1']!='' and self.state['C2']!='' and self.state['C3']!=''):
            messagebox.showinfo('result', 'draw')
            self.state = self.fixed_state.copy()
            self.computer_playable = self.fixed_computer_playable.copy()
            for i in self.fixed_computer_playable:
                i.config(state='normal', text='')






app=Tictactoe()
app.mainloop()
