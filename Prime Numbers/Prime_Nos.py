def PrimeFunc(n):
	""" Prints a list containing Prime Numbers between 2 and the defined parameter (n)"""
	RetnList = [True]* n  # O(n)
	for x in range(3,int(n**0.5) + 1, 2): # O(n+1)
		if RetnList[i]:
		
			RetnList[i*i::2*i] = [False]*((n-1*i-1)/(2*i)+1)  
				
	return [2] + [i for i in range(3, n, 2) if RetnList[i]] # O(n+1)
	
	# O(n+1)
		
		