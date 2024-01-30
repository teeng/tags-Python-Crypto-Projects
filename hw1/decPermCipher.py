# function for decrypting permutation cipher with m = 8
def decPerm(y, key):
  m = 8

  # clean whitespace and convert to lower
  y = "".join(y.lower().split(" "))
  x = [0] * len(y)
  for i in range(0, len(y), m):
    for k in range(m):
      x[i+key[k]-1] = y[i+k]
  return ''.join(x)

# test decryption with given ciphertext:
y = "T G E E M N E L N N T D R O E O A A H D O E T C S H A E I R L M"
key = [4, 1, 6, 2, 7, 3, 8, 5]

x = decPerm(y, key)
print("plaintext:", x)