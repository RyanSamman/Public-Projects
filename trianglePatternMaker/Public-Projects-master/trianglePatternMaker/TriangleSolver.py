from tkinter import *
from patterns import *


def run():
    pattern_chooser = var.get()
    x = input_one.get()
    out_string = ""

    try:
        x = eval(x)
        y = 2 if x >= 10 else 1

        if x > 20:
            print("ERROR, INPUT MORE THAN 20")
            out_string = "Enter a number smaller or equal to 20"
        elif x <= 20:
            list1 = ["Select a Pattern", pattern1(x, y), pattern2(x, y), pattern3(x, y), pattern4(x, y)]
            out_string = list1[pattern_chooser]
    except:
        print("ERROR, INPUT NOT A NUMBER")
        out_string = "Enter a valid number"

    output_one.delete(1.0, END)
    output_one.insert(1.0, out_string)


def reset():
    output_one.delete(1.0, END)
    input_one.delete(0, END)


def main():
    global var, input_one, output_one

    root = Tk()
    root.title("~~ Pattern Generator ~~")
    top_gui = Frame(root)
    top_gui.grid(row=1)
    bottom_gui = Frame(root)
    bottom_gui.grid(row=2)

    # Top GUI
    Label(top_gui, text="Enter size of pattern:", width=34).grid(row=1, column=1)
    runner = Button(top_gui, text="Run", width=34, command=lambda: run())
    runner.grid(row=1, column=2)

    input_one = Entry(top_gui, width=40)
    input_one.grid(row=2, column=1, columnspan=1)
    input_one.insert(0, "6")

    Button(top_gui, text="Reset", command=lambda: reset(), width=34).grid(row=2, column=2)

    # Bottom GUI
    output_one = Text(bottom_gui, width=60, height=20, background="light gray")
    output_one.grid(row=2, column=1)
    Button(bottom_gui, width=68, text="QUIT", command=root.destroy, fg="red").grid(row=3, column=1)

    # ~~~~~~~~~~~~~~~~ Radios ~~~~~~~~~~~~~~~~
    var = IntVar()
    r1 = Radiobutton(top_gui, text="Pattern 1", variable=var, value=1, command=lambda: run())
    r1.grid(row=3, column=1)

    r2 = Radiobutton(top_gui, text="Pattern 2", variable=var, value=2, command=lambda: run())
    r2.grid(row=3, column=2)

    r3 = Radiobutton(top_gui, text="Pattern 3", variable=var, value=3, command=lambda: run())
    r3.grid(row=4, column=1)

    r4 = Radiobutton(top_gui, text="Pattern 4", variable=var, value=4, command=lambda: run())
    r4.grid(row=4, column=2)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    root.mainloop()


if __name__ == '__main__':
    main()
