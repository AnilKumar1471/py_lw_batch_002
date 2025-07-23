sell_price = int(input("Enter selling price of 15 items: "))
profit = int(input("Enter profit in rupees: "))
actual_cost = sell_price - profit
actual_cost_one_item =  actual_cost / 15

print("one item price is: ",actual_cost_one_item)