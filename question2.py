def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        return True
    else:
        return False


for i in range(1, 1001):
    if perfect(i):
        print (i)
