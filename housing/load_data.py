import pandas as pd
import os

def load_housing_data(housing_path):
    """
    load data from the given path
    input:
              path: path to where the data is stored
    output:
              df: pandas dataframe of the data
    """
    csv_path = os.path.join(housing_path, "housing.csv")
    df = pd.read_csv(csv_path)
    return df

if __name__=="__main__":
    HOUSING_PATH = os.path.join("datasets", "housing")
    load_housing_data(HOUSING_PATH)