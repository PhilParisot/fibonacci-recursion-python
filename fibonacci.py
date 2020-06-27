def display_fib(n: int):
    n = int(n)

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return display_fib(n - 1) + display_fib(n - 2)


Num = input("Input fibonacci number: ")

print("Your fibonnaci number is ", display_fib(Num))
