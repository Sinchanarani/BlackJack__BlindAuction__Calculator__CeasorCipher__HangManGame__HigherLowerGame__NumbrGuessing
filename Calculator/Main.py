import Art
print(Art.logo)
def add(n1,n2):
    sum= n1+n2
    return sum
def subtract(n1,n2):
    difference= n1-n2
    return difference
def multiply(n1,n2):
    product=n1*n2
    return product
def division(n1,n2):
    if n2==0:
        print("Division by zero")
    else:
        quotient=n1/n2
        return quotient

n1=float(input("What is the first number? "))
print('''
+
-
*
/''')
operator=input("Pick an operation: ")
n2=float(input("What is the next number? "))
if operator=='+':
    res=add(n1,n2)
elif operator=='-':
    res=subtract(n1,n2)
elif operator=='*':
    res=multiply(n1,n2)
elif operator=='/':
    res=division(n1,n2)
print(f"{float(n1)} {operator} {float(n2)}= {res}")
while True:
    nextOP=input("Type 'y' to continue with previous result or type 'n' to start a new calculation:")
    if nextOP=='y':
        n1=res
        print('''
        +
        -
        *
        /''')
        operator = input("Pick an operation: ")
        n2 = float(input("What is the next number? "))
        if operator == '+':
            res = add(n1, n2)
        elif operator == '-':
            res = subtract(n1, n2)
        elif operator == '*':
            res = multiply(n1, n2)
        elif operator == '/':
            res = division(n1, n2)
        print(f"{float(n1)} {operator} {float(n2)}= {res}")

    elif nextOP=='n':
        break