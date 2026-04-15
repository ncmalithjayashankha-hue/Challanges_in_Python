import matplotlib.pyplot as plt
import math

S_a = -10
S_b = 2
D_a = 300
D_b = 5

price = []
quantity_of_demand = []
quantity_of_supply = []
while True:
    cPrice = int(input("Enter the price: "))
    if cPrice == 0:
        break
    else:
        price.append(cPrice)


sorted_price = sorted(price)
for i in sorted_price:
    qd = D_a - D_b * i
    qs = S_a + S_b * i
    quantity_of_demand.append(qd)
    quantity_of_supply.append(qs)

equilibrium = [0.0,0.0]
p = (D_a + math.sqrt(S_a * S_a))/(S_b + D_b)
equilibrium[0] = p
q = D_a - D_b * p
equilibrium[1] = q

print(f"Market Equilibrium Price is: {equilibrium[0]} and Equilibrium Quantity is: {equilibrium[1]}")


plt.plot(quantity_of_demand, sorted_price,label="demand")
plt.plot(quantity_of_supply, sorted_price,label="Supply")
plt.plot(equilibrium[1], equilibrium[0], "o",label="Equilibrium")
plt.legend()
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.title("Market equilibrium")
plt.grid(True)
plt.show()