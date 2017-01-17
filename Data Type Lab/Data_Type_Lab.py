def data_type(n):
	if type(n) == type([]):
		try:
			x = n[2]
			return x
		except:
			return None
			
	elif n == None:
		return 'no value'
	elif n == True:
		return True
	elif n == False:
		return False
	elif (isinstance (n, int)) == True:
		if n < 100:
			return 'less than 100'
		elif n == 100:
			return 'Equal to 100'
		else:
			return 'more than 100'
	else:
		if (isinstance (n, str)) == True:
			return len(n)