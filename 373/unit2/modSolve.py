# ax cong b mod n

#X = each person gets this many in the end
#5*X + 1 = how many before they all leave
#5(5*X + 1)/4 + 1 = how many before the last person steals
#5(5(5*X + 1)/4 + 1)/4 + 1 = how many before the fourth person steals
#5(5(5(5*X + 1)/4 + 1) + 1)/4 + 1 = how many before the third person steals
#5(5(5(5(5*X + 1)/4 + 1) + 1)/4 + 1)/4 + 1 = how many before the second person steals
#5(5(5(5(5(5*X + 1)/4 + 1) + 1)/4 + 1)/4 + 1) = how many before the first person steals

#5X + 1 = an integer

#25X + 9 = 0 mod 4
#25X = 3 mod 4

#(125*X + 61)/16
#125X = -61 mod 16

#(625*X + 369)/64
#625X = -369 mod 64
#625X = -369 mod 64

#(3125*X + 2101)/256
#3125X = -2101 mod 256
#3125X = 203 mod 256

#(15625*X + 11529)/1024
#15625X = -11529 mod 1024

#(78125*X + 61741)/4096
#78125X = -61741 mod 4096

def main():
	#system = [(25, 3, 4),
	#		  (125, 3, 16),
	#		  (625, -369, 64),
	#		  (3125, -2101, 256),
	#		  (15625, -11529, 1024),
	#		  (78125, -61741, 4096)]
	system = [(1, 1, 5**1),
			  (4, 9, 5**2),
			  (4**2, 61, 5**3),
			  (4**3, 369, 5**4),
			  (4**4, 2101, 5**5),
			  (4**5, 11529, 5**6)]
	for i in range(len(system)):
		cong = system[i]
		if i == 0:
			sols = modSolve(cong)
		else:
			sols = sols & modSolve(cong)
		print sols
	for sol in sols:
		print sol
		print story(sol)

def modSolve(cong):
	a = cong[0]
	b = cong[1]
	n = cong[2]
	r, s = Euclidean(a,n)
	sols = []
	sol = r*b % n
	#print sol
	for k in range(10000):
		sols.append(sol + n*k)
	return set(sols)

def Euclidean(a, b):
    r = 0
    lastr = 1
    s = 1
    lasts = 0
    while not b == 0:
        q = a / b
        a, b = b, a % b
        r, lastr = lastr - q*r, r
        s, lasts = lasts - q*s, s       
    return (lastr, lasts)

def story(N):
	erin = (N - 1)/5.
	left = N - erin
	sami = (left - 1)/5.
	left = left - sami
	elliot = (left -1)/5.
	left = left - elliot
	dad = (left -1)/5.
	left = left - dad
	mom = (left -1)/5.
	left = left - mom
	portion = (left - 1)/5.
	print portion

main()
