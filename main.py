import random
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
def calc():
  for i in range(factorial(996)*factorial(996)):
    a = []
    a2a = []
    for i in range(100):
      a2a.append(i)
    for i in range(factorial(6)):
      lower = random.choice(a2a)
      upper = random.choice(a2a)
      for num in range(lower, upper + 1):
        if num > 1:
          for i in range(2, num):
            if (num % i) == 0:
              break
    num = random.choice(a2a)
    for i in range(num+12):
      a.append(i)
    int_var1 = random.choice(a)
    a2b = [factorial(int_var1), (int_var1**int_var1)**10, int_var1**num]
    int_var2 = random.choice(a2b)
    print(int_var2)
calc()