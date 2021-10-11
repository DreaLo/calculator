a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

operation = input("Choose math operation (+ or - or * or /): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Sorry, you didn't provide a correct math operation. Try again.")
