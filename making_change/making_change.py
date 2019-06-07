#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Denominations = [1, 5, 10, 25, 50]
  cache = {
      0: 1,
    # 1: 0,
    # 2: 0,
    # 3: 0,
    # 4: 0,
    # 5: 0
  }

  def compute(amount, coin):
    if coin > amount:
      return
    for value in range(coin, amount + 1):
      if value not in cache:
        cache[value] = 1
      if coin == 1:
        next
      if coin > 1:
          remainder = value -coin
          cache[value] += cache[remainder]
        # cache[value] += int(value/coin - 1)
        # cache[value] += int(value/coin)
      # print(f'Cache: value - {value}, combos - {cache[value]}')
    print('Cache: ', cache)

  # remainder = 0

  if amount < 5:
    if amount < 0:
      return 0
    return 1

  else:
    # Calculate ways to make change
    for coin in denominations:
      compute(amount, coin)

  return cache[amount]

making_change(20, [1, 5, 10, 25, 50])



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")