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
        "scansion": [
            {
                "tokens": [
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "ver"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "de"
                            }
                        ]
                    }
                ]
            },
            {
                "tokens": [
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "bri"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "go"
                            }
                        ]
                    }
                ]
            }
        ]
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
        "scansion": [
            {
                "tokens": [
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "Ja"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "más"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "en"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "con"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "tra"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "ré"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "más"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "fiel"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "mi"
                            }
                        ]
                    },
                    {
                        "symbol": "-"
                    }
                ]
            },
            {
                "tokens": [
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "go"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "que"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "en"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "los"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "has_sinaeresis": True,
                                "is_stressed": False,
                                "syllable": "pe"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "o"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "res"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "mo"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "men"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "tos"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "rri"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "me"
                            }
                        ]
                    }
                ]
            },
            {
                "tokens": [
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "y"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "no"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "me"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "has_sinaeresis": True,
                                "is_stressed": True,
                                "syllable": "tra"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "e"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "mi"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "ver"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "de"
                            }
                        ]
                    }
                ]
            },
            {
                "tokens": [
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "bri"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "go"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "que"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "su"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "cuer"
                            },
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "po"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "mi"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "al"
                            },
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "ma"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "ba"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "ti"
                            },
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "da"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "has_synalepha": True,
                                "is_stressed": True,
                                "syllable": "y"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "ni"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "me"
                            }
                        ]
                    }
                ]
            },
            {
                "tokens": [
                    {
                        "stress_position": -3,
                        "word": [
                            {
                                "is_stressed": True,
                                "syllable": "dán"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "do"
                            },
                            {
                                "has_synalepha": True,
                                "is_stressed": False,
                                "syllable": "me"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "el"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "ca"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "lor"
                            }
                        ]
                    },
                    {
                        "stress_position": 0,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "del"
                            }
                        ]
                    },
                    {
                        "stress_position": -1,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "me"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "jor"
                            }
                        ]
                    },
                    {
                        "stress_position": -2,
                        "word": [
                            {
                                "is_stressed": False,
                                "syllable": "a"
                            },
                            {
                                "is_stressed": True,
                                "syllable": "bri"
                            },
                            {
                                "is_stressed": False,
                                "syllable": "go"
                            }
                        ]
                    },
                    {
                        "symbol": "."
                    }
                ]
            }
        ]
    }
