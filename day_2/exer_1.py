                        #Test Case1
days =  int(input())   #days = 500
year = days//365       #year = 500//365 =>1
day = (days%365)       #day = 500 % 365=>135
month = (day//30)      #month = 135 // 30 => 4
days = day % 30        #days = 135 % 30 =>15
print(year,month,days)
