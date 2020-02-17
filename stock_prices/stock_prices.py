#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = float('-inf')
  cheapest_price = prices[0]

  for i in range(1, len(prices)):
      
    profit = prices[i] - cheapest_price

    if profit > max_profit:
      max_profit = profit
    
    if prices[i] < cheapest_price:
      cheapest_price = prices[i]

  print(max_profit)   
  return max_profit



if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))