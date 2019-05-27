import json
import pytest
from poetrylab_api import app


@pytest.fixture(scope='module')
def client():
    with app.app.test_client() as test_client:
        yield test_client


def test_health(client):
    text = """Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo."""
    response = client.post('/analysis?operations=enjambment&operations=scansion', data=text)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        'scansion': [{'tokens': [{'word': [{'syllable': 'Ja', 'is_stressed': False},
                                           {'syllable': 'más', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'en', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'con', 'is_stressed': False},
                                           {'syllable': 'tra', 'is_stressed': False},
                                           {'syllable': 'ré', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'más', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'fiel', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'symbol': 'ami-'}]},
                     {'tokens': [{'word': [{'syllable': 'go', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'que',
                                            'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'en', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'los', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'pe', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'o', 'is_stressed': True},
                                           {'syllable': 'res', 'is_stressed': False}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'mo', 'is_stressed': False},
                                           {'syllable': 'men', 'is_stressed': True},
                                           {'syllable': 'tos', 'is_stressed': False}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'a', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'rri', 'is_stressed': True},
                                           {'syllable': 'me', 'is_stressed': False}],
                                  'stress_position': -2}]},
                     {'tokens': [{'word': [{'syllable': 'y', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'no', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'me', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'tra', 'is_stressed': True,
                                            'has_sinaeresis': True},
                                           {'syllable': 'e', 'is_stressed': False}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'mi', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'ver', 'is_stressed': True},
                                           {'syllable': 'de', 'is_stressed': False}],
                                  'stress_position': -2}]},
                     {'tokens': [{'word': [{'syllable': 'a',
                                            'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'bri', 'is_stressed': True},
                                           {'syllable': 'go', 'is_stressed': False}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'que', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'su', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'cuer', 'is_stressed': True},
                                           {'syllable': 'po', 'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'a', 'is_stressed': True,
                                            'has_sinaeresis': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'mi', 'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'al', 'is_stressed': True,
                                            'has_sinaeresis': True},
                                           {'syllable': 'ma', 'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'a', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'ba', 'is_stressed': False},
                                           {'syllable': 'ti', 'is_stressed': True},
                                           {'syllable': 'da', 'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': -2},
                                 {'word': [{'syllable': 'y', 'is_stressed': True,
                                            'has_synalepha': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'a', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'ni', 'is_stressed': True},
                                           {'syllable': 'me', 'is_stressed': False}],
                                  'stress_position': -2}]},
                     {'tokens': [{'word': [{'syllable': 'dán', 'is_stressed': True},
                                           {'syllable': 'do', 'is_stressed': False},
                                           {'syllable': 'me', 'is_stressed': False,
                                            'has_synalepha': True}],
                                  'stress_position': -3},
                                 {'word': [{'syllable': 'el', 'is_stressed': False}],
                                  'stress_position': 0},
                                 {'word': [{'syllable': 'ca', 'is_stressed': False},
                                           {'syllable': 'lor', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'del', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'me', 'is_stressed': False},
                                           {'syllable': 'jor', 'is_stressed': True}],
                                  'stress_position': -1},
                                 {'word': [{'syllable': 'a', 'is_stressed': False,
                                            'has_sinaeresis': True},
                                           {'syllable': 'bri', 'is_stressed': True},
                                           {'syllable': 'go', 'is_stressed': False}],
                                  'stress_position': -2},
                                 {'symbol': '.'}]}],
        'enjambment': {'0': ['tmesis', ['ami', 'go']],
                       '2': ['sirrematic', ['ADJ', 'NOUN']]}}
