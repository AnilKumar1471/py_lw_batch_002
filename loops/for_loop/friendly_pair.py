num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

sum1  = 0
for i in range(1, num1 + 1):
    if num1 % i == 0:
        sum1 = sum1 + i
        
sum2 = 0
for j in range(1, num2 + 1):
    if num2 % j == 0:
        sum2 = sum2 + j
        
ratio1 = sum1 / num1
ratio2 = sum2 / num2

if ratio1 == ratio2:
    print(num1, "and", num2, "are friendly pair")
else:
    print(num1, "and", num2, "are not friendly pair")