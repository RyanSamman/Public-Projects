from tkinter import *


def main():

    def suvat_input(s="", u="", v="", a="", t=""):
        # Checks which ones are present
        s_present = u_present = v_present = a_present = t_present = True

        if s == "":
            s_present = False
        else:
            try:
                s = float(s)
            except:
                s_present = False

        if u == "":
            u_present = False
        else:
            try:
                u = float(u)
            except:
                u_present = False

        if v == "":
            v_present = False
        else:
            try:
                v = float(v)
            except:
                v_present = False

        if a == "":
            a_present = False
        else:
            try:
                a = float(a)
            except:
                a_present = False

        if t == "":
            t_present = False
        else:
            try:
                t = float(t)
            except:
                t_present = False

        # Calculates the rest
        if not s_present:
            if u_present and t_present and a_present:
                s = u * t + 0.5 * a * t ** 2
                s_present = True
            elif u_present and v_present and t_present:
                s = 0.5 * (v + u) * t
                s_present = True
            elif v_present and u_present and a_present:
                s = (v ** 2 - u ** 2) / (2 * a)
                s_present = True
            else:
                s = "ERROR! @ S"

        if not u_present:
            if v_present and u_present and t_present:
                u = v - a * t
                u_present = True
            elif s_present and v_present and t_present:
                u = (2 * s / t) - v
                u_present = True
            elif v_present and a_present and s_present:
                u = (v ** 2 - 2 * a * s) ** 0.5
                u_present = True
            elif s_present and t_present and a_present:
                u = (s / t) - 0.5 * a * t
                u_present = True
            else:
                u = "ERROR! @ U"

        if not v_present:
            if u_present and a_present and t_present:
                v = u + a * t
                v_present = True
            elif s_present and t_present and u_present:
                v = (2 * s / t) - u
                v_present = True
            elif u_present and a_present and s_present:
                v = (u ** 2 + 2 * a * s) ** 0.5
                v_present = True
            else:
                v = "ERROR! @ V"

        if not a_present:
            if v_present and u_present and t_present:
                a = (v - u) / t
                a_present = True
            elif v_present and u_present and s_present:
                a = (v ** 2 - u ** 2) / (2 * s)
                a_present = True
            elif s_present and u_present and t_present:
                a = 2 * (s - u * t) / t ** 2
                a_present = True
            else:
                a = "ERROR! @ A"
        if not t_present:
            if v_present and u_present and a_present:
                t = format((v - u) / a, ".2f")
                t_present = True
            elif s_present and u_present and v_present:
                t = format(2 * s / (u + v), ".2f")
                t_present = True
            elif u_present and a_present and s_present:
                t = (format(-u / a + (2 * a * s + u ** 2) ** 0.5 / a, ".2f")
                     + "Or" + format(-u / a - (2 * a * s + u ** 2) ** 0.5 / a, ".2f"))
                t_present = True
            else:
                t = "ERROR @ T"

        if s_present and u_present and v_present and a_present and t_present:
            out_string = ("s = %s\nu = %s\nv = %s\na = %s\nt = %s\n"
                          % (format(s, ".2f"), format(u, ".2f"), format(v, ".2f"), format(a, ".2f"), t))
        else:
            out_string = (
                          "ERROR:" +
                          "\n Displacement: {s}" +
                          "\n Initial Velocity: {u}" +
                          "\n Final Velocity: {v}" +
                          "\n Accelleration: {a}" +
                          "\n Time:  + {t}" +
                          "INPUT AT LEAST 3 VALID NUMBERS INTO GUI"
                          ).format(s=s_present, u=u_present, v=v_present, a=a_present, t=t_present)

        return out_string

    def run():
        output.delete(1.0, END)
        s = inputS.get()
        u = inputU.get()
        v = inputV.get()
        a = inputA.get()
        t = inputT.get()

        dict1 = {"s": s, "u": u, "v": v, "a": a, "t": t}
        # dict1 = {"s": "None", "u": "0", "v": "None", "a": "10", "t": "2"}  # Testing code
        print(dict1)
        output.insert(END, suvat_input(**dict1))

    def reset():
        output.delete(1.0, END)
        inputS.delete(0, END)
        inputU.delete(0, END)
        inputV.delete(0, END)
        inputA.delete(0, END)
        inputT.delete(0, END)
        inputS.insert(0, "")
        inputU.insert(0, "")
        inputV.insert(0, "")
        inputA.insert(0, "")
        inputT.insert(0, "")

    # Initialization
    root = Tk()
    root.title("SUVAT solver")
    root.geometry("400x400")
    top_gui = Frame(root)
    middle_gui = Frame(root)
    bottom_gui = Frame(root)
    top_gui.grid(row=1)
    middle_gui.grid(row=2)
    bottom_gui.grid(row=3)

    # Top GUI Widgets
    Label(top_gui, text="Input 3 values", width=21).grid(row=1, column=1, columnspan=2, sticky=W)

    reset_button = Button(top_gui, text="Reset", command=lambda: reset(), width=15)
    reset_button.grid(row=1, column=3, sticky=E)

    # Middle GUI Widgets
    Label(middle_gui, text="S").grid(row=1, column=1, sticky=W)
    Label(middle_gui, text="U").grid(row=2, column=1, sticky=W)
    Label(middle_gui, text="V").grid(row=1, column=3, sticky=W)
    Label(middle_gui, text="A").grid(row=2, column=3, sticky=W)
    Label(middle_gui, text="T").grid(row=1, column=5, sticky=W)
    run_button = Button(middle_gui, text="Run", command=lambda: run(), width=15)
    run_button.grid(row=2, column=5, columnspan=2)

    inputS = Entry(middle_gui, width=10)
    inputU = Entry(middle_gui, width=10)
    inputV = Entry(middle_gui, width=10)
    inputA = Entry(middle_gui, width=10)
    inputT = Entry(middle_gui, width=10)

    inputS.grid(row=1, column=2, sticky=W)
    inputU.grid(row=2, column=2, sticky=W)
    inputV.grid(row=1, column=4, sticky=W)
    inputA.grid(row=2, column=4, sticky=W)
    inputT.grid(row=1, column=6, sticky=W)

    # Bottom GUI Widgets
    output = Text(bottom_gui, width=30, height=6)
    output.grid(row=1)
    Button(bottom_gui, width=30, text="QUIT", command=root.destroy, fg="red").grid(row=2)
    reset()
    root.mainloop()


if __name__ == '__main__':
    main()
