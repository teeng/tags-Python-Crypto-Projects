# find the gcd of three integers a, b, c
def gcdThree(r0, r1, r2):
    # gcd(a, b, c) = gcd(gcd(a, b), c))

    def gcdTwo(r0, r1):
      r2 = r0 % r1

      while(r2 != 0):
        r0 = r1
        r1 = r2
        r2 = r0 % r1
      return r1

    gcd_ab = gcdTwo(r0, r1)
    gcd_abc = gcdTwo(gcd_ab, r2)
    print("gcd(", r0, ",", r1, ",", r2, "): ", gcd_abc, sep='')


# test the function with given inputs:
gcdThree(-144, 2058, 302526)
gcdThree(3674160, -243, 51030)
gcdThree(-733, -21379, 46782)
