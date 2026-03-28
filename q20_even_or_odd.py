def evenodd_func():
    return num % 2 == 0
num = int(input("Enter a number: "))
if evenodd_func():
    print("The number is even")
else:
    print("The number is odd")