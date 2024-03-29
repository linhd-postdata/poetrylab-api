# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_analysis_enjambment 1'] = {
    'enjambment': {
        '0': {
            'on': [
                'ami',
                'go'
            ],
            'type': 'tmesis'
        }
    }
}

snapshots['test_analysis_enjambment_scansion 1'] = {
    'enjambment': {
        '0': {
            'on': [
                'ami',
                'go'
            ],
            'type': 'tmesis'
        },
        '2': {
            'on': [
                'ADJ',
                'NOUN'
            ],
            'type': 'sirrematic'
        }
    },
    'scansion': [
        [
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
    ]
}

snapshots['test_analysis_enjambment_scansion_structure 1'] = {
    'enjambment': {
        '4': {
            'on': [
                'CONJ',
                'NOUN'
            ],
            'type': 'sirrematic_relation_words_conjunction'
        },
        '5': {
            'on': [
                'CONJ',
                'ADJ'
            ],
            'type': 'sirrematic_relation_words_conjunction'
        }
    },
    'scansion': [
        [
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'La'
                    },
                    {
                        'is_stressed': False,
                        'syllable': 'ce'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'bo'
                    },
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'syllable': 'llaes',
                        'synalepha_index': [
                            2
                        ]
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 5,
                    'length_range': {
                        'max_length': 6,
                        'min_length': 5
                    },
                    'stress': '--++-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': 0,
                        'word': [
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'La'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'ce'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'bo'
                            },
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'lla'
                            }
                        ]
                    },
                    {
                        'stress_position': -1,
                        'word': [
                            {
                                'is_stressed': True,
                                'is_word_end': True,
                                'syllable': 'es'
                            }
                        ]
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': False,
                        'syllable': 'ce'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'rra'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'day',
                        'synalepha_index': [
                            1
                        ]
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'po'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'bre'
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 5,
                    'length_range': {
                        'max_length': 6,
                        'min_length': 5
                    },
                    'stress': '-+-+-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'ce'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'rra'
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
                                'is_stressed': True,
                                'syllable': 'po'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'bre'
                            }
                        ]
                    },
                    {
                        'symbol': ':'
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': False,
                        'syllable': 'es'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'car'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'cha'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'de'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'tus'
                    },
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'sinaeresis_index': [
                            1
                        ],
                        'syllable': 'días'
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 7,
                    'length_range': {
                        'max_length': 8,
                        'min_length': 7
                    },
                    'stress': '-+---+-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'es'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'car'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'cha'
                            }
                        ]
                    },
                    {
                        'stress_position': 0,
                        'word': [
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'de'
                            }
                        ]
                    },
                    {
                        'stress_position': 0,
                        'word': [
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'tus'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'has_sinaeresis': True,
                                'is_stressed': True,
                                'syllable': 'dí'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'as'
                            }
                        ]
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'y'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'de'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'mis'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'no'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'ches'
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 5,
                    'length_range': {
                        'max_length': 5,
                        'min_length': 5
                    },
                    'stress': '---+-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
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
                        'stress_position': 0,
                        'word': [
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'de'
                            }
                        ]
                    },
                    {
                        'stress_position': 0,
                        'word': [
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'mis'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'no'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'ches'
                            }
                        ]
                    },
                    {
                        'symbol': '.'
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': True,
                        'syllable': 'Ham'
                    },
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'syllable': 'brey',
                        'synalepha_index': [
                            2
                        ]
                    }
                ],
                'rhyme': 'a',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 3,
                    'length_range': {
                        'max_length': 4,
                        'min_length': 3
                    },
                    'stress': '++-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'Ham'
                            },
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'bre'
                            }
                        ]
                    },
                    {
                        'stress_position': -1,
                        'word': [
                            {
                                'is_stressed': True,
                                'is_word_end': True,
                                'syllable': 'y'
                            }
                        ]
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': True,
                        'syllable': 'hie'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'lo'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'ne'
                    },
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'syllable': 'groy',
                        'synalepha_index': [
                            2
                        ]
                    }
                ],
                'rhyme': 'a',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 5,
                    'length_range': {
                        'max_length': 6,
                        'min_length': 5
                    },
                    'stress': '+-++-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'hie'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'lo'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'ne'
                            },
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'gro'
                            }
                        ]
                    },
                    {
                        'stress_position': -1,
                        'word': [
                            {
                                'is_stressed': True,
                                'is_word_end': True,
                                'syllable': 'y'
                            }
                        ]
                    }
                ]
            },
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
                    {
                        'is_stressed': True,
                        'syllable': 'gran'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'dey',
                        'synalepha_index': [
                            1
                        ]
                    },
                    {
                        'is_stressed': False,
                        'syllable': 're'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'don'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'da'
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 5,
                    'length_range': {
                        'max_length': 6,
                        'min_length': 5
                    },
                    'stress': '+--+-',
                    'type': 'pattern'
                },
                'structure': 'septilla',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'gran'
                            },
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'de'
                            }
                        ]
                    },
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
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 're'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'don'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'da'
                            }
                        ]
                    },
                    {
                        'symbol': '.'
                    }
                ]
            }
        ]
    ]
}

snapshots['test_analysis_enjambment_scansion_structure_alternative_output 1'] = {
    'enjambment': {
        '4': {
            'on': [
                'CONJ',
                'NOUN'
            ],
            'type': 'sirrematic_relation_words_conjunction'
        },
        '5': {
            'on': [
                'CONJ',
                'ADJ'
            ],
            'type': 'sirrematic_relation_words_conjunction'
        }
    },
    'scansion': {
        'enjambment': [
            {
                'absoluteLineNumber': '',
                'on': '',
                'type': ''
            }
        ],
        'stanzaList': [
            {
                'content': '''La cebolla es 
cerrada y pobre:
escarcha de tus días
y de mis noches.
Hambre y 
hielo negro y 
grande y redonda.''',
                'isMetricStanza': True,
                'lineList': [
                    {
                        'absoluteLineNumber': 1,
                        'content': 'La cebolla es ',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 6,
                            'lineMinLength': 5,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '--++-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'la ce BO LLAES',
                            'syllabicMetricalLength': 5,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'La',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'ce',
                                'isStressed': False,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'bo',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'llaes',
                                'isStressed': True,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': [
                                    2
                                ],
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 1,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': '-',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'La',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'La',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'cebolla',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'ce',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': False,
                                        'is_stressed': False,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'bo',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'lla',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': True,
                                        'has_synalepha': True,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'es',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'es',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': True,
                                        'is_stressed': True,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 2,
                        'content': 'cerrada y pobre:',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 6,
                            'lineMinLength': 5,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '-+-+-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'ce RRA day PO bre',
                            'syllabicMetricalLength': 5,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'ce',
                                'isStressed': False,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'rra',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'day',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': [
                                    1
                                ],
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'po',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'bre',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 2,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': '-',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'cerrada',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'ce',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': False,
                                        'is_stressed': False,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'rra',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'da',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': True,
                                        'has_synalepha': True,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'y',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'y',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'pobre',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'po',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'bre',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': ':',
                                'type': 'symbol'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 3,
                        'content': 'escarcha de tus días',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 8,
                            'lineMinLength': 7,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '-+---+-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'es CAR cha de tus DÍAS',
                            'syllabicMetricalLength': 7,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'es',
                                'isStressed': False,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'car',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'cha',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'de',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'tus',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'días',
                                'isStressed': True,
                                'isWordEnd': True,
                                'sinaeresisIndex': [
                                    1
                                ],
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 3,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': '-',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'escarcha',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'es',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': False,
                                        'is_stressed': False,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'car',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'cha',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'de',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'de',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'tus',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'tus',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'días',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'dí',
                                        'hasSinaeresis': True,
                                        'hasSynalepha': False,
                                        'has_sinaeresis': True,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'as',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 4,
                                'wordSense': 'example_wordSense'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 4,
                        'content': 'y de mis noches.',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 5,
                            'lineMinLength': 5,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '---+-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'y de mis NO ches',
                            'syllabicMetricalLength': 5,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'y',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'de',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'mis',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'no',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'ches',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 4,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': '-',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'y',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'y',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'de',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'de',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'mis',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'mis',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'noches',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'no',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'ches',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 4,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': '.',
                                'type': 'symbol'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 5,
                        'content': 'Hambre y ',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 4,
                            'lineMinLength': 3,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '++-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'HAM BREY',
                            'syllabicMetricalLength': 3,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'Ham',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'brey',
                                'isStressed': True,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': [
                                    2
                                ],
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 5,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': 'a',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'Hambre',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'Ham',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'bre',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': True,
                                        'has_synalepha': True,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'y',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'y',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': True,
                                        'is_stressed': True,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 6,
                        'content': 'hielo negro y ',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 6,
                            'lineMinLength': 5,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '+-++-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'HIE lo NE GROY',
                            'syllabicMetricalLength': 5,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'hie',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'lo',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'ne',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'groy',
                                'isStressed': True,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': [
                                    2
                                ],
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 6,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': 'a',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'hielo',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'hie',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'lo',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'negro',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'ne',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'gro',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': True,
                                        'has_synalepha': True,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'y',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'y',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': True,
                                        'is_stressed': True,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            }
                        ]
                    },
                    {
                        'absoluteLineNumber': 7,
                        'content': 'grande y redonda.',
                        'firstHemistich': 'example_firstHemistich',
                        'foot': [
                            {
                                'clausula': 'example_clausula',
                                'footNumber': 1,
                                'footType': 'example_footType',
                                'isDividedBy': 'example_isDividedBy',
                                'isHypermetrical': False,
                                'isIrregular': False,
                                'nextFootAfterCaesura': 'example_nextFootAfterCaesura',
                                'previousFootBeforeCaesura': 'example_previousFootBeforeCaesura',
                                'scheme': 'example_scheme'
                            }
                        ],
                        'isRefrain': False,
                        'linePattern': {
                            'accentedVowels': 'example_accentedVowels',
                            'accentedVowelsPattern': 'example_accentedVowelsPattern',
                            'altMoraeMetricalScheme': 'example_altMoraeMetricalScheme',
                            'altPatterningMetricalScheme': 'example_altPatterningMetricalScheme',
                            'altSyllabicMetricalScheme': 'example_altSyllabicMetricalScheme',
                            'employs': 'pattern',
                            'feetType': 'example_feetType',
                            'grammaticalStressPattern': 'example_grammaticalStressPattern',
                            'hasAnacrusis': False,
                            'hasCaesura': False,
                            'hasMetaplasm': True,
                            'initialPhonemesPattern': 'example_initialPhonemesPattern',
                            'initialPhonemesPatternByManner': 'example_initialPhonemesPatternByManner',
                            'isHypermetre': False,
                            'isHypometre': True,
                            'isRegular': True,
                            'lineMaxLength': 6,
                            'lineMinLength': 5,
                            'moraeMetricalScheme': 'example_moraeMetricalScheme',
                            'patterningMetricalScheme': '+--+-',
                            'phonemePattern': 'example_phonemePattern',
                            'phonemePatternByManner': 'example_phonemePatternByManner',
                            'scannedLine': 'GRAN dey re DON da',
                            'syllabicMetricalLength': 5,
                            'vowelTypeScheme': 'example_vowelTypeScheme'
                        },
                        'mentions': [
                            {
                                'content': 'example_content',
                                'type': 'example_type'
                            }
                        ],
                        'metaplasm': [
                            {
                                'affectsFirst': 'example_affectsFirst',
                                'typeOfMetaplasm': 'example_typeOfMetaplasm'
                            }
                        ],
                        'mora': [
                            {
                                'content': 'example_content',
                                'forms': 'example_forms',
                                'moraNumber': 1
                            }
                        ],
                        'phonologicalGroups': [
                            {
                                'content': 'gran',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'dey',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': [
                                    1
                                ],
                                'weight': 'example_weight'
                            },
                            {
                                'content': 're',
                                'isStressed': False,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'don',
                                'isStressed': True,
                                'isWordEnd': False,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            },
                            {
                                'content': 'da',
                                'isStressed': False,
                                'isWordEnd': True,
                                'sinaeresisIndex': None,
                                'synalephaIndex': None,
                                'weight': 'example_weight'
                            }
                        ],
                        'relativeLineNumber': 7,
                        'rhyme': {
                            'ending': '',
                            'endingStressedVowel': None,
                            'finalConsonant': 'x_finalConsonant',
                            'isEcho': False,
                            'prefinalConsonants': 'example_prefinalConsonants',
                            'presentsRhymeMatching': 'example_presentsRhymeMatching',
                            'rhymeGrapheme': '',
                            'rhymeLabel': '-',
                            'rhymePhoneme': 'example_rhymePhoneme',
                            'typeOfRhymeMatching': ''
                        },
                        'secondHemistich': 'example_secondHemistich',
                        'tokenList': [
                            {
                                'content': 'grande',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'gran',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'de',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': True,
                                        'has_synalepha': True,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 1,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'y',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 'y',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 2,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': 'redonda',
                                'lemma': 'example_lemma',
                                'morphologicalAnnotation': 'example_morphologicalAnnotation',
                                'partOfSpeech': 'EX_partOfSpeech',
                                'syllableList': [
                                    {
                                        'coda': 'example_coda',
                                        'content': 're',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': False,
                                        'is_stressed': False,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'don',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': True,
                                        'isWordEnd': False,
                                        'is_stressed': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    },
                                    {
                                        'coda': 'example_coda',
                                        'content': 'da',
                                        'hasSinaeresis': False,
                                        'hasSynalepha': False,
                                        'isStressed': False,
                                        'isWordEnd': True,
                                        'is_stressed': False,
                                        'is_word_end': True,
                                        'nucleus': 'example_nucleus',
                                        'onset': 'example_onset'
                                    }
                                ],
                                'translation': 'example_translation',
                                'type': 'word',
                                'wordNumber': 3,
                                'wordSense': 'example_wordSense'
                            },
                            {
                                'content': '.',
                                'type': 'symbol'
                            }
                        ]
                    }
                ],
                'metricalNotes': 'example_metricalNotes',
                'paraphrasis': 'example_paraphrasis',
                'stanzaNumber': 1,
                'stanzaPattern': {
                    'altRhymeScheme': 'example_altRhymeScheme',
                    'clausulaScheme': 'example_clausulaScheme',
                    'clausulaSchemeType': 'example_clausulaSchemeType',
                    'isStanzaPatternOf': 'example_isStanzaPatternOf',
                    'metricalType': 'septilla',
                    'rhymeDispositionType': '',
                    'rhymeScheme': '----aa-'
                },
                'typeOfStanzaEdition': 'example_typeOfStanzaEdition',
                'typeofStanza': 'example_typeofStanza'
            }
        ],
        'workPattern': {
            'hasRefrain': 'example_hasRefrain',
            'interStrophicRelations': 'example_interStrophicRelations',
            'isIsometric': True,
            'isIsostrophic': False,
            'isUnissonant': True,
            'metricalCategory': 'example_metricalCategory',
            'metricalComplexity': 'example_metricalComplexity',
            'metricalContext': 'example_metricalContext',
            'rhymeTypeProportion': 'example_rhymeTypeProportion',
            'versificationType': 'example_versificationType'
        }
    }
}

snapshots['test_analysis_scansion 1'] = {
    'scansion': [
        [
            {
                'phonological_groups': [
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
                    'length': 2,
                    'stress': '+-',
                    'type': 'pattern'
                },
                'tokens': [
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
                    }
                ],
                'rhythm': {
                    'length': 3,
                    'stress': '-+-',
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
                    }
                ]
            }
        ]
    ]
}

snapshots['test_analysis_scansion_no_structure 1'] = {
    'scansion': [
        [
            {
                'ending': '',
                'ending_stress': 0,
                'phonological_groups': [
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
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 2,
                    'length_range': {
                        'max_length': 2,
                        'min_length': 2
                    },
                    'stress': '+-',
                    'type': 'pattern'
                },
                'structure': 'unknown',
                'tokens': [
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
                'ending': '',
                'ending_stress': 0,
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
                    }
                ],
                'rhyme': '-',
                'rhyme_relaxation': None,
                'rhyme_type': '',
                'rhythm': {
                    'length': 3,
                    'length_range': {
                        'max_length': 3,
                        'min_length': 3
                    },
                    'stress': '-+-',
                    'type': 'pattern'
                },
                'structure': 'unknown',
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
                    }
                ]
            }
        ]
    ]
}

snapshots['test_analysis_scansion_structure 1'] = {
    'scansion': [
        [
            {
                'ending': 'ado',
                'ending_stress': -3,
                'phonological_groups': [
                    {
                        'is_stressed': True,
                        'syllable': 'Pon'
                    },
                    {
                        'has_synalepha': False,
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'go'
                    },
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'syllable': 'un'
                    },
                    {
                        'is_stressed': False,
                        'syllable': 'pa'
                    },
                    {
                        'has_sinaeresis': True,
                        'is_stressed': False,
                        'syllable': 're'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'a'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'do'
                    }
                ],
                'rhyme': 'a',
                'rhyme_relaxation': True,
                'rhyme_type': 'consonant',
                'rhythm': {
                    'length': 7,
                    'length_range': {
                        'max_length': 7,
                        'min_length': 7
                    },
                    'stress': '+-+--+-',
                    'type': 'pattern'
                },
                'structure': 'couplet',
                'tokens': [
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': True,
                                'syllable': 'Pon'
                            },
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'go'
                            }
                        ]
                    },
                    {
                        'stress_position': -1,
                        'word': [
                            {
                                'is_stressed': True,
                                'is_word_end': True,
                                'syllable': 'un'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'pa'
                            },
                            {
                                'has_sinaeresis': True,
                                'is_stressed': False,
                                'syllable': 're'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'a'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'do'
                            }
                        ]
                    }
                ]
            },
            {
                'ending': 'ado',
                'ending_stress': -3,
                'phonological_groups': [
                    {
                        'is_stressed': True,
                        'is_word_end': True,
                        'syllable': 'meha',
                        'synalepha_index': [
                            1
                        ]
                    },
                    {
                        'is_stressed': False,
                        'syllable': 'sa'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'li'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'do'
                    },
                    {
                        'is_stressed': False,
                        'syllable': 'cua'
                    },
                    {
                        'is_stressed': True,
                        'syllable': 'dra'
                    },
                    {
                        'is_stressed': False,
                        'is_word_end': True,
                        'syllable': 'do'
                    }
                ],
                'rhyme': 'a',
                'rhyme_relaxation': True,
                'rhyme_type': 'consonant',
                'rhythm': {
                    'length': 7,
                    'length_range': {
                        'max_length': 8,
                        'min_length': 7
                    },
                    'stress': '+-+--+-',
                    'type': 'pattern'
                },
                'structure': 'couplet',
                'tokens': [
                    {
                        'stress_position': 0,
                        'word': [
                            {
                                'has_synalepha': True,
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'me'
                            }
                        ]
                    },
                    {
                        'stress_position': -1,
                        'word': [
                            {
                                'is_stressed': True,
                                'is_word_end': True,
                                'syllable': 'ha'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'sa'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'li'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'do'
                            }
                        ]
                    },
                    {
                        'stress_position': -2,
                        'word': [
                            {
                                'is_stressed': False,
                                'syllable': 'cua'
                            },
                            {
                                'is_stressed': True,
                                'syllable': 'dra'
                            },
                            {
                                'is_stressed': False,
                                'is_word_end': True,
                                'syllable': 'do'
                            }
                        ]
                    }
                ]
            }
        ]
    ]
}
