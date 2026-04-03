from tkinter import *

window= Tk()
window.title = ("Tkinter Sample Window ")
window.geometry = ('300x300')

greeting = Label(text="Hello Guys",fg='black',bg='white')
button = Button(text='Click Me',fg='black',bg='white')
entry = Entry(fg='yellow',bg='blue',width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
lable = Label(master=frame,text='Sample Frame')
lable.pack()

textbox=Text(fg='green',bg='yellow')
textbox.pack()

window.mainloop()
                   
                   