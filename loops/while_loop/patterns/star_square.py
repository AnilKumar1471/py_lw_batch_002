# n = int(input("Enter the number: "))
# for i in range(0, n):
#     for j in range(0,n):
#         print("*", end="")
#     print()


# n =  int(input("Enter the number: "))
# for i in range(0, n+1):
#         for j in range(0, n-i):
#             print("* ", end="")
#         print()
# for i in range(0, n+1):
#     for j in range(0, i):
#         print("* ", end="")
#     print()
    
# for i in range(n, 1, -1):
#     for j in range(1, i+1):
#         print("* ", end="")
#     print()

n = int(input("Enter the number: "))
for i in range(0, n):
    for j in range(1, n-i):
        print(" ",end="")
    for j in range(0, i):
        print("*", end=" ")
    print()


# n = int(input("Enter the number: "))
# for i in range(0, n):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(1, n-i):
#         print("*",end="")
#     print()

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" "*i, "*"*(n-i))

n = int(input("Enter the number: "))
for i in range(0, n):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(0, n-1):
    for j in range(1, n-i-1):
        print("*",end="")
    print()

# 

# n  = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(j + 64), end="")
#     print()


# n  = int(input("Enter the number: "))
# k = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(k+64), end="")
#         k += 1
#     print()
