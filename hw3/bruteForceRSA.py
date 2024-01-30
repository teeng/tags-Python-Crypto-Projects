# demonstrates protocol failure
# ciphertext can be decrypted without determining key
# by bruteforce when using a cryptosystem with
# relatively small modulo 
n, b = 18721, 25
y = [365, 0, 4845, 14930, 2608, 2608, 0]

def easyRSA(y):
  dec = ""
  for i in range(len(y)):
    j = 0
    while ((j**b % n != y[i]) and (j < 26)):
      j += 1
    dec += chr(j + ord("a"))
  return dec

print(easyRSA(y))