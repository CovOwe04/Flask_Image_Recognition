import sys
import os
import pytest
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Helper Function for File Upload
def upload_file(client, file_path, file_name):
    """
    Simulate user file upload to the prediction endpoint.
    """
    with open(file_path, 'rb') as file:
        data = {'file': (file, file_name)}
        return client.post('/prediction', data=data, content_type='multipart/form-data')

# Acceptance Test 1: Valid Image Prediction
def test_valid_image_prediction(client):
    """
    Test Name: Valid Image Prediction
    Given: The user uploads a valid image of a hand sign digit.
    When: The system processes the image.
    Then: It should return a prediction representing the recognized digit.
    """
    # Given
    file_path = 'tests/test_image.jpeg'
    file_name = 'test_image.jpeg'

    # When
    response = upload_file(client, file_path, file_name)

    # Then
    assert response.status_code == 200
    assert b"Prediction" in response.data

# Acceptance Test 2: Invalid File Handling
def test_invalid_file_handling(client):
    """
    Test Name: Invalid File Handling
    Given: The user uploads a file that is not an image.
    When: The system processes the file.
    Then: It should return an error message indicating the file cannot be processed.
    """
    # Given
    file_path = 'tests/test_invalid_file.txt'
    file_name = 'test_invalid_file.txt'

    # When
    response = upload_file(client, file_path, file_name)

    # Then
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data

# Acceptance Test 3: Accurate Prediction for Specific Image
def test_prediction_accuracy(client):
    """
    Test Name: Accurate Prediction for Valid Image
    Given: The user uploads an image of a specific hand sign ('2').
    When: The system processes the image.
    Then: It should correctly predict the digit as '2'.
    """
    # Given
    file_path = 'tests/Sign2.jpeg' 
    file_name = 'Sign2.jpeg'

    # When
    response = upload_file(client, file_path, file_name)
    assert response.status_code == 200

    # Then
    soup = BeautifulSoup(response.data, 'html.parser')  # Parse the HTML response
    prediction_text = soup.find('h2').text.strip()  # Extract the prediction text
    assert prediction_text == "2"  # Ensure the prediction matches the expected digit

