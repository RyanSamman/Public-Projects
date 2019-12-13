from tkinter import *


def is_prime(integer) -> bool:
    '''
    :param integer: is the input number (as a type integer) which you want to check
    :return: Returns True if "integer" is a prime number, False if "integer" is NOT a prime number
    '''
    if integer < 2:
        return False
    if integer == 2:
        return True
    else:
        for divider in range(2, integer//2):
            if integer % divider == 0:
                return False
        return True


def get_prime_list(number):
    # Generates a list of prime numbers with a list length of number
    # Example =
    prime_list = []
    count = i = 0
    while True:
        if count == number:
            break
        if is_prime(i):
            prime_list.append(i)
            count += 1
        i += 1
    return prime_list


def prime_output(number_primes, number_per_line):
    count = 0
    string = ""
    prime_list = get_prime_list(number_primes)
    for i in prime_list:
        if count == number_per_line:
            string += "\n"
            count = 0
        string += format(i, "5d") + ","
        count += 1
    return string


def main():

    def run():
        nonlocal input_one
        x = int(input_one.get())
        output_one.delete(1.0, END)
        x = prime_output(x, 10)
        output_one.insert(END, x)

    root = Tk()
    root.title("Prime Generator")

    frame1 = Frame(root)
    frame1.grid(row=1, sticky=W)
    frame2 = Frame(root)
    frame2.grid(row=2)

    Label(frame1, text="Enter number of primes: ", width=34).grid(row=1, column=1)
    runner = Button(frame1, text="Run", width=34, command=lambda: run())
    runner.grid(row=1, column=2)
    Button(frame1, text="Restart", command=lambda: output_one.delete(1.0, END), width=34).grid(row=2, column=2)

    input_one = Entry(frame1, width=34)
    input_one.grid(row=2, column=1)

    output_one = Text(frame2, width=60, background="light gray")
    output_one.grid(row=2, column=1)
    Button(root, width=68, text="QUIT", command=root.destroy, fg="red").grid(row=3)
    root.mainloop()


if __name__ == '__main__':
    main()
