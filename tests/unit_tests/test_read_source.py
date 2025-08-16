from src.extract.read_source import retrieve_urls


# Test return type
def test_return_type():
    test_urls = retrieve_urls()
    assert isinstance(test_urls, list)


# Test return list of type string
def test_return_list_of_strings():
    test_urls = retrieve_urls()
    assert all(isinstance(url, str) for url in test_urls)


# Test return correct number of items
def test_return_number_of_items():
    test_urls = retrieve_urls()
    assert len(test_urls) == 2


# Test function for expected return
def test_retrieve_urls():
    test_urls = retrieve_urls()
    url_prefix = "https://nyc3.digitaloceanspaces.com/owid-public/data/"
    mocked_urls = [
        f"{url_prefix}co2/owid-co2-data.csv",
        f"{url_prefix}energy/owid-energy-data.csv"
    ]

    assert test_urls == mocked_urls
