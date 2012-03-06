import math
import sys

def gauss(mu, var, x):
	pi = 3.141592653589793238462
	normalizingConstant = (2*pi*var)**(-0.5)
	return normalizingConstant * math.exp((-0.5)*(((x-mu)**2)/var))

mu = sys.argv[1]
var = sys.argv[2]
x = sys.argv[3]
print gauss(mu, var, x)
