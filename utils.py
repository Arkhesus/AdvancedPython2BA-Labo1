# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math
import scipy.integrate as integration
import scipy.special as special

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n == 0:
		return 1
	if n > 0 :
		return fact(n-1)*n
	if n < 0 :
		raise ValueError("Must be positive")
	

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
		
		Pre: -
		Post: Returns a tuple with zero, one or two elements corresponding
			to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = ((b**2) -(4*a*c))
	

	if delta == 0 :
		rootzero = -b/(2*a)
		return(rootzero)
	if delta < 0 :
		raise ValueError("Delta doesn't exist")
	if delta > 0 :
		rootneg = (-b - math.sqrt(delta))/(2*a)
		rootpos = (-b + math.sqrt(delta))/(2*a)
		return(rootpos, rootneg)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	f = lambda x :eval(function)
	solution = integration.quad(f, lower, upper)
	return solution[0] - solution[1]

if __name__ == '__main__':
	print(fact(5))
	print(roots(4,-4,-24))
	print(integrate('x ** 2 - 1', -1, 1))
