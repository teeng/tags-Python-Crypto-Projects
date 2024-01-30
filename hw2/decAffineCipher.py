from genFunctions import *

# decrypt affine cipher with key value pair (a, b)
def decAffine(y, a, b):
  x = ""
  toZero = ord("a")
  for i in range(0, len(y)):
    if (y[i] == " "):
      x = x + " "
    else:
      x = x + chr((invMod(a, 26)[0] * (ord(y[i].lower()) - toZero - b) % 26) + toZero)
  return x

# decrypt "enc_ACAD.txt" with function
print("\nMay take a while due to large input file size... Please Wait")
f1 = open("enc_ACAD.txt", "r")
f2 = open("affine_output.txt", "w")

a, b = 9, -17

f1 = open("enc_ACAD.txt", "r")
f2 = open("affine_output.txt", "w")

for line in f1:
    f2.write(decAffine(line, a, b, 26))

print(f"File saved as {f2.name}")
f1.close()
f2.close()

# print the 30th to 39th ciphertext characters
# and corresponding plaintext
f1 = open("enc_ACAD.txt", "r")
f2 = open("affine_output.txt", "r")
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
