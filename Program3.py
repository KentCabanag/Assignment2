ammount = float(input("Enter the ammount of money you have: "))
aplprice = float(input("Enter the price of an apple: "))
napple = int(ammount/aplprice)
change = ammount % aplprice
print(f"You can buy {napple} apples and your change is {change:.2f} pesos.")