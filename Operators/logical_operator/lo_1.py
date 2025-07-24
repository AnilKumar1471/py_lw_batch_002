'''
#Logical AND operator
print(10 and 25)#10 is true and 25 is true  if true and true the entire expression value is True 
print(25 and 10)# 25 is True and 10 is True if TRue and True the entire expression value is True
print(25 and 10> 5)# 25 is value is True and 10>5 value is True if True and True the entire expression 
print(10>5 and 25)
print(5>10 and 25)
print(0 and 25)
print( 25 and 66>234 and 0)
print(25 and 0 and 66 > 234)


#Logical OR operator
print(10 or 25) #10 value is True and 25 value is True if True or True to return first True value
print(25 or 10) # 25 value is True and 10 value is True if True or True to return first True value
print(25 or 10> 5)# 25 value is True and 10> 5 value is True if True or True to return first True value
print(10>5 or 25)
print(5>10 or 25)
print(0 or 25)
print( 25 or 66>234 or 0)
print(25 or 0 or 66 > 234)

#Logical NOT operator
r = 10 and 20
print(r)
print(not r)
print(r)

is_raining = True
print(is_raining)
print(not is_raining)

n1 = 25
print(not 25)# 25 value is True if not True value is false
print(not not 25)# 25 value is True if not True value is false then not false value is True
print(not not not 25)# 25 value is True if not True value is false then not false value is True then not true value is False '''
'''
#Unary minus(-)
n1 = -10
n2 = -n1
print(n1 , n2) 

#Membership Operator(in , not in )
print('Z' in "Welcome")
print('W' in "Welcome")
print('w' in "Welcome")
print('Z' not in "Welcome")
print('W' not in "Welcome")
print('w' not in "Welcome")'''
'''
#Identity Operator(is, is not)
num1 = 10
num2 = 20
num3 = 10
num4 = '10'

print(type(num1))#type of num1 is denots class and type =>class int
print(id(num1))#id(num1) is denotes the its allocated num1 address
print(id(num3))
print(id(num2))
print(num1 is num3)
print(num1 is not num3)
print(num1 is num2)
print(id(num4))
print(num1 is num4)'''
'''
#Bitwise Operator
num1 = 18
num2 = 24
print(18 & 24)#16
print(18 | 24)#26
print(18^24)#10

#work
# num1 =42
# num2 = 64

print(~(-1007))
print(~(1007))
#Left shifting
#value * 2^number of shift
print(5 << 2)# 5 * 2^2 =>20
print(5 << 1)# 5 * 2^1 =>10
print(46 << 5)# 46 * 2^5 =>1472


#Right shifting
print(18>>2)# 18 / 2^2 =>18/4=>4.something => 4
print(89>>3)# 89 / 2^3 =>89/8=>11.something => 11'''
'''
#Type Conversion(implicit and explicit)
num1 =  1
num2 = 2.5
print(num1 + num2 )# 10.0 + 2.5 => 12.5
print(int(num1 + num2 ))#10.0 + 2.5=>int(12.5)=>12'''

#Precedence And Associate

num1 = 42
num2 = 24
print(42 & 24)
print(42 | 24)
print(42^24)








