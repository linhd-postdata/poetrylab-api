import pytest
from rdflib import Graph
from unittest import mock

from poetrylab_api.core import analyze
from poetrylab_api.serializers import FORMATS
from poetrylab_api.serializers import serialize


@pytest.mark.parametrize("mime, format", list(FORMATS.items()))
def test_serialize(snapshot, mime, format):
    text = """Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
-
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo."""
    operations = ("scansion", )
    analysis = analyze(text, operations)
    serialization = serialize(analysis, mime)
    Graph().parse(data=serialization, format=format)
    assert True
