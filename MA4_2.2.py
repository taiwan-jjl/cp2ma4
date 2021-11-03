"""
Student: Jyong-Jhih Lin
Mail: jyong-jhih.lin.6989@student.uu.se
Reviewed by: Sven-Erik
Date reviewed: 2011/11/03
"""

import matplotlib.pyplot as plt #for plot
from time import perf_counter as pc #for perf
from numba import njit  #for numba
from integer import Integer #for c++

def fib_pure_py(n):
    if n <= 1:
        return n
    else:
        return(fib_pure_py(n-1) + fib_pure_py(n-2))

@njit
def fib_numba_py(n):
    if n <= 1:
        return n
    else:
        return(fib_numba_py(n-1) + fib_numba_py(n-2))


def main():
    #part 1
    t_py = []
    t_numba = []
    t_cpp = []
    n_arr = range(30,46)

    for i in n_arr:
        start = pc()
        fib_pure_py(i)
        end = pc()
        t_py.append(end-start)

        start = pc()
        fib_numba_py(i)
        end = pc()
        t_numba.append(end-start)

        start = pc()
        f = Integer(i)
        f.fib()
        end = pc()
        t_cpp.append(end-start)

    plt.figure()
    plt.plot(n_arr, t_py, label='pure py')
    plt.plot(n_arr, t_numba, label='numba')
    plt.plot(n_arr, t_cpp, label='cpp')
    plt.xlabel('n')
    plt.ylabel('seconds')
    plt.title('Fibonacci numbers')
    plt.legend()
    plt.savefig("py_numba_cpp.png")
    # plt.show()


    #part 2
    t_py = []
    t_numba = []
    t_cpp = []
    n_arr = range(1,31)

    for i in n_arr:
        start = pc()
        fib_pure_py(i)
        end = pc()
        t_py.append(end-start)

        start = pc()
        fib_numba_py(i)
        end = pc()
        t_numba.append(end-start)

    plt.figure()
    plt.plot(n_arr, t_py, label='pure py')
    plt.plot(n_arr, t_numba, label='numba')
    plt.xlabel('n')
    plt.ylabel('seconds')
    plt.title('Fibonacci numbers')
    plt.legend()
    plt.savefig("py_numba.png")
    # plt.show()


    #part 3
    t_py = []
    t_numba = []
    t_cpp = []
    n_arr = range(47,48)

    for i in n_arr:
        start = pc()
        fib_numba = fib_numba_py(i)
        end = pc()
        t_numba.append(end-start)

        start = pc()
        f = Integer(i)
        fib_cpp = f.fib()
        end = pc()
        t_cpp.append(end-start)

    print('n = 47, numba time = ', t_numba)
    print('n = 47, cpp time = ', t_cpp)
    print('fib 47 via numba = ', fib_numba)
    print('fib 47 via cpp = ', fib_cpp)

    



    #debug
    # print(fib_pure_py(10))
    # print(fib_numba_py(10))

    # f = Integer(5)
    # print(f.get())
    # f.set(10)
    # print(f.fib())


if __name__ == '__main__':
	main()