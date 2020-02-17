import json
from functools import reduce

from flask import Response

from .ontologies import get_scansion_graph

FORMATS = {
    "application/ld+json": "json-ld",
    "application/rdf+xml": "xml",
    "application/n-triples": "nt",
    "application/x-turtle": "turtle",
    "text/turtle": "turtle",
    "text/rdf+n3": "n3",
    "text/n3": "n3",
}


def serialize(obj, mime=None):
    """Serialize a dictionary with keys for core attributes, scansion, and
    enjambment into a string with RDF/LOD data. If the MIME type specified is
    not supported, the same object will be returned as a JSON string
    :param obj: Dict to serialize
    :para mime: String with the MIME type of the resulting response
    """
    graphs = []
    if obj.get("scansion"):
        graph = get_scansion_graph(obj["scansion"])
        graphs.append(graph)
    if mime in FORMATS.keys():
        graph = reduce(lambda x, y: x + y, graphs)  # union on graphs
        return graph.serialize(format=FORMATS[mime])
    else:
        return json.dumps(obj)
