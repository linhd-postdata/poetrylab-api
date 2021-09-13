import requests
import unittest
from unittest import mock

from poetrylab_api import app
from poetrylab_api.addons import is_available
from poetrylab_api.addons import perform
from poetrylab_api.settings import ADDONS



@mock.patch('requests.request')
def test_is_avalilable(mocked_request):
    mocked_request.return_value = mock.Mock(status_code=200)
    assert "success" in is_available("entities")


@mock.patch('requests.request')
def test_is_avalilable_different_status(mocked_request):
    mocked_request.return_value = mock.Mock(status_code=400)
    assert "error" in is_available("entities")


@mock.patch('requests.request')
def test_is_avalilable_exception(mocked_request):
    mocked_request.side_effect = requests.exceptions.ConnectionError()
    output = is_available("entities")
    assert "error" in output


def test_is_avalilable_invalid():
    assert "error" in is_available("INVALID")


@mock.patch('requests.request')
def test_perform(mocked_request):
    mock_output = {"entities": ["N"]}
    mocked_request.return_value = mock.Mock(json=lambda: mock_output)
    assert perform("entities", "Random text.") == mock_output


@mock.patch('requests.request')
def test_perform_output(mocked_request):
    addons_ = ADDONS.copy()
    addons_["entities"]["endpoint"]["output"] = "result"
    # Mocking ADDONS in a context manager to avoid leaking its mock
    with mock.patch('poetrylab_api.addons.ADDONS', addons_):
        mock_output = {"result": ["N"]}
        mocked_request.return_value = mock.Mock(json=lambda: mock_output)
        assert perform("entities", "Random text.") == mock_output["result"]


@mock.patch('requests.request')
def test_perform_exception(mocked_request):
    mocked_request.side_effect = requests.exceptions.ConnectionError()
    output = perform("entities", "Random text.")
    assert "error" in output
