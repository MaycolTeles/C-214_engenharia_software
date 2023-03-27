"""
Module containing the "render_web" function.
"""

from typing import Dict, List, Optional

from app.src.api import get_data_from_api


def render_web() -> Optional[List[Dict[str, str]]]:
    """
    Function to render a web page.

    This is just a minor and fake implementation, it doesn't actually renders a web page.

    Returns
    --------
    Optional[List[Dict[str, str]]]
        A dictionary containing lists of each professor's data int the following format:
        [
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
    """
    response = get_data_from_api()

    if not response:
        return

    for professor_data in response:
        classroom = professor_data.get("sala")

        if not classroom:
            return

        building = _get_building_based_on_classroom(classroom)

        if not building:
            return

        professor_data["predio"] = building

    return response


def _get_building_based_on_classroom(classroom: str) -> Optional[str]:
    """
    Private Function to return the building associated to the classroom received as argument.
    """
    if classroom in ["1", "2", "3", "4", "5"]:
        return "1"

    if classroom in ["6", "7", "8", "9", "10"]:
        return "2"

    if classroom in ["11", "12", "13", "14", "15"]:
        return "3"

    if classroom in ["16", "17", "18", "19", "20"]:
        return "4"

    if classroom in ["21", "22", "23", "24", "25"]:
        return "5"

    if classroom in ["26", "27", "28", "29", "30"]:
        return "6"
