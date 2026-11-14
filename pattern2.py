rows = int(input("Enter the number of rows: "))
number = 1
print("Floyd's triangle:")
for i in range(rows):
    for j in range(i):  
        print(number, end=" ")
        number += 1
    print()