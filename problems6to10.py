__author__ = 'mani'
import math
import numpy


def isPrime(number):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        r = math.sqrt(number)
        f = 5
        #print number,f,r
        while f <= r:
            if number %f==0 :
                #print "number %f",r, f
                return False
            if number %(f+2) == 0:
                #print "number %(f+2)", r, f
                return False
            f = f + 6
        return True

#problem6: The sum of the squares of the first ten natural numbers is,12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 and 385 is 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def squares6():

    sumSquare = sum(map(lambda i: i*i, [i for i in range(1,101)]))
    squareSum = sum(map(lambda i: i, [i for i in range(1,101)]))
    squareSum = squareSum * squareSum
    print sumSquare, squareSum
    print "difference between the sum of the squares of the first one hundred natural numbers and the square of the sumis {}".format(squareSum - sumSquare)

#problem7:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?


def primes7():
    count = 1
    limit = 10001
    num = 1
    while count < limit:
        num = num + 2
        if isPrime(num):
            count += 1
            if count == limit:
                break
    print num


#problem8:The four adjacent digits in the 1000-digit number that have the greatest product are 9989 = 5832.
valStr="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def adjProduct8():

    adjmax = []
    i=0
    product = 0
    LIMIT_MAX= 13
    limit = i+ LIMIT_MAX
    while limit <= len(valStr):
        if product < reduce(lambda x, y: int(x) * int(y), str(valStr[i:limit])):
            product = reduce(lambda x, y: int(x) * int(y), str(valStr[i:limit]))
            val = int(valStr[i:limit])
        i += 1
        limit = i+ LIMIT_MAX
    print val, numpy.product([int(i) for i in str(val)]),product
    return val, numpy.product([int(i) for i in str(val)]),product
    # max = 0
    # for i, _ in enumerate(valStr[:-12]):
    #     numbers_prod = reduce(lambda x, y: x * y, [int(valStr[x]) for x in range(i, i + 13)])
    #     if numbers_prod > max:
    #         max = numbers_prod
    #         val = valStr[i: i + 13]
    # print numbers_prod, max,valStr[x], val



#problem9:A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,a2+b2 equals c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pythog9():
    val = []
    limit = 1000
    for c in range(0,500):
        for b in range(0, c):
            for a in range(0, b):
                if a < b < c and a+b+c == limit:
                    if a*a + b*b == c*c:
                        product = a*b*c
                        val.append((a,b,c))

    print val, product
    return product


#problem10:The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million

def sumPrime10(limit=2000000):
    newLimit = int(math.sqrt(limit))
    # use the fact that there wouldn't be any prime more than the sqrt(number)
    val = [i for i in range(1,limit) if isPrime(i) == True]
    print sum(val)

if __name__ == '__main__':
    squares6()
    primes7()
    adjProduct8()
    pythog9()
    sumPrime10()