number = int(input("Enter the number of rows: "))

for i in range(number):
    for j in range(i+1):
        print("*", end="")
    print("")