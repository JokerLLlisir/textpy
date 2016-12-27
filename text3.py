while 1:
    isPrime = []
    notPrime = []
    def ifPrime():
        max = int(raw_input('Please input num to text prime:'))
        for a in range(1,max+1):
            index = 0
            for b in range(2,a):
                if a%b == 0:
                    notPrime.append(a)
                    index = 1
            if index == 0:
                    isPrime.append(a)
    ifPrime()
    print 'This is Prime:'
    print  set(isPrime)
    print  'This is not Prime:'
    print  set(notPrime)









