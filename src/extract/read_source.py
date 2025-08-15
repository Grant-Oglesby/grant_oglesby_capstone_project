# Set import requirements


# Global variable to hold urls from function
urls_to_read = []


# Define callable function for ETL pipeline
# Function should retrieve two urls from data/source.txt
# Returns list(strings)
def retrieve_urls():
    with open("data/source.txt") as f:
        for line in f:
            urls_to_read.append(line.strip())
    return urls_to_read
