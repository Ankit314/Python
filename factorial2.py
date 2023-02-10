from math import factorial


def per(n,r):
    
    if (n>r):
      return factorial(n)/factorial(n-r)
    print("permutation",n,r)