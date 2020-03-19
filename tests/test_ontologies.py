import pytest
from unittest import mock

from owlready2 import get_ontology
from rdflib import Graph

from poetrylab_api.ontologies import add_structural_individuals
from poetrylab_api.ontologies import get_scansion_graph
from poetrylab_api.ontologies import filter_individuals
from poetrylab_api.ontologies import join_syllables
from poetrylab_api.ontologies import join_tokens
from poetrylab_api.ontologies import onto_to_graph
from poetrylab_api.ontologies import ONTOLOGIES


@pytest.fixture(scope='module')
def tokens():
    return [{
        'stress_position': -1,
        'word': [{
                'is_stressed': False,
                'syllable': 'Ja'
            }, {
                'is_stressed': True,
                'is_word_end': True,
                'syllable': 'más'
            }]
        }, {
        'symbol': ","
        }, {
        'stress_position': -1,
        'word': [{
                'is_stressed': False,
                'syllable': 'en'
            }, {
                'is_stressed': False,
                'syllable': 'con'
            }, {
                'is_stressed': False,
                'syllable': 'tra'
            }, {
                'is_stressed': True,
                'is_word_end': True,
                'syllable': 'ré'
        }]
    }]


def test_onto_to_graph():
    with mock.patch("poetrylab_api.ontologies.filter_individuals",
                    side_effect=None):
        # Code cannot be used for testing since the host it is usually down
        onto = get_ontology(ONTOLOGIES["structural"]).load()
        assert isinstance(onto_to_graph(onto), Graph)


def test_get_scansion_graph(snapshot, tokens):
    scansion = [{
        'null': None,
    }, {
        'tokens': tokens,
    }]
    assert isinstance(get_scansion_graph(scansion), Graph)


def test_add_structural_individuals(tokens):

    class Onto:
        def __init__(self):
            self.Line = mock.MagicMock()
            self.Word = mock.MagicMock()
            self.Syllable = mock.MagicMock()

    scansion = [{
        'null': None,
    }, {
        'tokens': tokens,
    }]
    onto = Onto()
    output = add_structural_individuals(scansion, onto)
    assert output.Line.call_count == 1
    assert output.Word.call_count == 3
    assert output.Syllable.call_count == 6


def test_join_tokens(snapshot, tokens):
    output = join_tokens(tokens)
    snapshot.assert_match(output)


def test_join_syllables(snapshot):
    token = {
        'word': [{
                'is_stressed': False,
                'syllable': 'Ja'
            }, {
                'is_stressed': True,
                'is_word_end': True,
                'syllable': 'más'
            }]
        }
    output = join_syllables(token)
    snapshot.assert_match(output)


def test_join_syllables_symbol(snapshot):
    token = {
        'symbol': ","
    }
    output = join_syllables(token)
    snapshot.assert_match(output)


def test_filter_individuals():
    graph = mock.MagicMock()
    graph.onto.Line = mock.MagicMock
    graph.onto.Word = mock.MagicMock
    graph.onto.Syllable = mock.MagicMock
    assert filter_individuals(graph, s=1)
