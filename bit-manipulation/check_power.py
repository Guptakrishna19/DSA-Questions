def checkPower(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n//2
    return n==1  #if n becomes 1 that mean number is power of two
print(checkPower(9))
