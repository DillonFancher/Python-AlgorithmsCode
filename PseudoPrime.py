B = True
i = 1
while B:

	i += 1
	a = i**1 % 2
	b = i**2 % 3
	c = i**2012 % 2013
	
	if a == 1 and b == 1 and c == 1:
		B = False
		print('i is 2 pseudoprime, 3 pseudoprime, and 2013 pseudoprime')
		print(i)
	else:
		print('i is not the number we want yet')
		



