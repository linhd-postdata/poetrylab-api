import json
import pytest
from poetrylab_api import app


@pytest.fixture(scope='module')
def client():
    with app.app.test_client() as test_client:
        yield test_client


def test_analysis_enjambment(snapshot, client):
    text = """ami-
go"""
    response = client.post('/analysis?operations=enjambment', data=text)
    assert response.status_code == 200
    snapshot.assert_match(json.loads(response.data))


def test_analysis_scansion(snapshot, client):
    text = """verde
abrigo"""
    response = client.post('/analysis?operations=scansion', data=text)
    assert response.status_code == 200
    snapshot.assert_match(json.loads(response.data))


def test_analysis_enjambment_scansion(snapshot, client):
    text = """Jamás encontraré más fiel ami-
go que en los peores momentos arrime
y no me trae mi verde
abrigo que su cuerpo a mi alma abatida y anime
dándome el calor del mejor abrigo."""
    response = client.post(
        '/analysis?operations=enjambment&operations=scansion', data=text
    )
    assert response.status_code == 200
    snapshot.assert_match(json.loads(response.data))
