def check_even_odd(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
num = int(input("Enter number: "))
check_even_odd(num)