import pandas as pd
from typing import List, Dict, Union
from sqlalchemy import create_engine  # For future DB connections

class DataIntegrator:
    def __init__(self, sources: List[Union[str, Dict[str, str]]]):
        """
        Initialize with paths to data sources or DB connections.

        :param sources: List of file paths or DB connection details.
        """
        self.sources = sources

    def load_data(self) -> pd.DataFrame:
        """
        Load data from specified sources. Supports CSV and database connections.

        :return: Combined DataFrame.
        """
        dataframes = []
        for source in self.sources:
            if isinstance(source, str) and source.endswith('.csv'):
                df = pd.read_csv(source)
            else:
                engine = create_engine(source['connection_string'])
                df = pd.read_sql(source['table'], con=engine)
            dataframes.append(df)
        return pd.concat(dataframes, ignore_index=True)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df.drop_duplicates(inplace=True)
        df.dropna(subset=['required_column'], inplace=True)
        return df

    def transform_data(self, df: pd.DataFrame) -> List[Dict[str, Any]]:
        df = df.rename(columns={"OldColumnName": "NewColumnName"})
        return df.to_dict(orient="records")
