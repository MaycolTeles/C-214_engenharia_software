"""
Module containing the "get_data_from_api" function.
"""

from typing import Dict, List, Union


def get_data_from_api() -> List[Dict[str, Union[str, List[str]]]]:
    """
    Function to retrieve data from an api.

    Returns
    --------
    List[Dict[str, Union[str, List[str]]]]
        A list containing a dictionaryon each index which contains the office hours in the following format:
        {
            "nomeDoProfessor": "<nome_do_professor",
            "horarioDeAtendimento": "<horario_de_atendimento>",
            "periodo": "<integral_ou_noturno>",
            "sala": "<sala_de_atendimento>",
            "predio":[
                "1",
                "2",
                "3",
                "4",
                "6"
            ]
        }
    """
    response: List[Dict[str, Union[str, List[str]]]] = []

    professor_1 = {
        "nomeDoProfessor": "Chris",
        "horarioDeAtendimento": "13:30",
        "periodo": "integral",
        "sala": "2",
        "predio":[
            "3",
            "4",
            "6"
        ]
    }

    professor_2 = {
        "nomeDoProfessor": "RenZo",
        "horarioDeAtendimento": "17:30",
        "periodo": "noturno",
        "sala": "5",
        "predio":[
            "1",
            "2",
        ]
    }

    professor_3 = {
        "nomeDoProfessor": "Marcelo",
        "horarioDeAtendimento": "19:30",
        "periodo": "noturno",
        "sala": "7",
        "predio":[
            "1",
            "2",
            "3",
            "4",
            "6"
        ]
    }

    response.append(professor_1)
    response.append(professor_2)
    response.append(professor_3)

    return response
