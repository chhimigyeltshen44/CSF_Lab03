numbers = [1,4,3,2,3,9]
print(numbers)
target = int(input("Enter a number: "))
print(f"searching for: {target}")
for x in numbers:
    if x == target:
        print("Number found")
    else:
        while x != target:
            print("Target not found")
            break
