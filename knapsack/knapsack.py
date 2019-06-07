#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  selected = []
  total_cost = 0
  total_value = 0

  if len(items) > 0 and capacity > 0:
    ratios = []

    for i in items:
      item_ratio = round(i.value/i.size, 3)
      ratios.append([item_ratio, i.index])
    ratios = sorted(ratios, reverse=True)
    # print('Ratios: ', ratios)

    sorted_items = []

    for r in range(0, len(items)):
      index = ratios[r][1]-1
      sorted_items.append(items[index])
    # print('Sorted Items: ', sorted_items)

    for item in sorted_items:
      if total_cost + item.size <= capacity:
        selected.append(item.index)
        total_cost += item.size
        total_value += item.value

  print(f'Items to Select: {selected}')
  print(f'Total Cost: {total_cost}')
  print(f'Total Value: {total_value}')

  selected = sorted(selected)
  
  return {'Value': total_value, 'Chosen': selected}

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')