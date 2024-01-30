# Stream cipher - finding the coefficient of recurrences
# first stream to test:
a = [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1,
1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0,
1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1,
0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
1, 0, 0, 0, 0]

import itertools # used to quickly find all combinations to go through
import numpy as np # required for faster array calculations

def bruteForce(y):
  def makeStream(coeff, init):
    new = init # initialize stream with initial
    for i in range(1, len(y) - len(init) + 1):
      chunk = new[i-1:i-1+len(coeff)]
      new = np.append(new, np.sum(coeff * chunk) % 2) # prev coefficient-sized block
    return new

  for i in range(2, int(len(y)/2)): # possible coeff lengths (half of keystream)
      initPossible = y[:i] # match possible coeff length
      coeffPossible = list(itertools.product([0, 1], repeat=i))
      for j in range(len(coeffPossible)):
        test = makeStream(np.array(coeffPossible[j]), initPossible)
        if np.array_equiv(test, y):
          return coeffPossible[j]
  return None

print(f'coeff: {bruteForce(a)}')


# second stream to test:
b = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,
0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1,
1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,
1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1,
1, 1, 1, 1, 1]

print(f'coeff: {bruteForce(b)}')
