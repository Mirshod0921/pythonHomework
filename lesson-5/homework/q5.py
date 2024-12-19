def is_prime(n):
    flag = True
    if n == 1:
        return False
    else:
        for i in range(2, n-1):
            if n%i == 0:
                flag = False
                break
        return flag


            