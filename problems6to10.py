__author__ = 'mani'


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


if __name__ == '__main__':
    squares6()



