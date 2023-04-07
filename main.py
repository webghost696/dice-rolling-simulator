# mini project in python to simulate dice rolling
import random
while True:
    numbers= [i for i in range(1,7)]
    probability=[0.1,0.2,0.1,0.3,0.2,0.4]
    f=random.choices(numbers,probability)
    print(f"Your number is {f}")
    a=int(input("Do you want to roll it again?\n1.Yes\n2.No\n"))
    if a==2:
        break