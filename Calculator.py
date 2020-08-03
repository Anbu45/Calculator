def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def rounddivide(a,b):
    return a//b
def modulus(a,b):
    return a%b
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Rounddivide")
print("6.Modulus")
while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4','5','6'):
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "//", num2, "=", rounddivide(num1, num2))
        elif choice == '6':
            print(num1, "%", num2, "=", modulus(num1, num2))
        break
    else:
        print("Invalid")
