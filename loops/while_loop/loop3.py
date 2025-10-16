n  = int(input("enter a number : "))
n1 =n2 = n
count =  0
while n > 0:
    n = n// 10
    count += 1
ans = 0
while n1 > 0:
    digit = n1 % 10
    ans = ans + (digit ** count)
    n1 = n1 // 10
    count -= 1
if n2 == ans:
    print("given number is diasarium number")
else:
    print("given number is not a diasarium number")