#!/usr/bin/python
from jollyjumper.core import get_enjambment
from rantanplan.core import get_scansion


def get_analysis(poem, operations):
    """
    :param poem: A string with the text of the poem
    :param operations: List of strings with the operations to be performed:
                            "scansion": Performs scansion analysis
                            "enjambment": Performs enjambment detection
    :return: Python dict with a key for each operation and its analysis
    """
    poem = poem.decode('utf-8')
    output = {}
    for operation in operations:
        if operation == "scansion":
            output[operation] = get_scansion(poem)
        if operation == "enjambment":
            output[operation] = get_enjambment(poem)
    return output
