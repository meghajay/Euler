__author__ = 'mani'

#problem1:If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#solution1:straight forward method
def natural1A():
    sum = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print "soln1. sum of all the multiples of 3 or 5 below 10 is {}".format(sum)


##solution2:using list comprehensions and lambda, for some reason sum(list) is not working
def natural1B():
    val =reduce(lambda a,b: a+b,[i for i in range(1,1000) if (i%3 == 0 or i%5 == 0)])
    print "soln2. sum of all the multiples of 3 or 5 below 10 is {}".format(val)



#problem2: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

#solution1:find the fibonacci within 4 million(4000000)
def fibonacci2():
    def fib(limit):
        sum = 0
        a = 1
        b = 1
        ll = []
        while b < limit:
            sum = a + b
            a = b
            b =sum
            ll.append(sum) if sum%2 == 0 else None
        print ll
        return ll

    solution = reduce(lambda a,b: a+b,[val for val in fib(limit = 4000000)])
    print "solution for fibonacii series upto 4 million is {}".format(solution)

#problem3:The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#solution1:
def primefactor3():
    import math
    n = 600851475143
    #n = 13195
    if n % 2 == 0:
        lastFactor=2
        n=n/2
        while n%2==0:
            n=n/2
    else:
        lastFactor=1
    factor=3

    print lastFactor

    while n > 1:
        if n % factor == 0:
            n = n / factor
            lastfactor = factor
            print "++++++++++",lastfactor,n
            while n % factor == 0:
                n = n/factor
        factor = factor + 2

    print "lastfactor is {}".format(lastfactor)


#problem4:A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009
#91times99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome4():
    largestPalindrome = 0


    for i in range(999,90,-1):
        for j in range(999,900,-1):
                val = i * j
                if (str(val) == str(val)[::-1]) and  (val > largestPalindrome):
                    print i,j
                    largestPalindrome = val

    print "largerst plaindrome is {}".format(largestPalindrome)
    return largestPalindrome

palindrome4()


#problem5:2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def small5():
    num = 10
    while num >= 0:
        val = all(map(lambda y:num%y==0,[i for i in range(1,21)]))
        if val:
            print num
            return num
        num += 10

if __name__ == '__main__':
    import timeit

    natural1A()
    natural1B()
    fibonacci2()
    primefactor3()
    palindrome4()
    print(timeit.timeit(small5,number =1))




