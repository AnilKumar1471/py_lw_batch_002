num = int(input())           #84                       #56                      #78                       # 65
num1 = num //10              #num1 = 84 // 10 =>8      #num1 = 56 // 10 =>5     #num1 = 78 // 10 =>7      #num1 = 65 // 10=>6
num2 = num % 10              #num2 = 84 % 10 => 4      #num2 = 56 % 10 =>6      #num2 = 78 % 10 =>8       #num2 = 65 % 10=>5
reverse =  num2*10 + num1    #reverse = 4*10 + 8       #reverse = 6*10 + 5      #reverse = 8*10 + 7       #reverse = 5*10 + 6
print(num +reverse)          #84 + 48 =>132            #56 + 65 =>121           #78 + 87 =>165            #65 + 56 =>121
