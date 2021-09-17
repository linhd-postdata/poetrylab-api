from contextlib import ExitStack
from unittest import mock

import pytest

from poetrylab_api import app
from poetrylab_api.core import analyze
from poetrylab_api.core import get_analysis
from poetrylab_api.core import get_traceback


@pytest.fixture(scope='module')
def poem():
    return bytes("""Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo.""", 'utf-8')


@pytest.fixture(scope='module')
def poem_2():
    return bytes("""Pongo un pareado
me ha salido cuadrado""", 'utf-8')


@pytest.fixture(scope='module')
def poem_3():
    return bytes("""La cebolla es 
cerrada y pobre:
escarcha de tus días
y de mis noches.
Hambre y 
hielo negro y 
grande y redonda.""", 'utf-8')


def test_analyze_scansion(snapshot, poem):
    operations = ["scansion"]
    output = analyze(poem.decode("utf8"), operations)
    snapshot.assert_match(output)


def test_analyze_scansion_structure(snapshot, poem_2):
    operations = ["scansion"]
    rhyme_analysis = True
    output = analyze(poem_2.decode("utf8"), operations, rhyme_analysis)
    snapshot.assert_match(output)


def test_analyze_scansion_structure_alternative_output(snapshot, poem_2):
    operations = ["scansion"]
    rhyme_analysis = True
    alternative_output = True
    output = analyze(poem_2.decode("utf8"), operations, rhyme_analysis, alternative_output)
    snapshot.assert_match(output)


def test_analyze_enjambment(snapshot, poem):
    operations = ["enjambment"]
    output = analyze(poem.decode("utf8"), operations)
    snapshot.assert_match(output)


def test_analyze_enjambment_scansion(snapshot, poem):
    operations = ["enjambment", "scansion"]
    output = analyze(poem.decode("utf8"), operations)
    snapshot.assert_match(output)


def test_analyze_enjambment_scansion_structure(snapshot, poem_3):
    operations = ["enjambment", "scansion"]
    rhyme_analysis = True
    output = analyze(poem_3.decode("utf8"), operations, rhyme_analysis)
    snapshot.assert_match(output)


def test_analyze_addon(snapshot, poem):
    module = "poetrylab_api.core"
    is_available = {"success": True}
    perform = {"entities": []}
    operations = ["entities"]
    with ExitStack() as stack:
        managers = (
            mock.patch(f"{module}.is_available", return_value=is_available),
            mock.patch(f"{module}.perform", return_value=perform),
        )
        [stack.enter_context(manager) for manager in managers]
        output = analyze(poem.decode("utf8"), operations)
        assert output["entities"] == perform


def test_analyze_unavailable_addon(snapshot, poem):
    module = "poetrylab_api.core"
    is_available = {"error": True}
    perform = {"entities": []}
    operations = ["entities"]
    with ExitStack() as stack:
        managers = (
            mock.patch(f"{module}.is_available", return_value=is_available),
            mock.patch(f"{module}.perform", return_value=perform),
        )
        [stack.enter_context(manager) for manager in managers]
        output = analyze(poem.decode("utf8"), operations)
        assert "error" in output["entities"]


def test_get_analysis_scansion(snapshot, poem):
    with app.app.test_request_context('/analysis'):
        operations = ["scansion"]
        output = get_analysis(poem, operations)
        snapshot.assert_match(output)


def test_get_analysis_scansion_structure(snapshot, poem_2):
    with app.app.test_request_context('/analysis'):
        operations = ["scansion"]
        rhyme_analysis = True
        output = get_analysis(poem_2, operations, rhyme_analysis)
        snapshot.assert_match(output)


def test_get_analysis_enjambment(snapshot, poem):
    with app.app.test_request_context('/analysis'):
        operations = ["enjambment"]
        output = get_analysis(poem, operations)
        snapshot.assert_match(output)


def test_get_analysis_enjambment_scansion(snapshot, poem):
    with app.app.test_request_context('/analysis'):
        operations = ["enjambment", "scansion"]
        output = get_analysis(poem, operations)
        snapshot.assert_match(output)


def test_get_analysis_enjambment_scansion_structure(snapshot, poem_3):
    with app.app.test_request_context('/analysis'):
        operations = ["enjambment", "scansion"]
        rhyme_analysis = True
        output = get_analysis(poem_3, operations, rhyme_analysis)
        snapshot.assert_match(output)


def test_get_traceback():

    def raise_value_error(*args):
        raise ValueError("Error raised")

    output = get_traceback(raise_value_error, None)
    assert output["error"] == 'ValueError'
    assert output["message"] == 'Error raised'


def test_get_analysis_addon(snapshot, poem):
    module = "poetrylab_api.core"
    is_available = {"success": True}
    perform = {"entities": []}
    operations = ["entities"]
    with ExitStack() as stack:
        managers = (
            mock.patch(f"{module}.is_available", return_value=is_available),
            mock.patch(f"{module}.perform", return_value=perform),
            app.app.test_request_context('/analysis')
        )
        [stack.enter_context(manager) for manager in managers]
        output = get_analysis(poem, operations)
        snapshot.assert_match(output)


def test_get_analysis_unavailable_addon(snapshot, poem):
    module = "poetrylab_api.core"
    is_available = {"error": True}
    perform = {"entities": []}
    operations = ["entities"]
    with ExitStack() as stack:
        managers = (
            mock.patch(f"{module}.is_available", return_value=is_available),
            mock.patch(f"{module}.perform", return_value=perform),
            app.app.test_request_context('/analysis')
        )
        [stack.enter_context(manager) for manager in managers]
        output = get_analysis(poem, operations)
        snapshot.assert_match(output)
