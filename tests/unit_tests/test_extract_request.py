from src.extract.extract_request import extract_text


# Test function for correct type
def test_extract_text():
    output = extract_text()
    assert isinstance(output, list)


# Test function for list length over 0
def test_extract_text_length():
    output = extract_text()
    assert len(output) > 0


# Test function for list of type string
def test_extract_text_items():
    output = extract_text()
    assert all(isinstance(item, str) for item in output)


# Test function for non-empty strings
def test_extract_text_non_empty():
    output = extract_text()
    assert all(len(item) > 0 for item in output)
