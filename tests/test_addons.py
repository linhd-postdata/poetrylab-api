import requests
import unittest
from unittest import mock

from poetrylab_api import app
from poetrylab_api.addons import is_available
from poetrylab_api.addons import perform


@mock.patch('requests.request')
def test_is_avalilable(mocked_request):
    mocked_request.return_value = mock.Mock(status_code=200)
    assert is_available("entities")


@mock.patch('requests.request')
def test_is_avalilable_exception(mocked_request):
    mocked_request.side_effect = requests.exceptions.ConnectionError()
    output = is_available("entities")
    assert "error" in output


def test_is_avalilable_invalid():
    assert not is_available("INVALID")


@mock.patch('requests.request')
def test_perform(mocked_request):
    mock_output = {"entities": ["N"]}
    mocked_request.return_value = mock.Mock(json=lambda: mock_output)
    assert perform("entities", "Random text.") == mock_output


@mock.patch('requests.request')
def test_perform_exception(mocked_request):
    mocked_request.side_effect = requests.exceptions.ConnectionError()
    output = perform("entities", "Random text.")
    assert "error" in output
