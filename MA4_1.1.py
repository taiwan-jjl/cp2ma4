"""
Student: Jyong-Jhih Lin
Mail: jyong-jhih.lin.6989@student.uu.se
Reviewed by: Sven-Erik
Date reviewed: 2011/11/03
"""

import sys  #for command line argument
import random   #for random number
import math #for math.pi
import matplotlib.pyplot as plt #for plot


def main():
    #check input argument
    if len(sys.argv) != 2:
        print('input argument error')
        print(sys.argv)
        quit()
    elif not sys.argv[1].isnumeric():
        print('input argument is not numeric')
        print(sys.argv[1])
        quit()

    n = int(sys.argv[1])    #n points
    random.seed(1)  #fix seed

    x_arr = [0]*n  #x array
    y_arr = [0]*n  #y array
    col_arr = ['']*n    #color array
    nc = 0 #counter for inside the circle

    #the monte carlo
    for i in range(n):
        x_arr[i] = random.uniform(-1,1)
        y_arr[i] = random.uniform(-1,1)
        if x_arr[i]**2 + y_arr[i]**2 <= 1:
            col_arr[i] = 'red'
            nc = nc + 1
        else:
            col_arr[i] = 'blue'

    #Print the number of points nc that are inside the circle.
    print('nc = ', nc)

    #Print the approximation of π ≈ 4 nc / n.
    print('the approximation of pi = ', 4*nc/n)

    #Print the builtin constant π (math.pi) of Python.
    print('math.pi = ', math.pi)

    #Produce a png file that shows all points inside the circle as red dots and points outside the circle as blue dots (like Figure 2).
    plt.scatter(x_arr, y_arr, 1, col_arr)
    plt.axis('square')
    plt.show()

if __name__ == '__main__':
	main()


