#!/usr/bin/python
import io
import json
import traceback
import stardog

import connexion
from flask import Response
from jollyjumper.core import get_enjambment
from rantanplan.core import get_scansion

from .addons import is_available, perform
from .serializers import serialize
from urllib.parse import unquote

# load_pipeline should work as a "singleton"
_load_pipeline = {}

dumb_mode = True
dumb_query = 'select * { ?a ?p ?o }'


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
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def get_poeticWork(title):
    title = unquote(title)
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results

def get_authors():
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results

def get_author(name):
    name = unquote(name)
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results

def get_manifestations():
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def get_redaction(name):
    name = unquote(name)
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def get_book(title):
    title = unquote(title)
    if dumb_mode:
        create_dumb_database()
    conn, admin, database_name = conntect_to_database()
    query = dumb_query
    results = conn.select(query, content_type=stardog.content_types.SPARQL_JSON)
    return results


def conntect_to_database():
    connection_details = {
        'endpoint': 'http://localhost:5820',
        'username': 'admin',
        'password': 'admin'
    }
    database_name = "test_database"
    with stardog.Admin(**connection_details) as admin:
        if database_name in [db.name for db in admin.databases()]:
            return stardog.Connection(database_name, **connection_details), admin, database_name
        else:
            raise Exception(f"No database with the name: {database_name}")

def create_dumb_database():
    connection_details = {
        'endpoint': 'http://localhost:5820',
        'username': 'admin',
        'password': 'admin',
    }
    database_name = "test_database"
    with stardog.Admin(**connection_details) as admin:
        if database_name in [db.name for db in admin.databases()]:
            admin.database(database_name).drop()
        db = admin.new_database(database_name)

        conn = stardog.Connection(database_name, **connection_details)
        conn.begin()
        conn.add(stardog.content.File('poetrylab_api/example.ttl'))
        conn.commit()  # commit the transaction
        conn.__exit__()