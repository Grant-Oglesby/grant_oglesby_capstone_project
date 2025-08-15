import requests
import os
from src.extract.read_source import retrieve_urls


def extract_text():
    # Retrieve list of urls for data sources
    urls = retrieve_urls()
    extract_list = []

    # Iterate through list and store each requests.get.text in data/extract
    for i in range(len(urls)):
        # CHECK IF DATA ALREADY DOWNLOADED AND SKIP FILE SAVING IS EXISTS
        file_exists = os.path.exists(f"data/extract/data{i}.csv")
        if not file_exists:
            request = requests.get(urls[i])
            request.status_code
            data = request.text
            extract_list.append(data)
        else:
            with open(f"data/extract/data{i}.csv", "r") as file:
                data = file.read()
                extract_list.append(data)
    return extract_list
