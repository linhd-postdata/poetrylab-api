# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_analyze_scansion 1'] = {
    'scansion': [
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'syllable': 'Ja'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'más'
                },
                {
                    'is_stressed': False,
                    'syllable': 'en'
                },
                {
                    'is_stressed': False,
                    'syllable': 'con'
                },
                {
                    'is_stressed': False,
                    'syllable': 'tra'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'ré'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'más'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'fiel'
                },
                {
                    'is_stressed': True,
                    'syllable': 'a'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'mi'
                }
            ],
            'rhythm': {
                'length': 10,
                'stress': '-+---++++-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'Ja'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'más'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'en'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'con'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'tra'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'ré'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'más'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'fiel'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'symbol': '-'
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'go'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'queen',
                    'synalepha_index': [
                        2
                    ]
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'los'
                },
                {
                    'is_stressed': True,
                    'sinaeresis_index': [
                        1
                    ],
                    'syllable': 'peo'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'res'
                },
                {
                    'is_stressed': False,
                    'syllable': 'mo'
                },
                {
                    'is_stressed': True,
                    'syllable': 'men'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'tos'
                },
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'rri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                }
            ],
            'rhythm': {
                'length': 11,
                'stress': '+--+--+--+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'que'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'en'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'los'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'has_sinaeresis': True,
                            'is_stressed': False,
                            'syllable': 'pe'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'o'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'res'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'mo'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'men'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'tos'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'rri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'y'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'no'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'sinaeresis_index': [
                        2
                    ],
                    'syllable': 'trae'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'mi'
                },
                {
                    'is_stressed': True,
                    'syllable': 'ver'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'de'
                }
            ],
            'rhythm': {
                'length': 7,
                'stress': '-+-+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'y'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'no'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'has_sinaeresis': True,
                            'is_stressed': True,
                            'syllable': 'tra'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'e'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'ver'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'de'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'bri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'go'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'que'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'su'
                },
                {
                    'is_stressed': True,
                    'syllable': 'cuer'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'poa',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': True,
                    'syllable': 'mial',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'maa',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'ba'
                },
                {
                    'is_stressed': True,
                    'syllable': 'ti'
                },
                {
                    'is_stressed': False,
                    'syllable': 'daya',
                    'synalepha_index': [
                        1,
                        2
                    ]
                },
                {
                    'is_stressed': True,
                    'syllable': 'ni'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                }
            ],
            'rhythm': {
                'length': 14,
                'stress': '-+---+-+--+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'bri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'que'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'su'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'cuer'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'po'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'a'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'al'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'ma'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'ba'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'ti'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'da'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'y'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'ni'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': True,
                    'syllable': 'dán'
                },
                {
                    'is_stressed': False,
                    'syllable': 'do'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'meel',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'ca'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'lor'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'del'
                },
                {
                    'is_stressed': False,
                    'syllable': 'me'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'jor'
                },
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'bri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'go'
                }
            ],
            'rhythm': {
                'length': 11,
                'stress': '+---+--+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -3,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'dán'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'do'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'el'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'ca'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'lor'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'del'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'me'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'jor'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'bri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'symbol': '.'
                }
            ]
        }
    ]
}

snapshots['test_analyze_enjambment 1'] = {
    'enjambment': {
        0: {
            'on': [
                'ami',
                'go'
            ],
            'type': 'tmesis'
        },
        2: {
            'on': [
                'ADJ',
                'NOUN'
            ],
            'type': 'sirrematic'
        }
    }
}

snapshots['test_analyze_enjambment_scansion 1'] = {
    'enjambment': {
        0: {
            'on': [
                'ami',
                'go'
            ],
            'type': 'tmesis'
        },
        2: {
            'on': [
                'ADJ',
                'NOUN'
            ],
            'type': 'sirrematic'
        }
    },
    'scansion': [
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'syllable': 'Ja'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'más'
                },
                {
                    'is_stressed': False,
                    'syllable': 'en'
                },
                {
                    'is_stressed': False,
                    'syllable': 'con'
                },
                {
                    'is_stressed': False,
                    'syllable': 'tra'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'ré'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'más'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'fiel'
                },
                {
                    'is_stressed': True,
                    'syllable': 'a'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'mi'
                }
            ],
            'rhythm': {
                'length': 10,
                'stress': '-+---++++-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'Ja'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'más'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'en'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'con'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'tra'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'ré'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'más'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'fiel'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'symbol': '-'
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'go'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'queen',
                    'synalepha_index': [
                        2
                    ]
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'los'
                },
                {
                    'is_stressed': True,
                    'sinaeresis_index': [
                        1
                    ],
                    'syllable': 'peo'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'res'
                },
                {
                    'is_stressed': False,
                    'syllable': 'mo'
                },
                {
                    'is_stressed': True,
                    'syllable': 'men'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'tos'
                },
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'rri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                }
            ],
            'rhythm': {
                'length': 11,
                'stress': '+--+--+--+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'que'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'en'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'los'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'has_sinaeresis': True,
                            'is_stressed': False,
                            'syllable': 'pe'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'o'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'res'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'mo'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'men'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'tos'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'rri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'y'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'no'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'sinaeresis_index': [
                        2
                    ],
                    'syllable': 'trae'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'mi'
                },
                {
                    'is_stressed': True,
                    'syllable': 'ver'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'de'
                }
            ],
            'rhythm': {
                'length': 7,
                'stress': '-+-+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'y'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'no'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'has_sinaeresis': True,
                            'is_stressed': True,
                            'syllable': 'tra'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'e'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'ver'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'de'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'bri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'go'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'que'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'su'
                },
                {
                    'is_stressed': True,
                    'syllable': 'cuer'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'poa',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': True,
                    'syllable': 'mial',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'maa',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'ba'
                },
                {
                    'is_stressed': True,
                    'syllable': 'ti'
                },
                {
                    'is_stressed': False,
                    'syllable': 'daya',
                    'synalepha_index': [
                        1,
                        2
                    ]
                },
                {
                    'is_stressed': True,
                    'syllable': 'ni'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'me'
                }
            ],
            'rhythm': {
                'length': 14,
                'stress': '-+---+-+--+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'bri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'que'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'su'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'cuer'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'po'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'a'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'mi'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'al'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'ma'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'ba'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'ti'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'da'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'y'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'ni'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                }
            ]
        },
        {
            'phonological_groups': [
                {
                    'is_stressed': True,
                    'syllable': 'dán'
                },
                {
                    'is_stressed': False,
                    'syllable': 'do'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'meel',
                    'synalepha_index': [
                        1
                    ]
                },
                {
                    'is_stressed': False,
                    'syllable': 'ca'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'lor'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'del'
                },
                {
                    'is_stressed': False,
                    'syllable': 'me'
                },
                {
                    'is_stressed': True,
                    'is_word_end': True,
                    'syllable': 'jor'
                },
                {
                    'is_stressed': False,
                    'syllable': 'a'
                },
                {
                    'is_stressed': True,
                    'syllable': 'bri'
                },
                {
                    'is_stressed': False,
                    'is_word_end': True,
                    'syllable': 'go'
                }
            ],
            'rhythm': {
                'length': 11,
                'stress': '+---+--+-+-',
                'type': 'pattern'
            },
            'tokens': [
                {
                    'stress_position': -3,
                    'word': [
                        {
                            'is_stressed': True,
                            'syllable': 'dán'
                        },
                        {
                            'is_stressed': False,
                            'syllable': 'do'
                        },
                        {
                            'has_synalepha': True,
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'me'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'el'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'ca'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'lor'
                        }
                    ]
                },
                {
                    'stress_position': 0,
                    'word': [
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'del'
                        }
                    ]
                },
                {
                    'stress_position': -1,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'me'
                        },
                        {
                            'is_stressed': True,
                            'is_word_end': True,
                            'syllable': 'jor'
                        }
                    ]
                },
                {
                    'stress_position': -2,
                    'word': [
                        {
                            'is_stressed': False,
                            'syllable': 'a'
                        },
                        {
                            'is_stressed': True,
                            'syllable': 'bri'
                        },
                        {
                            'is_stressed': False,
                            'is_word_end': True,
                            'syllable': 'go'
                        }
                    ]
                },
                {
                    'symbol': '.'
                }
            ]
        }
    ]
}

snapshots['test_get_analysis_scansion 1'] = GenericRepr('<Response 8324 bytes [200 OK]>')

snapshots['test_get_analysis_enjambment 1'] = GenericRepr('<Response 114 bytes [200 OK]>')

snapshots['test_get_analysis_enjambment_scansion 1'] = GenericRepr('<Response 8438 bytes [200 OK]>')
