# num = 12345
# x = 1
# while num > 0:
#     digit = num % 10
#     ans = ans + digit * x
#     n = n //10
#     x = x * 10
# print(ans)

n = int(input("enter a number : "))
even =  odd = 0
n1 = n2 = n
x = 1
while n1 > 0:
    digit = n1 % 10
    if digit % 2 == 0:
        even = even + digit * x
        x = x * 10
    n1 = n1 // 10
y = 1
while n2 > 0:
    digit = n2 % 10
    if digit % 2 != 0:
        odd = odd +digit * y
        y = y * 10
    n2 = n2 // 10
        
        
print("even value is",even)
print("odd value number: ", odd)
print("Difference of even and odd numbers",abs(even - odd))