from PrimeNos import primes
import unittest

class primesTestCases(unittest.TestCase):

      def test_it_returns_correct_output_with_positives(self):
            result = primes(11)
            self.assertEqual(result, [2, 3, 5, 7], msg='Invalid output')

      def test_it_returns_a_List(self):
            result = primes(11)
            self.assertIsInstance(result, list, msg="Result returned should be a list")

      def test_only_ints_allowed(self):
            n=11
            primes(n)
            self.assertIsInstance(n, int, msg="Only Integers are allowed")
            
if __name__ == '__main__':
      unittest.main()
