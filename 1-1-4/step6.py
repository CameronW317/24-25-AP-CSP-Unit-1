num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

while num1 % num2 != 0:
    print("Number 1 is not divisible by number 2")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

print("They are divisible")