# tkinter for GUI
import tkinter as tk

calc = ""  # basic calculation string
def addToCalc(symbol):
    global calc
    calc += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calc)

def evaluateCalc():
    global calc
    print(calc)
    try:
        calc = str(eval(calc))
        text_results.delete(1.0, "end")
        text_results.insert(1.0, calc)
    except:
        clearField()
        text_results.insert(1.0, "Error")

def clearField():
    global calc
    calc = ""
    text_results.delete(1.0, "end")


root = tk.Tk()  # creating object ie the window for calculations
root.geometry("300x275")  # dimension of calc box

# 1st row occupied by text field
text_results = tk.Text(root, height=2, width=16, font=("Ariel", 24))
text_results.grid(columnspan=5)

bt1 = tk.Button(
    root, text="1", command=lambda: addToCalc(1), width=5, font=("Ariel", 14)
)
bt1.grid(row=2, column=1)
bt2 = tk.Button(
    root, text="2", command=lambda: addToCalc(2), width=5, font=("Ariel", 14)
)
bt2.grid(row=2, column=2)
bt3 = tk.Button(
    root, text="3", command=lambda: addToCalc(3), width=5, font=("Ariel", 14)
)
bt3.grid(row=2, column=3)
bt4 = tk.Button(
    root, text="4", command=lambda: addToCalc(4), width=5, font=("Ariel", 14)
)
bt4.grid(row=3, column=1)
bt5 = tk.Button(
    root, text="5", command=lambda: addToCalc(5), width=5, font=("Ariel", 14)
)
bt5.grid(row=3, column=2)
bt6 = tk.Button(
    root, text="6", command=lambda: addToCalc(6), width=5, font=("Ariel", 14)
)
bt6.grid(row=3, column=3)
bt7 = tk.Button(
    root, text="7", command=lambda: addToCalc(7), width=5, font=("Ariel", 14)
)
bt7.grid(row=4, column=1)
bt8 = tk.Button(
    root, text="8", command=lambda: addToCalc(8), width=5, font=("Ariel", 14)
)
bt8.grid(row=4, column=2)
bt9 = tk.Button(
    root, text="9", command=lambda: addToCalc(9), width=5, font=("Ariel", 14)
)
bt9.grid(row=4, column=3)
bt0 = tk.Button(
    root, text="0", command=lambda: addToCalc(0), width=5, font=("Ariel", 14)
)
bt0.grid(row=5, column=2)

btPlus = tk.Button(
    root, text="+", command=lambda: addToCalc("+"), width=5, font=("Ariel", 14)
)
btPlus.grid(row=2, column=4)
btSub = tk.Button(
    root, text="-", command=lambda: addToCalc("-"), width=5, font=("Ariel", 14)
)
btSub.grid(row=3, column=4)
btMul = tk.Button(
    root, text="*", command=lambda: addToCalc("*"), width=5, font=("Ariel", 14)
)
btMul.grid(row=4, column=4)
btDiv = tk.Button(
    root, text="/", command=lambda: addToCalc("/"), width=5, font=("Ariel", 14)
)
btDiv.grid(row=5, column=4)
btOpen = tk.Button(
    root, text="(", command=lambda: addToCalc("("), width=5, font=("Ariel", 14)
)
btOpen.grid(row=5, column=1)
btClose = tk.Button(
    root, text=")", command=lambda: addToCalc(")"), width=5, font=("Ariel", 14)
)
btClose.grid(row=5, column=3)
btEqual = tk.Button(
    root, text="=", command=evaluateCalc, width=12, font=("Ariel", 14)
)
btEqual.grid(row=6, column=3, columnspan=2)
btClear = tk.Button(root, text="C", command=clearField, width=12, font=("Ariel", 14))
btClear.grid(row=6, column=1, columnspan=2)

root.mainloop()  # run it here