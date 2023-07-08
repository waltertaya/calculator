from tkinter import *

def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    operator = entry_operator.get()
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '^':
        result = num1**num2
    else:
        result = 'invalid operator try again'
    
    label.configure(text = 'Answer {}'.format(result))
    entry1.delete(0,END)
    entry_operator.delete(0,END)
    entry2.delete(0,END)

root = Tk()

label_input = Label(text = 'Enter the value',font = ('Verdana', 16))
label = Label(font = ('Verdana', 16))
entry1 = Entry(font = ('Verdana',10),width = 4)
entry_operator = Entry(font = ('Verdana',10),width = 4)
entry2 = Entry(font = ('Verdana',10),width = 4)
button = Button(text = 'calculate', font = ('Verdana', 16),command = calculate)

label_input.grid(row = 0,column = 0)
label.grid(row = 1,column = 0)
button.grid(row = 1,column = 1,columnspan = 3)
entry1.grid(row = 0,column = 1)
entry_operator.grid(row = 0,column = 2)
entry2.grid(row = 0,column = 3)

mainloop()