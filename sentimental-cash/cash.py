import math

while True:
    cash = input("Cash owed: ")
    try:
        cash = float(cash)
        break
    except ValueError:
        continue

cents = round(cash * 100)
coins = 0

quaters = math.floor(cents / 25)
cents -= quaters * 25
coins += quaters

dimes = math.floor(cents / 10)
cents -= dimes * 10
coins += dimes

nickels = math.floor(cents / 5)
cents -= nickels * 5
coins += nickels

coins += cents

print(str(coins))
