"""
Module containing the "StackTest" Class.
"""

from unittest import TestCase

from src.stack import EmptyStackException, Stack


class StackTest(TestCase):
    """
    Class to assert the stack is working as expected.
    """

    def test_should_raise_exception_when_popping_from_stack_without_any_elements(self) -> None:
        """
        Method to assert the stack raises an exception when it's empty.
        """
        stack = Stack()

        with self.assertRaises(EmptyStackException):
            stack.pop()
