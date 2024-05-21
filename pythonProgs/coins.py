#Alex Melford
#026493127
import random
    
def coin_sim(p): 
  heads = 0 
  for i in range(1000): 
    flips = 0 
    count = 0
    while count == 0: 
      num = random.uniform(0,1) 
      flips += 1 
      if num <= p: 
        if flips % 2 != 0: 
          heads += 1 
        count += 1 
  return heads/1000       

print(coin_sim(0.2))
print(coin_sim(0.5))
print(coin_sim(2/3))


