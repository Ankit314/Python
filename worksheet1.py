def checkPrimeNum(gvnnum):
    
    countfactrs = 0
    for m in range(1, gvnnum+1):
        if gvnnum % m == 0:
            countfactrs = countfactrs + 1
     
    if countfactrs == 2:
        return True
 
numbr = 562
print('The twin primes below the number', numbr, 'are :')
 
for m in range(2, numbr):
  
    if (checkPrimeNum(m) == True and checkPrimeNum(m+2) == True):
        print('('+str(m)+','+str(m+2)+')', end='  ')