a = float(input())
o = str(input())
b = float(input())
if (o == "+"):
    print(a+b)
if (o == "-"):
    print(a-b)
if (o == "*"):
    print(a*b)
if (o == "/"):
    if(b == 0):
        print("Nie można dzielić przez zero")
    else:
        print(a/b)