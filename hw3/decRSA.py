# modulo base, public key
import math
def modulo_inverse_naive(n,m, print_flag = 0):
  if n == 1:
    print('Inverse of 1 in mod '+ str(m) +' is 1')
  else:
    if (float(n)).is_integer() and (float(m)).is_integer() and m > 0:
      if math.gcd(n,m) == 1:
        n_mod_m = n%m
        for x in range(1, m):
          if ((n_mod_m * x)%m)  == 1:#(np.mod((n_mod_m * x),m)  == 1):
            if print_flag == 1:
              print('Inverse of ' + str(n) + ' in mod '+ str(m) +' is ' + str(x))
            return x

      else:
        print('ERROR: gcd(n,m) is not 1. Inverse does not exist for n mod m')
    else:
      print('ERROR: n and m both must be integers. m should be positive')

def prime_fact(n):
  factors = []
  while (n % 2 == 0):
    factors.append(2)
    n = n/2
  # n must be odd, increment by 2
  for i in range(3, int(n**.5) + 1, 2):
    while (n % i == 0):
      factors.append(i)
      n = n / i
  if (n > 2):
    factors.append(int(n))
  return factors

def genRSAKey(n, b):
  fact_n = prime_fact(n)
  print(f'Factors of n: {fact_n}')
  if (len(fact_n) == 1):
    phi = n-1
  else:
    phi = (fact_n[0] - 1)*(fact_n[1] - 1)

  a = modulo_inverse_naive(b, phi)
  if (a < 0):
    a = a + phi
  return a


# factor n and compute RSA private key a
n, b = 31313, 4913
a = genRSAKey(n, b)
print(f'Public Key: ({b}, {n})\nPrivate Key: ({a}, {n})')


# implement square and multiply algorithm
# for computationally efficient exponentiation in modulo n
# assumes a is represented in binary
def square_and_mult(c, a, n):
  e = 1
  for i in range(len(a) - 1, -1, -1):
    e = (e**2) % n
    if (a[i] == 1):
      e = (e * c) % n
  return e

# decode ciphertext
y = [6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809,
    23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395,
    27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881,
    25774, 7647, 23901, 7372, 25774, 18436, 12056, 13547,
    7908, 8635, 2149, 1908, 22076, 7372, 8686, 1304,
    4082, 11803, 5314, 107, 7359, 22470, 7372, 22827,
    15698, 30317, 4685, 14696, 30388, 8671, 29956, 15705,
    1417, 26905, 25809, 28347, 26277, 7897, 20240, 21519,
    12437, 1108, 27106, 18743, 24144, 10685, 25234, 30155,
    23005, 8267, 9917, 7994, 9694, 2149, 10042, 27705,
    15930, 29748, 8635, 23645, 11738, 24591, 20240, 27212,
    27486, 9741, 2149, 29329, 2149, 5501, 14015, 30155,
    18154, 22319, 27705, 20321, 23254, 13624, 3249, 5443,
    2149, 16975, 16087, 14600, 27705, 19386, 7325, 26277,
    19554, 23614, 7553, 4734, 8091, 23973, 14015, 107,
    3183, 17347, 25234, 4595, 21498, 6360, 19837, 8463,
    6000, 31280, 29413, 2066, 369, 23204, 8425, 7792,
    25973, 4477, 30989]

def to_base(inp, base):
    res = []
    while (inp > 0):
        res.append(inp % base)
        inp = int(inp / base)
    return res

def decRSA(y, a, n):
  res = ""
  for i in range(len(y)):
    a_bin = to_base(a, 2)
    c_apply_a = square_and_mult(y[i], a_bin, n)
    c_base_26 = to_base(c_apply_a, 26)
    for i in range(3 - len(c_base_26)): c_base_26.append(0)

    sub = ""
    for j in range(len(c_base_26)):
      sub = chr(c_base_26[j] + ord("a")) + sub
    res += sub
  return res

print(decRSA(y, a, n))