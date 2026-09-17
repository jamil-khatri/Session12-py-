from functools import reduce

prices = [120, 80, 150, 60]
total = reduce(lambda price1, price2: price1 + price2, prices)

print("Total bill:", total)
