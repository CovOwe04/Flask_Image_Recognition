import sys
import os
# Adjust the Python path to ensure the app module can be imported from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import app  # Import the Flask app instance

# Pytest fixture to set up a test client for the Flask app
@pytest.fixture
def client():
    # The test client simulates HTTP requests to the app
    with app.test_client() as client:
        yield client  # Provides the client to the test functions

def test_homepage(client):
    """Basic test to ensure the homepage loads successfully."""
    # Simulate a GET request to the homepage route
    response = client.get('/')
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200
    # Check that a specific text string is in the response data (to confirm the correct page loaded)
    assert b"Hand Sign Digit Language Detection" in response.data

def test_prediction_route(client):
    """Advanced test to ensure prediction route handles an image upload."""
    # Simulate a POST request to the prediction route with a test image file
    data = {'file': (open('tests/test_image.jpeg', 'rb'), 'test_image.jpeg')}
    response = client.post('/prediction', data=data, content_type='multipart/form-data')
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200
    # Check that the response contains either an error message or prediction result
    assert b"File cannot be processed" in response.data or b"Prediction" in response.data

