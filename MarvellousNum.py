arr1 = list()
iSum = 0

def ChkPrime(arr1):
    global iSum
    for i in arr1:
        for j in range(2, i):
            if (i%j == 0):
                break
        else:
            iSum = iSum+i
    return iSum

ChkPrime(arr1)
