# Hypergeometric
import math
import matplotlib.pyplot as dist
G = int(input('Enter the number of green blocks. '))
R = int(input('Enter the number of red blocks. '))
N = G + R
n = G
X = []
Y = []
for j in range(0, n + 1):
 X.append(j)
 numerator = (math.factorial(G) / ((math.factorial(j) * math.factorial(G - j)))) *\
 (math.factorial(R) / ((math.factorial(n - j) * math.factorial(R - (n - j)))))
 denominator = math.factorial(N) / (math.factorial(n) * (math.factorial(N - n)))
 prob = numerator / denominator
 Y.append(prob)
 print(prob)
 dist.bar(X,Y)
dist.show()