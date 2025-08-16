import pandas as pd
from src.extract.extract import extract_data


# Test function for correct type
def test_extract_data():
    output = extract_data()
    assert isinstance(output, list)


# Test function for list length over 0
def test_extract_data_length():
    output = extract_data()
    assert len(output) > 0


# Test function for list of type DataFrame
def test_extract_data_items():
    output = extract_data()
    assert all(isinstance(item, pd.DataFrame) for item in output)


# Test function for non-empty DataFrames
def test_extract_data_non_empty():
    output = extract_data()
    assert all(not item.empty for item in output)


# Test for DataFrame shape
def test_extract_data_shape():
    output = extract_data()
    assert all(item.shape[0] > 0 and item.shape[1] > 0 for item in output)
