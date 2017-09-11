__author__ = 'mani'
import math
import numpy

'''
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
'''

'''
#problem7:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
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

'''
'''
#problem8:The four adjacent digits in the 1000-digit number that have the greatest product are 9989 = 5832.
valStr="73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def adjProduct8():

    adjmax = []
    i=0
    LIMIT_MAX= 13
    limit = i+ LIMIT_MAX
    while i < len(valStr):
        if "0" not in valStr[i:limit]:
            adjmax.append(int(valStr[i:limit]))
        i += 1
        limit = i+ LIMIT_MAX
    print max(adjmax), numpy.product([int(i) for i in str(max(adjmax))]), reduce(lambda x, y: int(x) * int(y), str(max(adjmax)))
    return max(adjmax),numpy.product([int(i) for i in str(max(adjmax))])
'''

if __name__ == '__main__':
    #squares6()
    #primes7()
    #adjProduct8()


