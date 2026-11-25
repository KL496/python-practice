number = int(input())

for i in range(number, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" " if j > 1 else "")
    print()