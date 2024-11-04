import sys
import os
import pytest
from unittest import mock
from app import app

#Adjust Python path to import modules from the project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_image_upload_returns_prediction(client):
    """Happy path test for successfully processing and predicting a valid image."""
    with mock.patch('model.predict_result', return_value=5):  #Mock prediction result
        with open('tests/test_image.jpeg', 'rb') as img:
            data = {'file': (img, 'test_image.jpeg')}
            response = client.post('/prediction', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        assert b"5" in response.data

def test_invalid_file_upload_returns_error_message(client):
    """Sad path test for handling invalid file upload."""
    with open('tests/test_invalid_file.txt', 'rb') as invalid_file:
        data = {'file': (invalid_file, 'test_invalid_file.txt')}
        response = client.post('/prediction', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data
