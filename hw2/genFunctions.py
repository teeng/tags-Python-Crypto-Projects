# General Functions
# find gcd of two numbers
def gcdTwo(r0, r1):
  r2 = r0 % r1

  while(r2 != 0):
    r0 = r1
    r1 = r2
    r2 = r0 % r1
  return r1

# find inverse mod of a in modulo m
def invMod(a, m):
  if(gcdTwo(a, m) != 1):
    return "Invalid, gcd(a,m) != 1"

  r = a % m
  x0, x1 = 1, 0
  y0, y1 = 0, 1
  while (r != 0):
    q = (a - r) / m
    x2 = x0 - q * x1
    y2 = y0 - q * y1

    x0, y0 = x1, y1
    x1, y1 = x2, y2

    a = m
    m = r
    r = a % m
  return int(x2), int(y2)


# convert to lowercase equivalent base 26 number
def textToNum(text):
  x = []
  for i in range(0, len(text)):
    if (text[i] == " "):
      x.append(27) # count spaces as 27 so it's not included in count of letters
    else:
      x.append((ord(text[i].lower()) - ord("a")) % 26)
  return x

# convert to equivalent base 26 number
def numToText(num):
  x = ""
  for i in range(0, len(num)):
    x += chr((num[i] % 26) + ord("a"))
  return x

def counter(inp, m):
  count = [0]*m # count of size m
  for i in range(0, len(inp)):
    if (inp[i] != 27):
      letter = inp[i]
      count[letter] = count[letter]+1

  freq = [0.0]*m
  for i in range(0, m):
    freq[i] = count[i] / len(inp)
  return count, freq

# base frequencies of each letter of the english alphabet
# index corresponds to the index of the letter in the alphabet (A: 0, B: 1 ...)
base_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
             0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
