import unittest
from day9 import decompress

class Test_day9(unittest.TestCase):

	def tests_decompress(self):
		# self.assertEqual(decompress('ADVENT'), 'ADVENT')
		# self.assertEqual(decompress('A(1x5)BC'), 'ABBBBBC')
		# self.assertEqual(decompress('(3x3)XYZ'), 'XYZXYZXYZ')
		self.assertEqual(decompress('A(2x2)BCD(2x2)EFG'), 'ABCBCDEFEFG')
		# self.assertEqual(decompress('(6x1)(1x3)A'), '(1x3)A')
		# self.assertEqual(decompress('X(8x2)(3x3)ABCY'), 'X(3x3)ABC(3x3)ABCY')


if __name__ == '__main__':
	unittest.main()