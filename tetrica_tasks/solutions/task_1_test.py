import unittest
from task_1 import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def concat(a: str, b: str) -> str:
    return a + b

@strict
def is_equal(a: bool, b: bool) -> bool:
    return a == b


class TestStrictDecorator(unittest.TestCase):

    def test_correct_int(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_incorrect_int_float(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.0)

    def test_correct_str(self):
        self.assertEqual(concat("a", "b"), "ab")

    def test_incorrect_str_int(self):
        with self.assertRaises(TypeError):
            concat("a", 1)

    def test_correct_bool(self):
        self.assertTrue(is_equal(True, True))

    def test_incorrect_bool_str(self):
        with self.assertRaises(TypeError):
            is_equal(True, "False")


if __name__ == '__main__':
    unittest.main()
