from tkinter import *


def main():

    def suvat_input(s="None", u="None", v="None", a="None", t="None"):
        # Checks which ones are present
        sCheck = uCheck = vCheck = aCheck = tCheck = True

        if s == "None":
            sCheck = False
        else:
            s = float(s)

        if u == "None":
            uCheck = False
        else:
            u = float(u)

        if v == "None":
            vCheck = False
        else:
            v = float(v)

        if a == "None":
            aCheck = False
        else:
            a = float(a)

        if t == "None":
            tCheck = False
        else:
            t = float(t)

        # Calculates the rest
        if not sCheck:
            if uCheck and tCheck and aCheck:
                s = u * t + 0.5 * a * t ** 2
            elif uCheck and vCheck and tCheck:
                s = 0.5 * (v + u) * t
            elif vCheck and uCheck and aCheck:
                s = (v ** 2 - u ** 2) / (2 * a)
            else:
                s = "ERROR! @ S"

        if not uCheck:
            if vCheck and uCheck and tCheck:
                u = v - a * t
            elif sCheck and vCheck and tCheck:
                u = (2 * s / t) - v
            elif vCheck and aCheck and sCheck:
                u = (v ** 2 - 2 * a * s) ** 0.5
            elif sCheck and tCheck and aCheck:
                u = (s / t) - 0.5 * a * t
            else:
                u = "ERROR! @ U"

        if not vCheck:
            if uCheck and aCheck and tCheck:
                v = u + a * t
            elif sCheck and tCheck and uCheck:
                v = (2 * s / t) - u
            elif uCheck and aCheck and sCheck:
                v = (u ** 2 + 2 * a * s) ** 0.5
            else:
                v = "ERROR! @ V"

        if not aCheck:
            if vCheck and uCheck and tCheck:
                a = (v - u) / t
            elif vCheck and uCheck and sCheck:
                a = (v ** 2 - u ** 2) / (2 * s)
            elif sCheck and uCheck and tCheck:
                a = 2 * (s - u * t) / t ** 2
            else:
                a = "ERROR! @ A"
        if not tCheck:
            if vCheck and uCheck and aCheck:
                t = format((v - u) / a, ".2f")
            elif sCheck and uCheck and vCheck:
                t = format(2 * s / (u + v), ".2f")
            elif uCheck and aCheck and sCheck:
                t = (format(-u / a + (2 * a * s + u ** 2) ** 0.5 / a, ".2f")
                     + "Or" + format(-u / a - (2 * a * s + u ** 2) ** 0.5 / a, ".2f"))
            else:
                t = "ERROR @ T"
        outString = ("s = %s\nu = %s\nv = %s\na = %s\nt = %s\n"
                     % (format(s, ".2f"), format(u, ".2f"), format(v, ".2f"), format(a, ".2f"), t))
        return outString

    def run():
        output.delete(1.0, END)
        s = inputS.get()
        u = inputU.get()
        v = inputV.get()
        a = inputA.get()
        t = inputT.get()

        dict1 = {"s": s, "u": u, "v": v, "a": a, "t": t}
        #dict1 = {"s": "None", "u": "0", "v": "None", "a": "10", "t": "2"}
        print(dict1)
        output.insert(END, suvat_input(**dict1))

    def reset():
        output.delete(1.0, END)
        inputS.delete(0, END)
        inputU.delete(0, END)
        inputV.delete(0, END)
        inputA.delete(0, END)
        inputT.delete(0, END)
        inputS.insert(0, "None")
        inputU.insert(0, "None")
        inputV.insert(0, "None")
        inputA.insert(0, "None")
        inputT.insert(0, "None")

    # Initialization
    root = Tk()
    root.title("SUVAT solver")
    #root.geometry("400x400")
    topGUI = Frame(root)
    middleGUI = Frame(root)
    bottomGUI = Frame(root)
    topGUI.grid(row=1)
    middleGUI.grid(row=2)
    bottomGUI.grid(row=3)

    # Top GUI Widgets
    Label(topGUI, text="Input 3 values", width=21).grid(row=1, column=1, columnspan=2, sticky=W)

    resetter = Button(topGUI, text="Reset", command=lambda: reset(), width=15)
    resetter.grid(row=1, column=3, sticky=E)

    # Middle GUI Widgets
    Label(middleGUI, text="S").grid(row=1, column=1, sticky=W)
    Label(middleGUI, text="U").grid(row=2, column=1, sticky=W)
    Label(middleGUI, text="V").grid(row=1, column=3, sticky=W)
    Label(middleGUI, text="A").grid(row=2, column=3, sticky=W)
    Label(middleGUI, text="T").grid(row=1, column=5, sticky=W)
    runner = Button(middleGUI, text="Run", command=lambda: run(), width=15)
    runner.grid(row=2, column=5, columnspan=2)

    inputS = Entry(middleGUI, width=10)
    inputU = Entry(middleGUI, width=10)
    inputV = Entry(middleGUI, width=10)
    inputA = Entry(middleGUI, width=10)
    inputT = Entry(middleGUI, width=10)

    inputS.grid(row=1, column=2, sticky=W)
    inputU.grid(row=2, column=2, sticky=W)
    inputV.grid(row=1, column=4, sticky=W)
    inputA.grid(row=2, column=4, sticky=W)
    inputT.grid(row=1, column=6, sticky=W)

    # Bottom GUI Widgets
    output = Text(bottomGUI, width=30, height=6)
    output.grid(row=1)
    Button(bottomGUI, width=30, text="QUIT", command=root.destroy, fg="red").grid(row=2)
    reset()
    root.mainloop()


if __name__ == '__main__':
    main()
