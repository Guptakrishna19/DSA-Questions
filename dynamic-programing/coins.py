def coins(amount):
    if amount == 0:
        return print('Invalid value 0')
    coins=[1,2,5,10,20,50,100,200,500,2000]
    n=len(coins)
    # print(n)
    ans=[]
    for i in range(n-1,-1,-1):
        while amount >= coins[i]:
            amount -=coins[i]
            ans.append(coins[i])
    print(ans)       

coins(122)  
    