msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0
while True:
    print(msg_0)
    calc = input()
    try:
        x, operation, y = calc.split()
        if x == "M":
            x = memory
        else:
            if y == "M":
                y = memory
            else:
                y = float(y)
            x = float(x)
    except ValueError:
        print(msg_1)
        continue


    if operation not in ("+", "-", "*", "/"):
        print(msg_2)
        continue

    if operation == "+":
        result = x + y

    elif operation == "-":
        result = x - y

    elif operation == "*":
        result = x * y

    elif operation == "/":
        if y == 0:
            print(msg_3)
            continue
        else:
            result = x / y
    else:
        raise Exception("Unknown Error")
    print(result)
    response = None
    while response not in ("y", "n"):
        print(msg_4)
        response = input()
        if response == "y":
            memory = result

    response = None
    while response not in ("y", "n"):
        print(msg_5)
        response = input()

    if response == "y":
        continue
    else:
        break



