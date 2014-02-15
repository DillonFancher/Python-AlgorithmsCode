def getrand100():
	from random import randint
	a = 10**100
	b = (10**101)-1
	return randint(a,b)

def nextprime(n):
	
	
	b = n
	c = 0
	T = True
	while T:
		b+=1
		c = 0
		for x in range(0, 11):
			a = pow(x, b-1, b)
			
			if a == 1:
				
				c+=1
			
						
		if c == 10:
			T = False
		else:
			T = True
			
			
	return(b)

def average_distance():
	c = 0
	for x in range(0, 11):
		a = getrand100()
		b = nextprime(a)
		c = c + b - a
		print(b-a)
	avg = c/10
	print('average is')
	print(avg)

print(nextprime(2013**50))
average_distance()
