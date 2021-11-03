"""
Student: Jyong-Jhih Lin
Mail: jyong-jhih.lin.6989@student.uu.se
Reviewed by: Sven-Erik
Date reviewed: 2011/11/03
"""

import sys  #for command line argument
import random   #for random number
import math #for math.pi, gamma function
import matplotlib.pyplot as plt #for plot
import numpy    #for multi-dimensional array
from time import perf_counter as pc #for perf
import concurrent.futures as future #for parallel


def rnd_pos(x):
    # print(x)  #if I turn this on, it can create more loading and increase the core usage.
    if numpy.inner(x,x) <= 1:
        nc = True
    else:
        nc = False
    return nc


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
    start = 0   #timing
    end = 0 #timing

    #the monte carlo
    x_arr = numpy.array([[random.uniform(-1,1) for j in range(dim)] for i in range(n)])  #List comprehensions
    #comment
    #the build-in random number generator cannot and should not be used in parallel. It will cause error and raising issue.
    #the possible parallel random number generator in numpy is not in the scope of this assignment.
    #therefore, I only parallelize the position checking part.
    start = pc()    #timing
    nc = len(list(filter(lambda x : numpy.inner(x,x) <= 1, x_arr))) #filter()
    end = pc()  #timing
    print(f"1 Process took {round(end-start, 2)} seconds")
##########
    nc = 0
    #n2 = int(n/10)
    start = pc()    #timing
    print('inter parallel')

    # with future.ProcessPoolExecutor(max_workers=10) as ex:    #not good
    #     p1 = ex.submit(rnd_pos, x_arr[0:n2])
    #     p2 = ex.submit(rnd_pos, x_arr[n2:2*n2])
    #     p3 = ex.submit(rnd_pos, x_arr[2*n2:3*n2])
    #     p4 = ex.submit(rnd_pos, x_arr[3*n2:4*n2])
    #     p5 = ex.submit(rnd_pos, x_arr[4*n2:5*n2])
    #     p6 = ex.submit(rnd_pos, x_arr[5*n2:6*n2])
    #     p7 = ex.submit(rnd_pos, x_arr[6*n2:7*n2])
    #     p8 = ex.submit(rnd_pos, x_arr[7*n2:8*n2])
    #     p9 = ex.submit(rnd_pos, x_arr[8*n2:9*n2])
    #     p10 = ex.submit(rnd_pos, x_arr[9*n2:10*n2])
    #     r1 = p1.result()
    #     r2 = p2.result()
    #     r3 = p3.result()
    #     r4 = p4.result()
    #     r5 = p5.result()
    #     r6 = p6.result()
    #     r7 = p7.result()
    #     r8 = p8.result()
    #     r9 = p9.result()
    #     r10 = p10.result()

    #comment
    #it is the map method automatically decides how many cores it uses.
    #I need to tune the chuck size to have a better speed.
    #it is possible to use "async"+"ProcessPoolExecutor" to enforce using 10 cores all the time, 
    #but "async" is not in the scope of this assignment.
    #I think my code already server the purpose of this assignment.
    with future.ProcessPoolExecutor(max_workers=10) as ex:
        pos_result = ex.map(rnd_pos, x_arr, chunksize=int(n/10))
    end = pc()  #timing
    for r in pos_result:
        if r == True:
            nc = nc+1 

    print(f"10 Process took {round(end-start, 2)} seconds")
    

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




if __name__ == '__main__':
	main()