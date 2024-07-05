# A basic calculator for add,sub,mul,div purpose.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


'''Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice(1/2/3/4): 1
Enter first number: 40
Enter second number: 20
The result is: 60.0
Do you want to perform another calculation? (yes/no): yes
Enter choice(1/2/3/4): 2
Enter first number: 45
Enter second number: 20
The result is: 25.0
Do you want to perform another calculation? (yes/no): yes
Enter choice(1/2/3/4): 3
Enter first number: 4
Enter second number: 3
The result is: 12.0
Do you want to perform another calculation? (yes/no): yes
Enter choice(1/2/3/4): 4
Enter first number: 40
Enter second number: 10
The result is: 4.0
Do you want to perform another calculation? (yes/no): no'''