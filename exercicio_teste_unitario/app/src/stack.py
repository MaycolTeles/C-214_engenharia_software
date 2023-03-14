"""
Module containing the "Stack" and "EmptyStackException" classes.
"""

from typing import Any, List



class EmptyStackException(Exception):
    """
    Exception that should be raised when the stack is empty.
    """


class Stack():
    """
    Class to represent a stack.
    """
    _elements: List[Any] = []

    def push(self, element: Any) -> None:
        """
        Method to add an element into the stack.

        Parameters
        ----------
        element : Any
            The element to be inserted into the stack.
        """
        self._elements.append(element)

    def pop(self) -> Any:
        """
        Method to remove and return the last inserted element from the stack.

        Returns
        --------
        Any
            The stack's last element.
        """
        if not self._elements:
            raise EmptyStackException()

        element = self._elements[-1]

        self._elements = self._elements[:-1]

        return element
