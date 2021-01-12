def is_lucky(n):
    """Method to check if a number is a lucky number"""

    n1 = n

    def check_lucky(num):
        add = 0
        rem = 0
        while num > 0:
            rem = num % 10
            add = add + rem
            num = num // 10

        return add

    summation = check_lucky(n)
    while summation > 10:
        summation = check_lucky(summation)

    if summation == 7:
        print(" It is a lucky number")
    else:
        print("It's not a lucky number")


is_lucky(7777777777777777777)
