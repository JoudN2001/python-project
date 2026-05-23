print("This App is claclate your electricity bill \nPlease fill the fllowing filed:")

name = input("Enter your name: ")
id = input("Enter your subscription id: ")
kWh = float(input("Enter consumed electricity (kW/h): "))

print(f"\nHello {name}, Your subscription id is {id}\n==========================================")

price_bracket = "One"
price_before_tax = 0

if kWh > 250:
    price_before_tax = (50 * 0.5) + (0.75 * 100) + (1.2 * 100) + ((kWh - 250) * 1.5)
    price_bracket = "above 250kW/h"
elif kWh > 150:
    price_before_tax = (50 * 0.5) + (0.75 * 100) + ((kWh - 150) * 1.2)
    price_bracket = "151kW/h - 250kW/h"
elif kWh > 50:
    price_before_tax = (50 * 0.5) + ((kWh - 50) * 0.75)
    price_bracket = "51kW/h - 151kW/h"
else:
    price_before_tax = 0.5 * kWh
    price_bracket = "less than 50kW/h"

tax = 0.2
price_tax = price_before_tax * tax
price_after_tax = price_before_tax + price_tax
print("\n--- Bill Summary ---")
print(f"Customer Number: {id}")
print(f"Customer Name: {name}")
print(f"Units Consumed: {kWh}")
print(f"Total Bill Amount (after surcharge): {price_after_tax} JD")

with open("electricity_bills.txt", "a") as file:
    file.write(f"ID: {id}, Name: {name}, Total Bill: {price_after_tax} JD\n")