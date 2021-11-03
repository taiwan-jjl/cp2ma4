"""
Student: Jyong-Jhih Lin
Mail: jyong-jhih.lin.6989@student.uu.se
Reviewed by:
Date reviewed:
"""

import sys  #for command line argument
import random   #for random number
import math #for math.pi, gamma function
import matplotlib.pyplot as plt #for plot
import numpy    #for multi-dimensional array


def main():
    #check input argument
    if len(sys.argv) != 3:
        print('input argument error')
        print(sys.argv)
        quit()
    elif not sys.argv[1].isnumeric():
        print('input argument 1 is not numeric')
        print(sys.argv[1])
        quit()
    elif not sys.argv[2].isnumeric():
        print('input argument 2 is not numeric')
        print(sys.argv[1])
        quit()

    n = int(sys.argv[1])    #n points
    dim = int(sys.argv[2])    #dimension
    random.seed(1)  #fix seed

    x_arr = numpy.zeros((n, dim))
    col_arr = ['']*n    #color array
    nc = 0 #counter for inside the circle

    #the monte carlo
    x_arr = numpy.array([[random.uniform(-1,1) for j in range(dim)] for i in range(n)])  #List comprehensions
    nc = len(list(filter(lambda x : numpy.inner(x,x) <= 1, x_arr))) #filter()

    for i in range(n):

        # for j in range(dim):
        #     x_arr[i][j] = random.uniform(-1,1)

        if numpy.inner(x_arr[i,:], x_arr[i,:]) <= 1:
            col_arr[i] = 'red'
            # nc = nc + 1
        else:
            col_arr[i] = 'blue'

    #Print the number of points nc that are inside the circle.
    print('nc = ', nc)

    #Print the approximation of π ≈ 4 nc / n.
    pi_app = lambda nc, n, dim : (nc/n*(2**dim)*math.gamma(dim/2+1))**(2/dim)   #Lambda-functions
    print('the approximation of pi = ', pi_app(nc, n, dim) )

    #Print the builtin constant π (math.pi) of Python.
    print('math.pi = ', math.pi)

    #Produce a png file that shows all points inside the circle as red dots and points outside the circle as blue dots (like Figure 2).
    # plt.scatter(x_arr[:,0], x_arr[:,1], 1, col_arr)
    # plt.axis('square')
    # plt.show()

    print('exact Vd(1) = ', math.pi**(dim/2)/math.gamma(dim/2+1))
    print('app. Vd(1) = ', nc/n*2**dim)

if __name__ == '__main__':
	main()


