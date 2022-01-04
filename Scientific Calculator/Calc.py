from tkinter import *

expression = ""


def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="gray")
    gui.title("Simple Calculator")
    gui.geometry("260x205")

    equation = StringVar()

    expression_field = Entry(gui, width=40, state='readonly', background='red', textvariable=equation)
    expression_field.grid(row=0, columnspan=10, ipadx=6, ipady=8)
    expression_field.focus()


    # COLUMN 1 - 7 8 9 #
    button7 = Button(gui, text=' 7 ', fg='white', bg='black', command=lambda: press(7), width=8)
    button7.grid(row=1, column=0, ipady=4, ipadx=2)

    button8 = Button(gui, text=' 8 ', fg='white', bg='black', command=lambda: press(8), width=8)
    button8.grid(row=1, column=1, ipady=4, ipadx=2)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black', command=lambda: press(9), width=8)
    button9.grid(row=1, column=2, ipady=4, ipadx=2)


    # COLUMN 2 - 4 5 6 #
    button4 = Button(gui, text=' 4 ', fg='white', bg='black', command=lambda: press(4), width=8)
    button4.grid(row=2, column=0, ipady=4, ipadx=2)

    button5 = Button(gui, text=' 5 ', fg='white', bg='black', command=lambda: press(5), width=8)
    button5.grid(row=2, column=1, ipady=4, ipadx=2)

    button6 = Button(gui, text=' 6 ', fg='white', bg='black', command=lambda: press(6), width=8)
    button6.grid(row=2, column=2, ipady=4, ipadx=2)


    # COLUMN 3 - 1 2 3 #
    button1 = Button(gui, text=' 1 ', fg='white', bg='black', command=lambda: press(1), width=8)
    button1.grid(row=3, column=0, ipady=4, ipadx=2)

    button2 = Button(gui, text=' 2 ', fg='white', bg='black', command=lambda: press(2), width=8)
    button2.grid(row=3, column=1, ipady=4, ipadx=2)

    button3 = Button(gui, text=' 3 ', fg='white', bg='black', command=lambda: press(3), width=8)
    button3.grid(row=3, column=2, ipady=4, ipadx=2)


    # COLUMN 4 - Clean 0 . #
    button_Clear = Button(gui, text=' C ', fg='white', bg='red', command=clear, width=8)
    button_Clear.grid(row=4, column=0, ipady=4, ipadx=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='black', command=lambda: press(0), width=8)
    button0.grid(row=4, column=1, ipady=4, ipadx=2)

    button_dec = Button(gui, text=' . ', fg='white', bg='black', command=lambda: press('.'), width=8)
    button_dec.grid(row=4, column=2, ipady=4, ipadx=2)

    # COLUMN 5 - = #
    button_equal = Button(gui, text=' = ', fg='white', bg='green', command=equalpress, width=8)
    button_equal.grid(row=5, column=1, ipady=4, ipadx=2)


    # GRID 4 #
    button_plus = Button(gui, text=' + ', fg='white', bg='black', command=lambda: press("+"), width=5)
    button_plus.grid(row=1, column=3, ipady=4, ipadx=2)

    button_minus = Button(gui, text=' - ', fg='white', bg='black', command=lambda: press("-"), width=5)
    button_minus.grid(row=2, column=3, ipady=4, ipadx=2)

    button_mult = Button(gui, text=' * ', fg='white', bg='black', command=lambda: press("*"), width=5)
    button_mult.grid(row=3, column=3, ipady=4, ipadx=2)

    button_div = Button(gui, text=' / ', fg='white', bg='black', command=lambda: press("/"), width=5)
    button_div.grid(row=4, column=3, ipady=4, ipadx=2)

    gui.mainloop()