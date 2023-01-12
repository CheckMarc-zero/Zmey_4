N = int(input('Введите число: '))
def Factor(n):
    Ans =[]
    d = 2
    while d*d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
res = Factor(N)    
print('Простые множители: ')  
print(*res,sep=', ')                  
