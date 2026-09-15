try:
    v1 = int(input(""))
    v = input("")
    v2 = int(input(""))
    if v == "+":
        print(int(v1) + int(v2))
    elif v == "/":
        print(int(v1) / int(v2))
    elif v == "-" or v == "_":
        print(int(v1) - int(v2))
    elif v == "%":
        print(int(v1) % int(v2))
    elif v == "*":
        print(int(v1) * int(v2))
    elif v == "<":
        print(int(v1) < int(v2))
    elif v == ">":
        print(int(v1) > int(v2))
    elif v == "=":
        print(int(v1) == int(v2))
except:
    print("error")
#python code %<+_-*>