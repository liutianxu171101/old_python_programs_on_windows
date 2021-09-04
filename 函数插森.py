import math
def PrimeNum(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
        
    return True

for i in range(2,200):
#    a = PrimeNum(i)
#    if a :
        print(i)
#        print()
        
