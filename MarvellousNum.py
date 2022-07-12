def ChkPrime(Num):
    flag = True
    for i in range(2,int(Num/2)+1):
        if((Num%i) == 0):
            flag = False

    return flag        


def PrimeAdd(data):
    sum = 0
    for i in range(len(data)):
        if(ChkPrime(data[i]) == True):
            print(data[i])
            sum = sum + data[i]
    
    return sum        
