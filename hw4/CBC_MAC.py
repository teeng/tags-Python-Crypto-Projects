# implementing CBC-MAC algorithm
# and find the CBC-MAC of a message

import numpy as np

def num_to_arr(n):
  n = str(n)
  return np.array([int(digit) for digit in n])

t = 16
IV = num_to_arr(1010000011111010)

def cbc_mac(m, IV, t=16):
  m = num_to_arr(m)
  m_blocks = m.reshape(-1, t)
  K_hill = np.array([[0,1,0,0], [1,0,0,0], [0,0,0,1], [0,0,1,0]])
  K_vig = num_to_arr(1001001111001001)
  # init
  C_res = []
  for i, block in enumerate(m_blocks):
    # print(block, "b")
    if (i == 0):
      # print(IV, "iv")
      # print(np.bitwise_xor(block, IV), "bit")
      block_hill = np.bitwise_xor(block, IV).reshape(-1, K_hill.shape[0])
      C_res.append(np.dot(block_hill, K_hill).flatten())
    elif (i % 2 == 0):
      # print(C_res[i-1], "C_-1")
      # print(np.bitwise_xor(block, C_res[i-1]), "bit")
      block_hill = np.bitwise_xor(block, C_res[i-1]).reshape(-1, K_hill.shape[0])
      C_res.append(np.dot(block_hill, K_hill).flatten())
    elif (i % 2 == 1):
      # print(C_res[i-1], "C_-1")
      # print(np.bitwise_xor(block, C_res[i-1]), "bit")
      C_res.append(np.bitwise_xor(np.bitwise_xor(block, C_res[i-1]), K_vig)) # binary adding at each index is the same as XOR
    # print(i, C_res[i])
  return int(''.join(map(str, C_res[-1])))

m = 100110010011100011000101000111101100111110101010010110110101100001101110010101111000000010001001

print(f'CBC-MAC: {cbc_mac(m, IV)}')