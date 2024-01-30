# factorizing a large number quickly
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

n = 2288233
a1, a2, a3, a4 = 880525, 2057202, 648581, 668676

x = a1 * a2
y = a3
get_factors(n, x, y)