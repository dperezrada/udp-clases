import jalisco
import unittest
import mock

class JaliscoUnitarioTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('jalisco.store_in_database', mock.Mock(side_effect=lambda x: 'SAVED mocked'))
    def testJalicoCalculationAddOne(self):
        input_number = 1
        expected = 2
        self.assertEquals(expected, jalisco.calculate_jalisco_number(1))


if __name__ == '__main__':
    unittest.main()
