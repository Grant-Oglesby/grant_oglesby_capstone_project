# Define callable function for ETL pipeline
# Function should retrieve two urls from data/source.txt
# Returns list(strings)
def retrieve_urls():
    urls_to_read = []
    with open("data/source.txt") as f:
        for line in f:
            urls_to_read.append(line.strip())
    return urls_to_read
