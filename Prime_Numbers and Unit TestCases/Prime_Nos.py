import unittest

def PrimeFunc(n):
	""" Prints a list containing Prime Numbers between 2 and the defined parameter (n)"""
	if (isinstance (n, int)) == True:
		RetnList = [True]* n  # O(n)
		for i in range(3,int(n**0.5) + 1, 2): # O(n+1)
			if RetnList[i]:
				RetnList[i*i::2*i] = [False]*((n-1*i-1)/(2*i)+1)  
				
		return [2] + [i for i in range(3, n, 2) if RetnList[i]] # O(n+1)
	
						
	
class PrimeFuncTestCases(unittest.TestCase):
	def test_it_runs_with_numbers_greater_2(self):
		primes(n) 
		assertGreater(n, 2, msg="number input should be greater than 2")

	
    def test_it_does_not_accept_strings(self):
		with self.assertRaises(TypeError) as context:
			primes(a)
			self.assertEqual(
				"The provided input is not an Integer"
				context.exception.message, "Invalid input of type Sttring not allowed"
				)
				
    def test_it_does_not_accept_strings(self):
		with self.assertRaises(TypeError) as context:
			primes(a)
			self.assertEqual(
				"The provided input is not an Integer"
				context.exception.message, "Invalid input of type Sttring not allowed"
				)

	def test_it_returns_a_List(self):
		result = primes(11)
		self.assertIsInstance(result, list, msg="Result returned should be a list")
		
	def test_only_ints_allowed(self):
		primes(n)
		self.assertIsInstance(n, int, msg="Only Integers are allowed")

		
		