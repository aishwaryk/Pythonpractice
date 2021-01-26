str = input('enter string to reverse: ')


def reverse_string(str):
    revstr = str.split(" ")
    revlist = []
    counter = len(revstr) - 1
    while counter >= 0:
        revlist.append(revstr[counter])
        counter = counter - 1
    x = " ".join(revlist)
    print(x)


reverse_string(str)
