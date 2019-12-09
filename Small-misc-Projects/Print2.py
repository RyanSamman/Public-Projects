import sys  # Required to output strings into console (sys.stdout)


def print2(*args, sep=' ', end='\n', file=sys.stdout):
    # Docstring
    '''
    :param args:
        Produces a tuple which lies all the strings to be outputted

    ~~~ Technically inputting a tuple and dictionary ~~~~
    print2(*(5, 6, 7, 8) ,**{sep: ' ', end: '\n', file: sys.stdout}) is the same as
    print2(5, 6, 7, 8, sep=' ', end='\n', file=sys.stdout)

    :param sep:
        the string between each string in the tuple
        (Default is ' ')

    :param end:
        the string added at the end of one output string
        (Default is '\n')
    :param file:
        the target file to output the string into, can be any file but must be opened beforehand
        (Ex:
        newfile = open("newfile.txt", "w")
        file=newfile
    '''
    string1 = ""
    for i in args:
        if i == args[-1]:
            string1 += str(i)
        else:
            string1 = string1 + str(i) + sep
    string1 += end
    file.write(string1)


print2(5, 6, 7, sep="  ", end="+")
print2(5, 6, 7, sep="  ", end="+")
print()  # Makes new line as last one ended with + not /n
print(5, 6, 7, sep="  ", end="+")
print(5, 6, 7, sep="  ", end="+")
print()  # Makes new line as last one ended with + not /n
print2("50"*6)
print("50"*6)
help(print2)  # Displays Docstrings

# Page 547 and 548 for emulation on 2.7
# Page 550 for tips on kwargs