rowsize = int(input("Enter the number of rows: "))
if rowsize%2 == 0:
    halfdiamon = rowsize/2
else:
    halfdiamon = (rowsize/2)+1

space = halfdiamon - 1
halfdiamon = int(halfdiamon)
space = int(space)
for i in range(1, halfdiamon+1):
    for j in range(1, space+1):
        print(" ", end="")
    space -= 1
    num = 1
    for j in range(1, 2*i):
        print(num, end="")
        num = num + 1
    print()
space = 1
for i in range(1, halfdiamon):
    for j in range(1, space+1):
        print(" ", end="")
    space += 1
    num = 1
    for j in range(1, 2*(halfdiamon-i)):
        print(num, end="")
        num = num + 1
    print()
