def adder(*args, **kwargs):
    res = 0
    for i in args:
        res += i
    for i in kwargs:
        res += i
    return res


import unittest


class My_Test(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(5, adder(2, 2))

    def test_neg_adder(self):
        self.assertEqual(-3, adder(-2, -2))

    def test_mix(self):
        self.assertEqual(1, adder(-2, 2))


if __name__ == '__main__':
    unittest.main()