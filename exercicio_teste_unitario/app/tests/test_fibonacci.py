"""
Module to test the "main()" function.
"""

from unittest import TestCase

from src.fibonacci import calculate_fibonacci


class TestCalculateFibonacci(TestCase):
    """
    Class to test the "main()" function.
    """

    def test_should_return_0_when_stop_is_0(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to 0 when the stop parameters is 0.
        """
        stop = 0

        actual = calculate_fibonacci(stop)
        expected = 0

        self.assertEqual(actual, expected)

    def test_should_return_1_when_stop_is_1(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to 1 when the stop parameters is 1.
        """
        stop = 1

        actual = calculate_fibonacci(stop)
        expected = 1

        self.assertEqual(actual, expected)
    
    def test_should_return_1_when_stop_is_2(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to 1 when the stop parameters is 2.
        """
        stop = 2

        actual = calculate_fibonacci(stop)
        expected = 1

        self.assertEqual(actual, expected)

    def test_should_return_2_when_stop_is_3(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to 2 when the stop parameters is 3.
        """
        stop = 3

        actual = calculate_fibonacci(stop)
        expected = 2

        self.assertEqual(actual, expected)

    def test_should_return_3_when_stop_is_4(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to 3 when the stop parameters is 4.
        """
        stop = 3

        actual = calculate_fibonacci(stop)
        expected = 2

        self.assertEqual(actual, expected)

    def test_should_return_X_when_stop_is_10(self) -> None:
        """
        Method to assert the calculate_fibonacci function returns a value equals to X when the stop parameters is 10.
        """
        stop = 10

        actual = calculate_fibonacci(stop)
        expected = 55

        self.assertEqual(actual, expected)