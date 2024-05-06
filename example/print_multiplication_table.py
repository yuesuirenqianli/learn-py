for i in range(1, 10):
    print("            " * (9 - i), end="")
    for j in range(1, i + 1):
        print(f'{j} * {10 - i + j - 1} = {j * (10 - i + j - 1)}'.ljust(10), end='  ')
    print()
