import tkinter as tk
from tkinter import ttk

prevAnswer = ""
number = ""

operationType = '*'

#makes the window and mainloop
root = tk.Tk()
root.title("Calculator")
frm = ttk.Frame(root, padding=10)

frm.grid()

#functions
# Updates the value in the label
def Update_Label(num):
    for widget in frm.grid_slaves(column=0, row=0):
        widget.grid_forget()
    ttk.Label(frm, text=num, anchor="e").grid(column=0, row=0, columnspan=4, sticky="ew")

#updates the number that gets put in label
def Update_Number(num):
    global number
    number = number + num

    Update_Label(number)

def Get_Answer():
    global prevAnswer, number, equationType

    match operationType:
        case '+':
            number = str(float(prevAnswer) + float(number))
            Update_Label(number)
            number = ""
        case '-':
            number = str(float(prevAnswer) - float(number))
            Update_Label(number)
            number = ""
        case 'x':
            number = str(float(prevAnswer) * float(number))
            Update_Label(number)
            number = ""
        case _:
            print("no operation selected")
        

def Set_Operation(operation):
    global operationType, prevAnswer, number
    operationType = operation
    prevAnswer = number
    number = ""
    Update_Label(number)

def Clear_Entry():
    global number, prevAnswer
    if number == "":
        prevAnswer = ""
    else:
        number = ""
    Update_Label(number)


ttk.Label(frm, text=number, anchor="e").grid(column=0, row=0, columnspan=4, sticky="ew")


#buttons:
#numbers starting from top row
ttk.Button(frm, text="9", command=lambda : Update_Number("9")).grid(column=2, row=1)
ttk.Button(frm, text="8", command=lambda : Update_Number("8")).grid(column=1, row=1)
ttk.Button(frm, text="7", command=lambda : Update_Number("7")).grid(column=0, row=1)

ttk.Button(frm, text="6", command=lambda : Update_Number("6")).grid(column=2, row=2)
ttk.Button(frm, text="5", command=lambda : Update_Number("5")).grid(column=1, row=2)
ttk.Button(frm, text="4", command=lambda : Update_Number("4")).grid(column=0, row=2)

ttk.Button(frm, text="3", command=lambda : Update_Number("3")).grid(column=2, row=3)
ttk.Button(frm, text="2", command=lambda : Update_Number("2")).grid(column=1, row=3)
ttk.Button(frm, text="1", command=lambda : Update_Number("1")).grid(column=0, row=3)

ttk.Button(frm, text="0", command=lambda : Update_Number("0")).grid(column=0, row=4)
ttk.Button(frm, text=".", command=lambda : Update_Number(".")).grid(column=1, row=4)

ttk.Button(frm, text="=", command=lambda : Get_Answer()).grid(column=2, row=4)

ttk.Button(frm, text="CE", command=lambda : Clear_Entry()).grid(column=3, row=1)

#operations
ttk.Button(frm, text="+", command=lambda : Set_Operation('+')).grid(column=3, row=3)
ttk.Button(frm, text="-", command=lambda : Set_Operation('-')).grid(column=3, row=2)
ttk.Button(frm, text="x", command=lambda : Set_Operation('x')).grid(column=3, row=4)

root.mainloop()
