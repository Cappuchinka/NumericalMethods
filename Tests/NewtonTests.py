import unittest
from task3 import finite_difference, a_n


class MyTestCase(unittest.TestCase):
    def test_finite_difference_k_equals_0(self, _y=None):
        if _y is None:
            _y = [0, 1, 2, 3, 4]
        result = finite_difference(0, _y)
        self.assertEqual(_y[0], result, str("Expected: ") + str(_y[0]) + str("; Actual: ") + str(result))

    def test_finite_difference_k_equals_1(self, _y=None):
        if _y is None:
            _y = [0, 1, 2, 3, 4]
        result = finite_difference(1, _y)
        expected = _y[1] - _y[0]
        self.assertEqual(expected, result, str("Expected: ") + str(_y[0]) + str("; Actual: ") + str(result))

    def test_finite_difference_k_equals_2(self, _y=None):
        if _y is None:
            _y = [0, 1, 2, 3, 4]
        result = finite_difference(2, _y)
        expected = (_y[2] - _y[1]) - (_y[1] - _y[0])
        self.assertEqual(expected, result, str("Expected: ") + str(_y[0]) + str("; Actual: ") + str(result))

    def test_finite_difference_k_equals_3(self, _y=None):
        if _y is None:
            _y = [0, 1, 2, 3, 4]
        result = finite_difference(3, _y)
        expected = ((_y[3] - _y[2]) - (_y[2] - _y[1])) - ((_y[2] - _y[1]) - (_y[1] - _y[0]))
        self.assertEqual(expected, result, str("Expected: ") + str(_y[0]) + str("; Actual: ") + str(result))

    def test_finite_difference_k_equals_4(self, _y=None):
        if _y is None:
            _y = [0, 1, 2, 3, 4]
        result = finite_difference(4, _y)
        expected = (((_y[4] - _y[3]) - (_y[3] - _y[2])) - ((_y[2] - _y[1]) - (_y[1] - _y[0]))) - (
                ((_y[3] - _y[2]) - (_y[2] - _y[1])) - ((_y[2] - _y[1]) - (_y[1] - _y[0])))
        self.assertEqual(expected, result, str("Expected: ") + str(_y[0]) + str("; Actual: ") + str(result))

    def test_a_0(self, _y=None):
        if _y is None:
            _y = [0.693, 0.792, 1.169, 1.832, 2.797]
        result = a_n(0, finite_difference(0, _y), _y, 1)
        expected = finite_difference(0, _y)

        self.assertEqual(expected, result, str("Expected: ") + str(expected) + str("; Actual: ") + str(result))

    def test_a_1(self, _y=None):
        if _y is None:
            _y = [0.693, 0.792, 1.169, 1.832, 2.797]
        result = a_n(1, finite_difference(0, _y), _y, 1)
        expected = finite_difference(1, _y)

        self.assertEqual(expected, result, str("Expected: ") + str(expected) + str("; Actual: ") + str(result))

    def test_a_2(self, _y=None):
        if _y is None:
            _y = [0.693, 0.792, 1.169, 1.832, 2.797]
        result = a_n(2, finite_difference(1, _y), _y, 1)
        expected = finite_difference(2, _y) / 2

        self.assertEqual(expected, result, str("Expected: ") + str(expected) + str("; Actual: ") + str(result))

    def test_a_3(self, _y=None):
        if _y is None:
            _y = [0.693, 0.792, 1.169, 1.832, 2.797]
        result = a_n(3, finite_difference(2, _y) / 2, _y, 1)
        expected = finite_difference(3, _y) / 6

        self.assertEqual(expected, result, str("Expected: ") + str(expected) + str("; Actual: ") + str(result))

    def test_a_4(self, _y=None):
        if _y is None:
            _y = [0.693, 0.792, 1.169, 1.832, 2.797]
        result = a_n(4, finite_difference(3, _y) / 6, _y, 1)
        expected = finite_difference(4, _y) / 24

        self.assertEqual(expected, result, str("Expected: ") + str(expected) + str("; Actual: ") + str(result))


if __name__ == '__main__':
    unittest.main()
