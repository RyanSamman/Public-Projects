from tkinter import *
from patterns import *


def main():
    def run():
        pattern_chooser = var.get()
        x = eval(input_one.get())
        y = 2 if x >= 10 else 1

        list1 = ["Select a Pattern", pattern1(x, y), pattern2(x, y), pattern3(x, y), pattern4(x, y)]
        outstring = list1[pattern_chooser]
        output_one.delete(1.0, END)
        output_one.insert(1.0, outstring)

    def reset():
        output_one.delete(1.0, END)
        input_one.delete(0, END)

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
    R1 = Radiobutton(top_gui, text="Pattern 1", variable=var, value=1, command=lambda: run())
    R1.grid(row=3, column=1)

    R2 = Radiobutton(top_gui, text="Pattern 2", variable=var, value=2, command=lambda: run())
    R2.grid(row=3, column=2)

    R3 = Radiobutton(top_gui, text="Pattern 3", variable=var, value=3, command=lambda: run())
    R3.grid(row=4, column=1)

    R3 = Radiobutton(top_gui, text="Pattern 4", variable=var, value=4, command=lambda: run())
    R3.grid(row=4, column=2)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    root.mainloop()


if __name__ == '__main__':
    main()
