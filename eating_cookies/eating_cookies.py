#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  #initialize cache with first 3 solutions (0, 1, and 2 cookies)
  cache[0] = 1
  cache[1] = 1
  cache[2] = 2
  
  #cache has been nitialized to 0 so if different 0 then a previous result has been saved
  if cache[n] != 0:
    return cache[n]
  else:
    result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    cache[n] = result
    return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')