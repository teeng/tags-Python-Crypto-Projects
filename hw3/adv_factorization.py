# factorization of an extremely large number, further details below
def gcdTwo(r0, r1):
  r2 = r0 % r1

  while(r2 != 0):
    r0 = r1
    r1 = r2
    r2 = r0 % r1
  return r1

def get_factors(n, x, y):
  factors = []
  if (x**2 % n == y**2 % n):
    if ((x % n != y % n) and (x % n != -1 * y % n)):
      factors.append(gcdTwo(x - y, n))
      factors.append(gcdTwo(x + y, n))
  print(f'Factors of {n}: {factors}\nVerify: {factors[0]}*{factors[1]} = {n} is {factors[0]*factors[1] == n}')
  return factors

n = 537069139875071
x, y = 85975324443166, 462436106261
print(gcdTwo(x + y, n), gcdTwo(x-y, n))

get_factors(n, x, y)


# x (or y) is a factor, so find a y (or x) where x^2 = y^2 and x != +- y
# gcd(x-y, n) with +- y is a nontrivial factor of n, meaning gcd(x-y, n) can be 1, meaning
# x-y can be set to p (or q) since it is a prime factor of n, and x+y can be set to q (or p) since it is also,
# matching gcd(x-y, n) = 1
# so x-y = p, x+y = q, find x and y (system of equations)
import numpy as np

p, q = 985739879, 1388749507
n = p * q

coeff = np.array([[1, -1], [1, 1]])
target = np.array([[p], [q]])

res = np.linalg.solve(coeff, target)
x, y = int(res[0][0]), int(res[1][0])

print(f'Verify for x is {x}, y is {y}')
print(f'x**2 % n = y**2 % n: {x**2 % n == y**2 % n}')
print(f'x % n != +- y % n: {(x % n != y % n) and (x % n != -1 * y % n)}')