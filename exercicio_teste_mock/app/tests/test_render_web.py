"""
Module containing the "TestRenderWeb" Class.
"""

from unittest import TestCase
from unittest.mock import patch, MagicMock

from app.src.render_web import render_web


class TestRenderWeb(TestCase):
    """
    Class to assert the render_web function is working as expected.
    """

    # GOOD SCENARIOS
    @patch("app.src.render_web.get_data_from_api")
    def test_should_return_formatted_data_for_single_professor_data(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is formatting the data correctly,
        by asserting the data is formatted when only one record were retrieved from the api.
        """
        fake_return = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "16",
                "predio": ["1", "2", "3", "4"]
            },
        ]

        mock_api_data.return_value = fake_return

        actual = render_web()[0]
        expected = {
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "19:30",
            "periodo": "noturno",
            "sala": "16",
            "predio": "4"
        }

        self.assertDictEqual(actual, expected)

        mock_api_data.assert_called_once()

    @patch("app.src.render_web.get_data_from_api")
    def test_should_return_formatted_data_for_many_professor_data(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is formatting the data correctly,
        by asserting the data is formatted when many records were retrieved from the api.
        """
        fake_return = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "16",
                "predio": ["1", "2", "3", "4"]
            },
            {
                "nomeDoProfessor": "RenZo",
                "horarioDeAtendimento": "17:30",
                "periodo": "integral",
                "sala": "10",
                "predio": ["1", "2", "3", "4"]
            },
            {
                "nomeDoProfessor": "Marcelo",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "3",
                "predio": ["1", "2", "3", "4"]
            },
        ]

        mock_api_data.return_value = fake_return

        actual = render_web()
        expected = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "16",
                "predio": "4"
            },
            {
                "nomeDoProfessor": "RenZo",
                "horarioDeAtendimento": "17:30",
                "periodo": "integral",
                "sala": "10",
                "predio": "2"
            },
            {
                "nomeDoProfessor": "Marcelo",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "3",
                "predio": "1"
            },
        ]

        self.assertListEqual(actual, expected)

        mock_api_data.assert_called_once()

    @patch("app.src.render_web.get_data_from_api")
    def test_should_get_right_building_for_classroom_equals_to_3(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is setting the data correctly
        by assigning the building value correctly.
        """
        fake_return = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "3",
                "predio": ["1", "2", "3", "4"]
            },
        ]

        mock_api_data.return_value = fake_return

        actual = render_web()
        expected = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "3",
                "predio": "1"
            },
        ]

        self.assertListEqual(actual, expected)

        mock_api_data.assert_called_once()

    # BAD SCENARIOS
    @patch("app.src.render_web.get_data_from_api")
    def test_should_return_None_when_api_return_empty_list(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is returning None
        when the API returns an empty list.
        """
        fake_return = []

        mock_api_data.return_value = fake_return

        actual = render_web()
        
        self.assertIsNone(actual)

    @patch("app.src.render_web.get_data_from_api")
    def test_should_return_None_when_api_return_missing_data(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is returning None
        when the API returns a list with missing data.
        """
        fake_return = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "predio": ["1", "2", "3", "4"]
            },
        ]

        mock_api_data.return_value = fake_return

        actual = render_web()
        
        self.assertIsNone(actual)

    @patch("app.src.render_web.get_data_from_api")
    def test_should_return_None_when_api_return_broken_data(self, mock_api_data: MagicMock) -> None:
        """
        Method to assert the render_web function is returning None
        when the API returns a list with broken data.
        """
        fake_return = [
            {
                "nomeDoProfessor": "Chris",
                "horarioDeAtendimento": "19:30",
                "periodo": "noturno",
                "sala": "test_incorrect",
                "predio": ["1", "2", "3", "4"]
            },
        ]

        mock_api_data.return_value = fake_return

        actual = render_web()
        
        self.assertIsNone(actual)
