def is_lucky(n):
    """Method to check if a number is a lucky number"""
    remainder = 0
    summation = 0
    n1 = n
    while n > 0:
        remainder = n % 10
        summation = summation + remainder
        n = n // 10
    if summation == 7:
        print(" It is a lucky number")
    else:
        print("It's not a lucky number")
   # return summation


is_lucky(143)

