import requests
from src.extract.read_source import retrieve_urls


# Global variable to hold pandas dataframes
extract_list = []


def extract_text():
    # Retrieve list of urls for data sources
    urls = retrieve_urls()
    # Iterate through list and store each requests.get.text in data/extract
    for i in range(len(urls)):
        try:
            request = requests.get(urls[i])
            data = request.text
            extract_list.append(data)
        except Exception as e:
            print(f"Failed: {e}")
    return extract_list
