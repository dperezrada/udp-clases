import jalisco
import unittest
import json

class JaliscoFuncionalTestCase(unittest.TestCase):

    def setUp(self):
        jalisco.app.config['TESTING'] = True
        self.app = jalisco.app.test_client()

    def tearDown(self):
        pass

    def testJaliscoAlwaysWinsIfInputCorrectNumber(self):
        input_number = 1
        expected = 'Yo gano con el 2'
        response = self.app.get('/?number=%s' % input_number)

        response_message = json.loads(response.data)['message']
        self.assertEquals(expected, response_message)


if __name__ == '__main__':
    unittest.main()
