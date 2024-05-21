# Binomial
import math
import matplotlib.pyplot as dist
n = 100
p = float(input('Enter a probability of success '))
q = 1 - p
X = []
Y = []
for x in range(0, n+1):
 X.append(x)
 c = math.factorial(n) /(math.factorial(x) * math.factorial(n - x))
 prob = c*(p**x)*(q**(n - x))
 Y.append(prob)
 print(prob)
 dist.bar(X,Y)

dist.show()