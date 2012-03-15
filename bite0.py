#!/usr/bin/env python

""" Mi hola mundo, blaba bla bla
Las triple comillas me permiten hacer comentario multi-linea
see!
"""

def helloworld():
    a = __name__
    return "goodbye WOOOOORLDzu ",a

print helloworld()

def fib(n):
    print 'n = ', n
    if n > 1:
        return n * fib(n-1)
    else:
        print 'end of the line'
        return 1

