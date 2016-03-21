import jalisco
import unittest

class JaliscoIntegracionTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJalicoCalculationAddOne(self):
        input_number = 1
        expected = 2
        self.assertEquals(expected, jalisco.calculate_jalisco_number(1))


if __name__ == '__main__':
    unittest.main()
