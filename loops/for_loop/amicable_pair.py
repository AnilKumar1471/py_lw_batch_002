num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

sum1  = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i
        
sum2 = 0
for j in range(1, num2):
    if num2 % j == 0:
        sum2 += j
        
if sum1 == num2 and sum2 == num1:
        print(num1, "and", num2, "are amicable pair")
else:
        print(num1, "and", num2, "are not amicable pair")