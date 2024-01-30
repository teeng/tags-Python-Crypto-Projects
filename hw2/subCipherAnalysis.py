from genFunctions import *

# Substitution Cipher Analysis
def substitution(text, key):
  y = textToNum(text)
  x = ""
  toZero = ord("a")
  for i in range(0, len(y)):
    if (y[i] == 27):
      x = x + " "
    else:
      index = y[i]
      x = x + chr((key[index] % 26) + toZero)
  return x

def swap(key, replace, new):
  old1, old2 = key.index(replace), key.index(new)
  key[old1] = new
  key[old2] = replace
  return key

y = "BCDCEFG BCHFIJEB KECBBCU LCGGCH JH MNCINCE INC OCUB CFBL PJHCL KJGQRQCB MCEC OTCGQHV FBBCI ATAAGCB INFI RJTGU INECFICH INC BLBICP"
print(f'cipher: {y}')
conv = textToNum(y)
count, freq = counter(conv, 26)
# print(f'Count for each ciphertext (base 26):\n{count}\nFrequency:\n{freq}')

key_cipher = textToNum("A F L T O Q U J")
key_plain = textToNum("b a y u f i d o")
key = [27]*26

for i in range(0, len(key_cipher)):
  if (key_cipher[i] != 27):
    index = key_cipher[i]
    key[index] = key_plain[i]
    freq[index] = -1
    base_freq[key_plain[i]] = -1

# iterate through the frequency list and find similarities between the English language frequency of letters
for i in range(0, 26):
  check = freq.index(max(freq)) # grab the next maximum frequency from ciphertext
  compare = base_freq.index(max(base_freq)) # grab the next maximum frequency from english text

  if (key[check] == 27):
    key[check] = compare # set ciphertext to plaintext
    freq[check] = -1 # remove from possible
    base_freq[compare] = -1


print(f'key: {key}')
print(substitution(y, key)) # initial guess

print(">>>'fedt' may be 'feds' for federal reserve, swap values so t is now s")
newKey = swap(key, 18, 19)
print(substitution(y, newKey))

print(">>>'assen' may be 'asset'")
newKey = swap(newKey, 13, 19)
print(substitution(y, newKey))

print(">>>'tle' may be 'the' and 'systew' may be 'system'")
newKey = swap(newKey, 11, 7)
newKey = swap(newKey, 22, 12)
print(substitution(y, newKey))

print(">>>'morey' may be 'money' and 'whethel' or 'wele' may be 'whether' or 'were'")
newKey = swap(newKey, 17, 13)
newKey = swap(newKey, 17, 11)
print(substitution(y, newKey))

print(">>>'seperal' may be 'several'")
newKey = swap(newKey, 21, 15)
print(substitution(y, newKey))

print(">>>'fuelinp' may be 'fueling'")
newKey = swap(newKey, 15, 6)
print(substitution(y, newKey))

print(">>>'pould' may be 'could'")
newKey = swap(newKey, 15, 2)
print(substitution(y, newKey))

print(">>>(Confirmed Yellen, Janet is an economist that served as the chair of the Federal Reserve from 2014 to 2018)")
