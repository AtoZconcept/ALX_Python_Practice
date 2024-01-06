money = input("Enter amount to invest: ")
interest = input("Enter intrest rate: ")
money = float(money)
interest = float(interest) * .01
for i in range(10):
    money += money * interest
print("{:.2f}".format(money))