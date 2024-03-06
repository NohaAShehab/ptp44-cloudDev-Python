

def ask_for_int(message='please enter an integer'):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num
        print("----Error-- Try again --- ")