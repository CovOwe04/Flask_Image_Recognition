import sys
import os
# Adjust the Python path to ensure the model module can be imported from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import numpy as np
from model import preprocess_img, predict_result  # Import functions to be tested

def test_preprocess_img():
    """Basic test to ensure preprocessing returns the correct shape."""
    # Path to the test image used in preprocessing tests
    img_path = 'tests/test_image.jpeg'
    # Preprocess the image and check that the output shape matches expected dimensions
    processed_img = preprocess_img(img_path)
    assert processed_img.shape == (1, 224, 224, 3)

def test_predict_result():
    """Advanced test to ensure predict_result outputs a valid class index."""
    # Create a dummy input image with expected shape for testing prediction
    dummy_input = np.zeros((1, 224, 224, 3))
    # Run the prediction function and check that the output is a valid class index
    prediction = predict_result(dummy_input)
    # Assert the prediction is an integer type (either int or numpy integer)
    assert isinstance(prediction, (int, np.integer))
    # Confirm the prediction is within the expected class range (0-9)
    assert 0 <= prediction <= 9

