#!/usr/bin/python
import io
import json
import traceback
import stardog

import connexion
from flask import Response, g, session
from jollyjumper.core import get_enjambment
from rantanplan.core import get_scansion

# from .addons import is_available, perform
# from .serializers import serialize
from urllib.parse import unquote

import ast
import json

# load_pipeline should work as a "singleton"

_load_pipeline = {}


def get_analysis(poem, operations, rhyme_analysis=False):
    """
    View for /analysis that perform an analysis of poem running the different
    operations on it.
    :param poem: A UTF-8 encoded byte string with the text of the poem
    :param operations: List of strings with the operations to be performed:
                       - "scansion": Performs scansion analysis
                       - "enjambment": Performs enjambment detection
    :param rhyme_analysis: Whether or not rhyme analysis is to be performed
    :return: Response object with a dict with a key for each operation and its
             analysis or a serialized version of it
    """
    analysis = analyze(poem.decode('utf-8'), operations, rhyme_analysis)
    mime = connexion.request.headers.get("Accept")
    # serialization = serialize(analysis, mime)
    return Response(json.dumps(analysis), mimetype=mime)


def analyze(poem, operations, rhyme_analysis=False):
    """
    Perform an analysis of poem running the different operations on it.
    :param poem: A string with the text of the poem
    :param operations: List of strings with the operations to be performed:
                       - "scansion": Performs scansion analysis
                       - "enjambment": Performs enjambment detection
    :param rhyme_analysis: Whether or not rhyme analysis is to be performed
    :return: A dict with a key for each operation and its analysis
    """
    output = {}
    for operation in operations:
        # Caching pipelines between calls
        if operation not in _load_pipeline:
            pipeline = locals().get(f"{operation}_pipeline")
            _load_pipeline[operation] = pipeline() if pipeline else lambda x: x
        poem_doc = _load_pipeline[operation](poem)
        if operation == "scansion":
            output[operation] = get_traceback(get_scansion, poem_doc,
                                              rhyme_analysis=rhyme_analysis,
                                              always_return_rhyme=rhyme_analysis,
                                              split_stanzas_on='\n{2,}',
                                              alternative_output=True)
        elif operation == "enjambment":
            output[operation] = get_traceback(get_enjambment, poem_doc)
        else:
            availability = is_available(operation)
            if "error" not in availability:
                output[operation] = perform(operation, poem)
            else:
                output[operation] = availability
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


def get_poeticWorks():
    conn = get_db()
    query = get_queries()['poeticWorks']
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def get_poeticWork(title, limit=10):

    title = unquote(title)
    conn = get_db()
    query = get_queries()['poeticWork'].replace('$*', title + '*').replace('$limit', str(limit))
    results = conn.graph(query, content_type=stardog.content_types.LD_JSON)
    return process_jsonld(results)


def get_authors():
    conn = get_db()
    query = get_queries()['authors']
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def get_author(name, limit=10):
    name = unquote(name)
    conn = get_db()
    query = get_queries()['author'].replace('$*', name + '*').replace('$limit', str(limit))
    results = conn.graph(query, content_type=stardog.content_types.LD_JSON)
    return process_jsonld(results)

def get_manifestations():
    # conn = get_db()
    # query = get_queries()['manifestations']
    # results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    # return results
    return {'TODO': 'TODO'}

def get_book(title):
    # title = unquote(title)
    # conn = get_db()
    # query = get_queries()['book']
    # results = conn.graph(query, content_type=stardog.content_types.LD_JSON)
    # return process_jsonld(results)
    return {'TODO': '?'}


def connect_to_database():
    connection_details = {
        'endpoint': 'http://62.204.199.252:5820',
        'username': 'admin',
        'password': 'LuckyLuke99',
    }
    database_name = "PD_KG"
    with stardog.Admin(**connection_details) as admin:
        if database_name in [db.name for db in admin.databases()]:
            return stardog.Connection(database_name, **connection_details)
        else:
            raise Exception(f"No database with the name: {database_name}")


def get_db():
    if 'db' not in g:
        g.db = connect_to_database()
    return g.db


def get_queries():
    # if 'queries' not in session.keys():
    #     with open('poetrylab_api/queries.txt') as f:
    #         queries = f.read()
    #         session['queries'] = ast.literal_eval(queries)
    # return session['queries']
    with open('poetrylab_api/queries.txt') as f:
        queries = f.read()
        queries = ast.literal_eval(queries)
    return queries


def process_jsonld(results):
    results = results.decode('utf8').replace("'", '"')
    return json.loads(results)


