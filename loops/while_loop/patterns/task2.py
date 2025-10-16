n = int(input("Enter a number: "))
for i in range(1, 2*n):
    if i<=n:
        num = i
    else:
        num = 2*n - i
    for j in range(1, 2*n):
        if i == j or i+j == 2*n:
            print(num,end=" ")
        else:
            print(" ", end=" ")
    print()

