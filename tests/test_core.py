from poetrylab_api import get_analysis


def test_get_analysis_scansion():
    operations = ["scansion"]
    poem = bytes("""Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo.""", 'utf-8')
    output = get_analysis(poem, operations)
    assert output == {'scansion': [{'tokens': [
        {'word': [{'syllable': 'Ja', 'is_stressed': False}, {'syllable': 'más', 'is_stressed': True}],
         'stress_position': -1}, {
            'word': [{'syllable': 'en', 'is_stressed': False}, {'syllable': 'con', 'is_stressed': False},
                     {'syllable': 'tra', 'is_stressed': False}, {'syllable': 'ré', 'is_stressed': True}],
            'stress_position': -1}, {'word': [{'syllable': 'más', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'fiel', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'a', 'is_stressed': True}, {'syllable': 'mi', 'is_stressed': False}],
         'stress_position': -2}, {'symbol': '-'}]}, {'tokens': [
        {'word': [{'syllable': 'go', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'que', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': 0},
        {'word': [{'syllable': 'en', 'is_stressed': False}], 'stress_position': 0},
        {'word': [{'syllable': 'los', 'is_stressed': False}], 'stress_position': 0}, {
            'word': [{'syllable': 'pe', 'is_stressed': False, 'has_sinaeresis': True},
                     {'syllable': 'o', 'is_stressed': True}, {'syllable': 'res', 'is_stressed': False}],
            'stress_position': -2}, {
            'word': [{'syllable': 'mo', 'is_stressed': False}, {'syllable': 'men', 'is_stressed': True},
                     {'syllable': 'tos', 'is_stressed': False}], 'stress_position': -2}, {
            'word': [{'syllable': 'a', 'is_stressed': False}, {'syllable': 'rri', 'is_stressed': True},
                     {'syllable': 'me', 'is_stressed': False}], 'stress_position': -2}]}, {'tokens': [
        {'word': [{'syllable': 'y', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'no', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'me', 'is_stressed': False}], 'stress_position': 0}, {
            'word': [{'syllable': 'tra', 'is_stressed': True, 'has_sinaeresis': True},
                     {'syllable': 'e', 'is_stressed': False}], 'stress_position': -2},
        {'word': [{'syllable': 'mi', 'is_stressed': False}], 'stress_position': 0},
        {'word': [{'syllable': 'ver', 'is_stressed': True}, {'syllable': 'de', 'is_stressed': False}],
         'stress_position': -2}]}, {'tokens': [{'word': [{'syllable': 'a', 'is_stressed': False},
                                                         {'syllable': 'bri', 'is_stressed': True},
                                                         {'syllable': 'go', 'is_stressed': False}],
                                                'stress_position': -2},
                                               {'word': [{'syllable': 'que', 'is_stressed': False}],
                                                'stress_position': 0},
                                               {'word': [{'syllable': 'su', 'is_stressed': False}],
                                                'stress_position': 0}, {
                                                   'word': [{'syllable': 'cuer', 'is_stressed': True},
                                                            {'syllable': 'po', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2},
                                               {'word': [{'syllable': 'a', 'is_stressed': False}],
                                                'stress_position': 0}, {'word': [
            {'syllable': 'mi', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': 0}, {
                                                   'word': [{'syllable': 'al', 'is_stressed': True},
                                                            {'syllable': 'ma', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2}, {
                                                   'word': [{'syllable': 'a', 'is_stressed': False},
                                                            {'syllable': 'ba', 'is_stressed': False},
                                                            {'syllable': 'ti', 'is_stressed': True},
                                                            {'syllable': 'da', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2},
                                               {'word': [{'syllable': 'y', 'is_stressed': True, 'has_synalepha': True}],
                                                'stress_position': -1}, {
                                                   'word': [{'syllable': 'a', 'is_stressed': False},
                                                            {'syllable': 'ni', 'is_stressed': True},
                                                            {'syllable': 'me', 'is_stressed': False}],
                                                   'stress_position': -2}]}, {'tokens': [{'word': [
        {'syllable': 'dán', 'is_stressed': True}, {'syllable': 'do', 'is_stressed': False},
        {'syllable': 'me', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': -3}, {'word': [
        {'syllable': 'el', 'is_stressed': False}], 'stress_position': 0}, {'word': [
        {'syllable': 'ca', 'is_stressed': False}, {'syllable': 'lor', 'is_stressed': True}], 'stress_position': -1}, {
                                                                                             'word': [
                                                                                                 {'syllable': 'del',
                                                                                                  'is_stressed': False}],
                                                                                             'stress_position': 0}, {
                                                                                             'word': [{'syllable': 'me',
                                                                                                       'is_stressed': False},
                                                                                                      {
                                                                                                          'syllable': 'jor',
                                                                                                          'is_stressed': True}],
                                                                                             'stress_position': -1}, {
                                                                                             'word': [{'syllable': 'a',
                                                                                                       'is_stressed': False},
                                                                                                      {
                                                                                                          'syllable': 'bri',
                                                                                                          'is_stressed': True},
                                                                                                      {'syllable': 'go',
                                                                                                       'is_stressed': False}],
                                                                                             'stress_position': -2},
                                                                                         {'symbol': '.'}]}]}



def test_get_analysis_enjambment():
    operations = ["enjambment"]
    poem = bytes("""Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo.""", 'utf-8')
    output = get_analysis(poem, operations)
    assert output == {
        'enjambment': {0: {'type': 'tmesis', 'on': ['ami', 'go']}, 2: {'type': 'sirrematic', 'on': ['ADJ', 'NOUN']}}}



def test_get_analysis_enjambment_scansion():
    operations = ["enjambment", "scansion"]
    poem = bytes("""Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo.""", 'utf-8')
    output = get_analysis(poem, operations)
    assert output == {'scansion': [{'tokens': [
        {'word': [{'syllable': 'Ja', 'is_stressed': False}, {'syllable': 'más', 'is_stressed': True}],
         'stress_position': -1}, {
            'word': [{'syllable': 'en', 'is_stressed': False}, {'syllable': 'con', 'is_stressed': False},
                     {'syllable': 'tra', 'is_stressed': False}, {'syllable': 'ré', 'is_stressed': True}],
            'stress_position': -1}, {'word': [{'syllable': 'más', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'fiel', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'a', 'is_stressed': True}, {'syllable': 'mi', 'is_stressed': False}],
         'stress_position': -2}, {'symbol': '-'}]}, {'tokens': [
        {'word': [{'syllable': 'go', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'que', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': 0},
        {'word': [{'syllable': 'en', 'is_stressed': False}], 'stress_position': 0},
        {'word': [{'syllable': 'los', 'is_stressed': False}], 'stress_position': 0}, {
            'word': [{'syllable': 'pe', 'is_stressed': False, 'has_sinaeresis': True},
                     {'syllable': 'o', 'is_stressed': True}, {'syllable': 'res', 'is_stressed': False}],
            'stress_position': -2}, {
            'word': [{'syllable': 'mo', 'is_stressed': False}, {'syllable': 'men', 'is_stressed': True},
                     {'syllable': 'tos', 'is_stressed': False}], 'stress_position': -2}, {
            'word': [{'syllable': 'a', 'is_stressed': False}, {'syllable': 'rri', 'is_stressed': True},
                     {'syllable': 'me', 'is_stressed': False}], 'stress_position': -2}]}, {'tokens': [
        {'word': [{'syllable': 'y', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'no', 'is_stressed': True}], 'stress_position': -1},
        {'word': [{'syllable': 'me', 'is_stressed': False}], 'stress_position': 0}, {
            'word': [{'syllable': 'tra', 'is_stressed': True, 'has_sinaeresis': True},
                     {'syllable': 'e', 'is_stressed': False}], 'stress_position': -2},
        {'word': [{'syllable': 'mi', 'is_stressed': False}], 'stress_position': 0},
        {'word': [{'syllable': 'ver', 'is_stressed': True}, {'syllable': 'de', 'is_stressed': False}],
         'stress_position': -2}]}, {'tokens': [{'word': [{'syllable': 'a', 'is_stressed': False},
                                                         {'syllable': 'bri', 'is_stressed': True},
                                                         {'syllable': 'go', 'is_stressed': False}],
                                                'stress_position': -2},
                                               {'word': [{'syllable': 'que', 'is_stressed': False}],
                                                'stress_position': 0},
                                               {'word': [{'syllable': 'su', 'is_stressed': False}],
                                                'stress_position': 0}, {
                                                   'word': [{'syllable': 'cuer', 'is_stressed': True},
                                                            {'syllable': 'po', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2},
                                               {'word': [{'syllable': 'a', 'is_stressed': False}],
                                                'stress_position': 0}, {'word': [
            {'syllable': 'mi', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': 0}, {
                                                   'word': [{'syllable': 'al', 'is_stressed': True},
                                                            {'syllable': 'ma', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2}, {
                                                   'word': [{'syllable': 'a', 'is_stressed': False},
                                                            {'syllable': 'ba', 'is_stressed': False},
                                                            {'syllable': 'ti', 'is_stressed': True},
                                                            {'syllable': 'da', 'is_stressed': False,
                                                             'has_synalepha': True}], 'stress_position': -2},
                                               {'word': [{'syllable': 'y', 'is_stressed': True, 'has_synalepha': True}],
                                                'stress_position': -1}, {
                                                   'word': [{'syllable': 'a', 'is_stressed': False},
                                                            {'syllable': 'ni', 'is_stressed': True},
                                                            {'syllable': 'me', 'is_stressed': False}],
                                                   'stress_position': -2}]}, {'tokens': [{'word': [
        {'syllable': 'dán', 'is_stressed': True}, {'syllable': 'do', 'is_stressed': False},
        {'syllable': 'me', 'is_stressed': False, 'has_synalepha': True}], 'stress_position': -3}, {'word': [
        {'syllable': 'el', 'is_stressed': False}], 'stress_position': 0}, {'word': [
        {'syllable': 'ca', 'is_stressed': False}, {'syllable': 'lor', 'is_stressed': True}], 'stress_position': -1}, {
                                                                                             'word': [
                                                                                                 {'syllable': 'del',
                                                                                                  'is_stressed': False}],
                                                                                             'stress_position': 0}, {
                                                                                             'word': [{'syllable': 'me',
                                                                                                       'is_stressed': False},
                                                                                                      {
                                                                                                          'syllable': 'jor',
                                                                                                          'is_stressed': True}],
                                                                                             'stress_position': -1}, {
                                                                                             'word': [{'syllable': 'a',
                                                                                                       'is_stressed': False},
                                                                                                      {
                                                                                                          'syllable': 'bri',
                                                                                                          'is_stressed': True},
                                                                                                      {'syllable': 'go',
                                                                                                       'is_stressed': False}],
                                                                                             'stress_position': -2},
                                                                                         {'symbol': '.'}]}],
                      'enjambment': {0: {'type': 'tmesis', 'on': ['ami', 'go']},
                                     2: {'type': 'sirrematic', 'on': ['ADJ', 'NOUN']}}}
