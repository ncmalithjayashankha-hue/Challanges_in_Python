import matplotlib.pyplot as plt
import math

while True:
    try:
        S_a = int(input("Enter value of 'a' in Supply Equation: "))
        S_b = int(input("Enter value of 'b' in Supply Equation: "))
        D_a = int(input("Enter value of 'a' in Demand Equation: "))
        D_b = int(input("Enter value of 'b' in demand Equation: "))
    except ValueError:
        print("Value of 'a' in Supply Equation must be an integer.")
    if S_a <= -1000 and S_b <= 0 and D_a <= 0 and D_b <= 0:
        continue
    else:
        break

price = [0]
quantity_of_demand = []
quantity_of_supply = []
cPrice = int(input("Enter the price: "))
price.append(cPrice)


sorted_price = sorted(price)
for i in sorted_price:
    qd = D_a - D_b * i
    qs = S_a + S_b * i
    quantity_of_demand.append(qd)
    quantity_of_supply.append(qs)

equilibrium = [0.0,0.0]
p = (D_a - S_a) / (S_b + D_b)
equilibrium[0] = p
q = D_a - D_b * p
equilibrium[1] = q

print(f"Market Equilibrium Price is: {equilibrium[0]} and Equilibrium Quantity is: {equilibrium[1]}")

def calculator(mode):
    if mode == 1:
        # Normal case
        q_eq = equilibrium[1]
        p_eq = equilibrium[0]

        p_max = D_a / D_b
        p_min = -S_a / S_b

        cs = ((p_max - p_eq) * q_eq) / 2
        ps = ((p_eq - p_min) * q_eq) / 2

        print("\n--- NORMAL MARKET ---")
        print(f"Equilibrium Price: {p_eq}")
        print(f"Equilibrium Quantity: {q_eq}")
        print(f"Consumer Surplus: {cs}")
        print(f"Producer Surplus: {ps}")
        print("Deadweight Loss: 0")

    elif mode == 2:
        # Tax case
        tx = float(input("Enter tax per unit: "))

        q_eq = equilibrium[1]

        # New equilibrium
        p_new = (D_a - S_a + S_b * tx) / (S_b + D_b)
        q_new = D_a - D_b * p_new

        p_max = D_a / D_b
        p_min = -S_a / S_b

        p_producer = p_new - tx

        cs = ((p_max - p_new) * q_new) / 2
        ps = ((p_producer - p_min) * q_new) / 2
        gov_rev = tx * q_new
        dwl = 0.5 * (q_eq - q_new) * tx

        print("\n--- TAX CASE ---")
        print(f"New Equilibrium Price (Consumers pay): {p_new}")
        print(f"Price received by Producers: {p_producer}")
        print(f"New Quantity: {q_new}")
        print(f"Consumer Surplus: {cs}")
        print(f"Producer Surplus: {ps}")
        print(f"Government Revenue: {gov_rev}")
        print(f"Deadweight Loss: {dwl}")

    elif mode == 3:
        # Subsidy case
        sub = int(input("Enter subsidy per unit: "))

        q_eq = equilibrium[1]

        p_new = (D_a - S_a - S_b * sub) / (S_b + D_b)
        q_new = D_a - D_b * p_new

        p_max = D_a / D_b
        p_min = -S_a / S_b

        p_producer = p_new + sub

        cs = ((p_max - p_new) * q_new) / 2
        ps = ((p_producer - p_min) * q_new) / 2
        gov_exp = sub * q_new
        dwl = 0.5 * abs(q_new - q_eq) * sub

        print("\n--- SUBSIDY CASE ---")
        print(f"New Equilibrium Price (Consumers pay): {p_new}")
        print(f"Price received by Producers: {p_producer}")
        print(f"New Quantity: {q_new}")
        print(f"Consumer Surplus: {cs}")
        print(f"Producer Surplus: {ps}")
        print(f"Government Expenditure: {gov_exp}")
        print(f"Deadweight Loss: {dwl}")

calculator(1)
def tax(prices):
    tx = float(input("Enter the tax amount: "))

    quantity_of_supply_after_tax = []

    sorted_price_after_tax = sorted(prices)
    for pt in sorted_price_after_tax:
        qst = ((S_a-(S_b*tx)) + S_b * pt)
        quantity_of_supply_after_tax.append(qst)

    shifted_equilibrium = [0.0,0.0]
    ept = (D_a-S_a+S_b*tx)/(S_b + D_b)
    shifted_equilibrium[0] = ept
    eqt = D_a - D_b * ept
    shifted_equilibrium[1] = eqt

    calculator(2)

    plt.plot(quantity_of_demand, sorted_price, label="demand")
    plt.plot(quantity_of_supply, sorted_price, label="Supply")
    plt.plot(quantity_of_supply_after_tax, sorted_price_after_tax, label="Shifted Supply Curve")
    plt.plot(shifted_equilibrium[1], shifted_equilibrium[0], "o", label=" Shifted Equilibrium")
    plt.plot(equilibrium[1], equilibrium[0], "o", label="Equilibrium")
    plt.legend()
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.title("Market equilibrium")
    plt.grid(True)
    plt.show()


def subsidies(prices):
    tx = float(input("Enter the Subsidiary amount: "))

    quantity_of_supply_after_tax = []

    sorted_price_after_tax = sorted(prices)
    for pt in sorted_price_after_tax:
        qst = ((S_a + (S_b * tx)) + S_b * pt)
        quantity_of_supply_after_tax.append(qst)

    shifted_equilibrium = [0.0, 0.0]
    ept = (D_a - S_a - S_b * tx) / (S_b + D_b)
    shifted_equilibrium[0] = ept
    eqt = D_a - D_b * ept
    shifted_equilibrium[1] = eqt

    calculator(3)

    plt.plot(quantity_of_demand, sorted_price, label="demand")
    plt.plot(quantity_of_supply, sorted_price, label="Supply")
    plt.plot(quantity_of_supply_after_tax, sorted_price_after_tax, label="Shifted Supply Curve")
    plt.plot(shifted_equilibrium[1], shifted_equilibrium[0], "o", label=" Shifted Equilibrium")
    plt.plot(equilibrium[1], equilibrium[0], "o", label="Equilibrium")
    plt.legend()
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.title("Market equilibrium")
    plt.grid(True)
    plt.show()

def normal():
    plt.plot(quantity_of_demand, sorted_price,label="demand")
    plt.plot(quantity_of_supply, sorted_price,label="Supply")
    plt.plot(equilibrium[1], equilibrium[0], "o",label="Equilibrium")
    plt.legend()
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.title("Market equilibrium")
    plt.grid(True)
    plt.show()

while True:
    choice = input("do you want to calculate tax or Subsidies (Yes/No): ").lower().strip()
    if choice == "no" or choice == "n":
        normal()
        break
    elif choice == "yes" or choice == "y":
        while True:
            ts = input("Tax or Subsidies? (T/S/Exit): ").lower().strip()
            if ts == "t":
                tax(price)
            elif ts == "s":
                subsidies(price)
            elif ts == "exit" or ts == "e":
                break
            else:
                print("Invalid input")

    else:
        print("invalid input")
