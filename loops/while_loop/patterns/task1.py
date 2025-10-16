
# n =  int(input("Enter the number: "))
# for i in range(0, n):
#         for j in  range(0, n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print(j, end=" ")
#         print()
# for i in range(n-2, 0, -1):
#         for j in  range(0,n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print(chr(i+64), end=" ")
#         print()

#sand glass pattern
# n =  int(input("Enter the number: "))
# for i in range(n-1, 1, -1):
#         for j in  range(0,n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print("*", end=" ")
#         print()
# for i in range(1, n):
#         for j in  range(0, n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print("*", end=" ")
#         print()

# X pattern
# n = int(input("Enter a odd number: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i==j) or (i+j == n+1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("Enter a odd number: "))
# for i in range(1, 2*n):
#     if i<=n:
#         num = n-i+1
#     else:
#         num = i-n+1
#     for j in range(1, 2*n):
#         if i==j or j == 2*n-i:
#             print(i, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter a number: "))
# for i in range(1, 2*n):
#     if i <= n:
#         num = i
#     else:
#         num=2*n-i
        
#     for j in range(1,2*n):
#         if i==j or j == 2*n-i:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1 or i ==  0 or i == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n =  int(input("Enter the number: "))
# for i in range(n-1, 0, -1):
#         for j in  range(0,n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print(i, end=" ")
#         print()
# for i in range(2, n):
#         for j in  range(0, n-i):
#             print(" ", end=" ")
#         for j in range(0, 2*i-1):
#             print(i, end=" ")
#         print()

n = int(input("Enter a number: "))
for i in range(1,2*n):
    if i <= n:
        num = i
    else:
        num = 2*n - i
    for j in range(1,2*n):
        
        if i+j == n+1 or j-i== n-1 or i-j == n-1 or i+j == 3*n-1 :
            print(num, end=" ")
        else:
            print(" ", end=" ")
    print()



