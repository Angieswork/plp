while True: 
 num1 = int(input("Enter first number:"))
 num2 = int(input("Enter second number: "))
 operation = str(input("Enter preferred mathematical operation: "))

 if operation == '+':
    print(f'Your result is: {num1 + num2}')
 elif operation == '-':
    print(f'Your result is: {num1 - num2}')
 elif operation == '*':
    print(f'Your result is: {num1 * num2}')
 else:
    print(f'Your result is: {num1 / num2}')


