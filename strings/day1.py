name  =  "Anil Kumar"

# print(name[1])
# print(name[5])
# for i in name:
#     print(i)
    
# i = 2
# print(name[i*4])

# str =  "python"

# print(str[1:5])
# print(str[1:])
# print(str[:6])
# print(str[:])
# print(str[1:20])
# print(str[-1])
# print(str[-6])
# print(str[-2:])
# print(str[:-2])
# print(str[-5:-2])

# str = "Welcome to The world of python"

# print(str[2:10])
# print(str[2:20:2])
# print(str[2:13:4])
# print(str[::2])
# print(str[::-1])
# print(str[::-3])
# print(str[-5:-20:-1])
# print(str[-4:-10:-3])
# print(str[-4:-25:-3])

# for i in range(0,256):
#     print(chr(i),i,end=" ")

str = "welcome to python world, lets start our python class1"
#len():its returns the length of the string. it counts the number of the characters in the string 
print(len(str))
print(str.capitalize())
name = "banana"
print(name.center(20))
print(str.count("python",5,20))
#endswith():it checks whether the string ends with suffix or not.
#if ends with suffix then it returns True value otherwise
print(str.endswith("class"))
#find()
print(str.find("q"))
#index():
# print(str.index("e"))
#isalnum():
print(str.isalnum())
#isalpha:
print(str.isalpha())
#isdigit():
print(str.isdigit())
#islower():
print(str.islower())
#isupper():it returns True value if the string has at least one character and every
#character is in upper case letter otherwise it will return False value
print(str.isupper())
#isnumeric():
print(str.isnumeric())
#isidentifier(): it returns True value if the string is a valid identifier otherwise it will 
#return False value.
print(str.isidentifier())
#lower():it converts all the characters of a string into lower case letters
print(str.lower())
#upper():it converts all the characters of a string into upper case letters
print(str.upper())
#ljust():
print(str.rjust(20,"*"))
#replace():
print(str.replace("e","2"))
#strip():it removes all leading and trailing whitespace 
print(str.strip())
#isstrip()
print(str.lstrip())
#rstrip():
print(str.rstrip())
#swapcase():it toggles the case of every character(upper case will converted into lower case and lower 
# case will converted into upper case)
print(str.swapcase())
#zfill():it return the string padded with zeros to a toatl width of characters.
#it is used with numbers and also retain the sign.
print(str.zfill(10))
#max():it return the higher alphabetical character from string 
print(max(str))
 



