#!/usr/bin/python
import io
import traceback

import connexion
from flask import Response

from jollyjumper.core import get_enjambment
from jollyjumper.pipeline import load_pipeline as enjambment_pipeline
from rantanplan.core import get_scansion
from rantanplan.pipeline import load_pipeline as scansion_pipeline

from .serializers import serialize

# load_pipeline should work as a "singleton"
_load_pipeline = {}

from .addons import is_available, perform


def get_analysis(poem, operations):
    """
    View for /analysis that perform an analysis of poem running the different
    operations on it.
    :param poem: A UTF-8 encoded byte string with the text of the poem
    :param operations: List of strings with the operations to be performed:
                       - "scansion": Performs scansion analysis
                       - "enjambment": Performs enjambment detection
    :return: Response object with a dict with a key for each operation and its
             analysis or a serialized version of it
    """
    analysis = analyze(poem.decode('utf-8'), operations)
    mime = connexion.request.headers.get("Accept")
    serialization = serialize(analysis, mime)
    return Response(serialization, mimetype=mime)


def analyze(poem, operations):
    """
    Perform an analysis of poem running the different operations on it.
    :param poem: A string with the text of the poem
    :param operations: List of strings with the operations to be performed:
                       - "scansion": Performs scansion analysis
                       - "enjambment": Performs enjambment detection
    :return: A dict with a key for each operation and its analysis
    """
    analysis = {}
    for operation in operations:
        # Caching pipelines between calls
        if operation not in _load_pipeline:
            pipeline = locals().get(f"{operation}_pipeline")
            _load_pipeline[operation] = pipeline() if pipeline else lambda x: x
        poem_doc = _load_pipeline[operation](poem)
        if operation == "scansion":
            analysis[operation] = get_traceback(get_scansion, poem_doc)
        if operation == "enjambment":
            output[operation] = get_traceback(get_enjambment, poem_doc)
        if is_available(operation):
            output[operation] = perform(operation, poem)

    return output


def get_traceback(func, *args, **kwargs):
    """
    Captures any possible exception in the execution of func with args
    and kwargs and return a dictionary informing of the error if necessary.
    :param func: Callable to invoke
    :param args: List of arguments to pass in to func
    :param kwargs: List of keyword arguments to pass in to func
    :return: The output of invoking func(*args, **kwards) or a dictionary with
             the exception raised if any.
    """
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        with io.StringIO() as file:
            traceback.print_exc(limit=1, file=file)
            trace = file.getvalue()
        return {
            "error": type(exc).__name__,
            "message": str(exc),
            "trace": trace,
        }
