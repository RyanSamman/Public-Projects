# ~~~~~~~~~~~~~~~~~~~~~ Pattern 1 ~~~~~~~~~~~~~~~~~~~~~~
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


def pattern1(x, y):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            outstring += format(j, (str(y) + "d")) + " "
        outstring += "\n"
    return outstring

# ~~~~~~~~~~~~~~~~~~~~~~~ Pattern 2 ~~~~~~~~~~~~~~~~~~~~~~
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


def pattern2(x, y):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, x + 2 - i):
            outstring += format(j, (str(y) + "d")) + " "
        outstring += "\n"
    return outstring


# ~~~~~~~~~~~~~~~~~~~~~~~ Pattern 3 ~~~~~~~~~~~~~~~~~~~~~~
#           1
#         2 1
#       3 2 1
#     4 3 2 1
#   5 4 3 2 1
# 6 5 4 3 2 1


def pattern3(x, y):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, x + 1 - i):
            if y == 1:
                outstring += "  "
            elif y == 2:
                outstring += "   "
        for k in range(i, 0, -1):
            outstring += format(k, (str(y) + "d")) + " "
        outstring += "\n"
    return outstring

# ~~~~~~~~~~~~~~~~~~~~~~~ Pattern 4 ~~~~~~~~~~~~~~~~~~~~~~
# 1 2 3 4 5 6
#   1 2 3 4 5
#     1 2 3 4
#       1 2 3
#         1 2
#           1


def pattern4(x, y):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, i):
            if y == 1:
                outstring += "  "
            elif y == 2:
                outstring += "   "
        for k in range(1, x + 2 - i):
            outstring += format(k, (str(y) + "d")) + " "
        outstring += "\n"
    return outstring
