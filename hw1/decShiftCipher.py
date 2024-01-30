# function for decrypting shift cipher
def shiftCipherDec(Y, K):
  toZero = ord("a")
  x = ""
  for i in range(len(Y)):
    if (Y[i] == " "):
      x = x + Y[i]
    else:
      x = x + chr(((ord(Y[i].lower()) - toZero - K) % 26) + toZero)
  return x

ciphertext = shiftCipherDec("VSZZC", 14)
print("plaintext:", ciphertext)

# test function with input file "sampleFICT.txt"
# with shift key = 15
f1 = open("sampleFICT.txt", "r")
f2 = open("shift_output.txt", "w")

K = 15

for line in f1:
  f2.write(shiftCipherDec(line, K))

f1.close()
f2.close()
print(f"File saved as {f2.name}")

# print the 30th to 39th ciphertext characters and
# corresponding plaintext
f1 = open("sampleFICT.txt", "r")
f2 = open("shift_output.txt", "r")

cipher, plain = "", ""

for i in range(30):
  f1.read(1)
  f2.read(1)

for i in range(10):
  cipher = cipher + f1.read(1)
  plain = plain + f2.read(1)

f1.close()
f2.close()

print("cipher-->", cipher, "\nplaintext-->", plain, sep='')
