import json
import pytest
from poetrylab_api import app


@pytest.fixture(scope='module')
def client():
    with app.app.test_client() as test_client:
        yield test_client


def test_health_enjambment(client):
    text = """ami-
go"""
    response = client.post('/analysis?operations=enjambment', data=text)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "enjambment": {
            "0": {
                "on": [
                    "ami",
                    "go"
                ],
                "type": "tmesis"
            }}}


def test_health_scansion(client):
    text = """verde
abrigo"""
    response = client.post('/analysis?operations=scansion', data=text)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "scansion": [{
                         'tokens': [{
                                        'word': [{
                                                     'syllable': 'ver',
                                                     'is_stressed': True
                                                 },
                                                 {
                                                     'syllable': 'de',
                                                     'is_stressed': False,
                                                     'is_word_end': True
                                                 }],
                                        'stress_position': -2
                                    }],
                         'phonological_groups': [
                             {'syllable': 'ver', 'is_stressed': True},
                             {
                                 'syllable': 'de', 'is_stressed': False,
                                 'is_word_end': True
                             }],
                         'rhythm': {
                             'stress': '+-', 'type': 'pattern', 'length': 2
                         }
                     },
                     {
                         'tokens': [{
                                        'word': [{
                                                     'syllable': 'a',
                                                     'is_stressed': False
                                                 },
                                                 {
                                                     'syllable': 'bri',
                                                     'is_stressed': True
                                                 },
                                                 {
                                                     'syllable': 'go',
                                                     'is_stressed': False,
                                                     'is_word_end': True
                                                 }],
                                        'stress_position': -2
                                    }],
                         'phonological_groups': [
                             {'syllable': 'a', 'is_stressed': False},
                             {'syllable': 'bri', 'is_stressed': True},
                             {
                                 'syllable': 'go', 'is_stressed': False,
                                 'is_word_end': True
                             }],
                         'rhythm': {
                             'stress': '-+-', 'type': 'pattern', 'length': 3
                         }
                     }]
    }


def test_health(client):
    text = """Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo."""
    response = client.post('/analysis?operations=enjambment&operations=scansion', data=text)
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "enjambment": {
            "0": {
                "on": [
                    "ami",
                    "go"
                ],
                "type": "tmesis"
            },
            "2": {
                "on": [
                    "ADJ",
                    "NOUN"
                ],
                "type": "sirrematic"
            }
        },
        'scansion': [{
            'tokens': [{
                'word': [{
                    'syllable': 'Ja',
                    'is_stressed': False
                },
                    {
                        'syllable': 'más',
                        'is_stressed': True,
                        'is_word_end': True
                    }],
                'stress_position': -1
            },
                {
                    'word': [{
                        'syllable': 'en',
                        'is_stressed': False
                    },
                        {
                            'syllable': 'con',
                            'is_stressed': False
                        },
                        {
                            'syllable': 'tra',
                            'is_stressed': False
                        },
                        {
                            'syllable': 'ré',
                            'is_stressed': True,
                            'is_word_end': True
                        }],
                    'stress_position': -1
                },
                {
                    'word': [{
                        'syllable': 'más',
                        'is_stressed': True,
                        'is_word_end': True
                    }],
                    'stress_position': -1
                },
                {
                    'word': [{
                        'syllable': 'fiel',
                        'is_stressed': True,
                        'is_word_end': True
                    }],
                    'stress_position': -1
                },
                {
                    'word': [{
                        'syllable': 'a',
                        'is_stressed': True
                    },
                        {
                            'syllable': 'mi',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                    'stress_position': -2
                },
                {'symbol': '-'}],
            'phonological_groups': [
                {'syllable': 'Ja', 'is_stressed': False},
                {
                    'syllable': 'más', 'is_stressed': True,
                    'is_word_end': True
                },
                {'syllable': 'en', 'is_stressed': False},
                {'syllable': 'con', 'is_stressed': False},
                {'syllable': 'tra', 'is_stressed': False},
                {
                    'syllable': 'ré', 'is_stressed': True,
                    'is_word_end': True
                },
                {
                    'syllable': 'más', 'is_stressed': True,
                    'is_word_end': True
                },
                {
                    'syllable': 'fiel', 'is_stressed': True,
                    'is_word_end': True
                },
                {'syllable': 'a', 'is_stressed': True},
                {
                    'syllable': 'mi', 'is_stressed': False,
                    'is_word_end': True
                }],
            'rhythm': {
                'stress': '-+---++++-', 'type': 'pattern',
                'length': 10
            }
        },
            {
                'tokens': [{
                    'word': [{
                        'syllable': 'go',
                        'is_stressed': True,
                        'is_word_end': True
                    }],
                    'stress_position': -1
                },
                    {
                        'word': [{
                            'syllable': 'que',
                            'is_stressed': False,
                            'has_synalepha': True,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'en',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'los',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'pe',
                            'is_stressed': False,
                            'has_sinaeresis': True
                        },
                            {
                                'syllable': 'o',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'res',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'mo',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'men',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'tos',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'a',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'rri',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'me',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    }],
                'phonological_groups': [{
                    'syllable': 'go',
                    'is_stressed': True,
                    'is_word_end': True
                },
                    {
                        'syllable': 'queen',
                        'is_stressed': False,
                        'synalepha_index': [2],
                        'is_word_end': True
                    },
                    {
                        'syllable': 'los',
                        'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'peo',
                        'is_stressed': True,
                        'sinaeresis_index': [1]
                    },
                    {
                        'syllable': 'res',
                        'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'mo',
                        'is_stressed': False
                    },
                    {
                        'syllable': 'men',
                        'is_stressed': True
                    },
                    {
                        'syllable': 'tos',
                        'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'a',
                        'is_stressed': False
                    },
                    {
                        'syllable': 'rri',
                        'is_stressed': True
                    },
                    {
                        'syllable': 'me',
                        'is_stressed': False,
                        'is_word_end': True
                    }],
                'rhythm': {
                    'stress': '+--+--+--+-', 'type': 'pattern',
                    'length': 11
                }
            },
            {
                'tokens': [{
                    'word': [{
                        'syllable': 'y',
                        'is_stressed': False,
                        'is_word_end': True
                    }],
                    'stress_position': 0
                },
                    {
                        'word': [{
                            'syllable': 'no',
                            'is_stressed': True,
                            'is_word_end': True
                        }],
                        'stress_position': -1
                    },
                    {
                        'word': [{
                            'syllable': 'me',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'tra',
                            'is_stressed': True,
                            'has_sinaeresis': True
                        },
                            {
                                'syllable': 'e',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'mi',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'ver',
                            'is_stressed': True
                        },
                            {
                                'syllable': 'de',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    }],
                'phonological_groups': [{
                    'syllable': 'y',
                    'is_stressed': False,
                    'is_word_end': True
                },
                    {
                        'syllable': 'no',
                        'is_stressed': True,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'me',
                        'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'trae',
                        'is_stressed': True,
                        'sinaeresis_index': [2],
                        'is_word_end': True
                    },
                    {
                        'syllable': 'mi',
                        'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'ver',
                        'is_stressed': True
                    },
                    {
                        'syllable': 'de',
                        'is_stressed': False,
                        'is_word_end': True
                    }],
                'rhythm': {
                    'stress': '-+-+-+-', 'type': 'pattern',
                    'length': 7
                }
            },
            {
                'tokens': [{
                    'word': [{
                        'syllable': 'a',
                        'is_stressed': False
                    },
                        {
                            'syllable': 'bri',
                            'is_stressed': True
                        },
                        {
                            'syllable': 'go',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                    'stress_position': -2
                },
                    {
                        'word': [{
                            'syllable': 'que',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'su',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'cuer',
                            'is_stressed': True
                        },
                            {
                                'syllable': 'po',
                                'is_stressed': False,
                                'has_synalepha': True,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'a',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'mi',
                            'is_stressed': False,
                            'has_synalepha': True,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'al',
                            'is_stressed': True
                        },
                            {
                                'syllable': 'ma',
                                'is_stressed': False,
                                'has_synalepha': True,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'a',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'ba',
                                'is_stressed': False
                            },
                            {
                                'syllable': 'ti',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'da',
                                'is_stressed': False,
                                'has_synalepha': True,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {
                        'word': [{
                            'syllable': 'y',
                            'is_stressed': False,
                            'has_synalepha': True,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'a',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'ni',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'me',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    }],
                'phonological_groups': [
                    {'syllable': 'a', 'is_stressed': False},
                    {'syllable': 'bri', 'is_stressed': True},
                    {
                        'syllable': 'go', 'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'que', 'is_stressed': False,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'su', 'is_stressed': False,
                        'is_word_end': True
                    },
                    {'syllable': 'cuer', 'is_stressed': True},
                    {
                        'syllable': 'poa',
                        'is_stressed': False,
                        'synalepha_index': [1],
                        'is_word_end': True
                    },
                    {
                        'syllable': 'mial', 'is_stressed': True,
                        'synalepha_index': [1]
                    },
                    {
                        'syllable': 'maa', 'is_stressed': False,
                        'synalepha_index': [1]
                    },
                    {'syllable': 'ba', 'is_stressed': False},
                    {'syllable': 'ti', 'is_stressed': True},
                    {
                        'syllable': 'daya', 'is_stressed': False,
                        'synalepha_index': [1, 2]
                    },
                    {'syllable': 'ni', 'is_stressed': True},
                    {
                        'syllable': 'me', 'is_stressed': False,
                        'is_word_end': True
                    }],
                'rhythm': {
                    'stress': '-+---+-+--+-+-', 'type': 'pattern',
                    'length': 14
                }
            },
            {
                'tokens': [{
                    'word': [{
                        'syllable': 'dán',
                        'is_stressed': True
                    },
                        {
                            'syllable': 'do',
                            'is_stressed': False
                        },
                        {
                            'syllable': 'me',
                            'is_stressed': False,
                            'has_synalepha': True,
                            'is_word_end': True
                        }],
                    'stress_position': -3
                },
                    {
                        'word': [{
                            'syllable': 'el',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'ca',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'lor',
                                'is_stressed': True,
                                'is_word_end': True
                            }],
                        'stress_position': -1
                    },
                    {
                        'word': [{
                            'syllable': 'del',
                            'is_stressed': False,
                            'is_word_end': True
                        }],
                        'stress_position': 0
                    },
                    {
                        'word': [{
                            'syllable': 'me',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'jor',
                                'is_stressed': True,
                                'is_word_end': True
                            }],
                        'stress_position': -1
                    },
                    {
                        'word': [{
                            'syllable': 'a',
                            'is_stressed': False
                        },
                            {
                                'syllable': 'bri',
                                'is_stressed': True
                            },
                            {
                                'syllable': 'go',
                                'is_stressed': False,
                                'is_word_end': True
                            }],
                        'stress_position': -2
                    },
                    {'symbol': '.'}],
                'phonological_groups': [
                    {'syllable': 'dán', 'is_stressed': True},
                    {'syllable': 'do', 'is_stressed': False},
                    {
                        'syllable': 'meel',
                        'is_stressed': False,
                        'synalepha_index': [1],
                        'is_word_end': True
                    },
                    {'syllable': 'ca', 'is_stressed': False},
                    {
                        'syllable': 'lor', 'is_stressed': True,
                        'is_word_end': True
                    },
                    {
                        'syllable': 'del', 'is_stressed': False,
                        'is_word_end': True
                    },
                    {'syllable': 'me', 'is_stressed': False},
                    {
                        'syllable': 'jor', 'is_stressed': True,
                        'is_word_end': True
                    },
                    {'syllable': 'a', 'is_stressed': False},
                    {'syllable': 'bri', 'is_stressed': True},
                    {
                        'syllable': 'go', 'is_stressed': False,
                        'is_word_end': True
                    }],
                'rhythm': {
                    'stress': '+---+--+-+-', 'type': 'pattern',
                    'length': 11
                }
            }]
    }
