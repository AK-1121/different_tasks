from config import *
import sys
import unittest

module = __import__(TEST_FILE)


class TestLoginString(unittest.TestCase):

    def test_empty_login(self):
        self.assertEqual(module.check_login(''), False)
        
    
    def test_20_length_login(self):
        self.assertEqual(module.check_login('Z'*20), True)
        self.assertEqual(module.check_login('0'*20), False)
    
    def test_21_length_login(self):
        self.assertEqual(module.check_login('a'*21), False)

    
    def test_one_symbol_login(self):
        self.assertEqual(module.check_login('a'), True)
        self.assertEqual(module.check_login('0'), False)
        self.assertEqual(module.check_login('!'), False)
        self.assertEqual(module.check_login('Z'), True)
        
    def test_first_symbol(self):
        self.assertEqual(module.check_login('a0'), True)
        self.assertEqual(module.check_login('0b'), False)
        self.assertEqual(module.check_login('!b'), False)
        self.assertEqual(module.check_login('Z' + 18*'-' + 'z'), True)
        
    def test_unpropriete_symbols(self):
        self.assertEqual(module.check_login('0a'), False)
        self.assertEqual(module.check_login('AB-'), False)
        self.assertEqual(module.check_login('   '), False)
        self.assertEqual(module.check_login('a!a'), False)

      

if __name__ == '__main__':
    print('testing file: ' + TEST_FILE)
    unittest.main()

    