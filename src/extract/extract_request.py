import requests
import os
from src.extract.read_source import retrieve_urls


def extract_text():
    # Retrieve list of urls for data sources and store in list
    urls = retrieve_urls()
    extract_list = []

    # Iterate through list and store each requests.get.text in data/extract
    for i in range(len(urls)):
        # Check if data already downloaded and skip file saving if exists
        file_exists = os.path.exists(f"data/extract/data{i}.csv")
        # TESTING WHEN USING EXISTING FILES WILL NOT COVER LINES 19-22
        # TESTING RESULT WITH EXISTING FILES: 76%
        # TESTING RESULT WITHOUT EXISTING FILES: 100%
        if not file_exists:
            request = requests.get(urls[i])
            request.status_code
            data = request.text
            extract_list.append(data)
        else:
            with open(f"data/raw/data{i}.csv", "r") as file:
                data = file.read()
                extract_list.append(data)
    # Return list of raw text to be used in transform phase
    return extract_list
