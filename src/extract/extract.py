import pandas as pd
import io
from src.extract.extract_request import extract_text


# Function to call and complete Extract process
def extract_data():
    df_list = []
    # Function to process requests.get and store raw data in data/extract
    data = extract_text()

    for i in range(len(data)):
        df = pd.read_csv(io.StringIO(data[i]), header=0)
        df_list.append(df)
        df.to_csv(f"data/extract/data{i}.csv")

    return df_list
