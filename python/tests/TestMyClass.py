import myclass
import unittest

class TestMyClass(unittest.TestCase):

	def setUp(self):
	
	def test_myfunction(self):
	
		#self.assertTrue(self.portalAdmin.is_logged_in, "Logged in user not known.")
		

if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
	unittest.TextTestRunner(verbosity=1).run(suite)