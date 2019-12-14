def Max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = Max(lst[1:])
        return m if m > lst[0] else lst[0]


def main():
    lst = eval(input(" please enter a list of numbers: "))
    print("the largest number is: ", Max(lst))


main()
