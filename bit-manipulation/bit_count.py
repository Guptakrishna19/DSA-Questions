def getBinary(n):
    s=''
    while n>0:
        s =str(n%2) + s
        n=n//2
    return s
def count(st):
    count=0
    for i in st:
        if i =='1':
            count=count+1
    return count        
    
print(getBinary(3))
st=getBinary(3)
print(count(st))