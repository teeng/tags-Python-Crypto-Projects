# finding inverse modulo
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


# timing naive modulo inverse function (it's not very efficient)
import time
n = [777, -37, 24865, -256789, -1900757]
m = [26, 512, 4096, 56789, 770077]

for i in range(len(n)):
  start_time = time.time()
  modulo_inverse_naive(n[i], m[i])
  end_time = time.time()
  print(f"Run time in seconds (s) for n: {n[i]} and m: {m[i]} = ({end_time - start_time})")


