import numpy as np
import pandas as pd


def create_dataframe():
    """Create a pandas dataframe with 2 columns: ds and value."""
    return pd.DataFrame(
        {
            "ds": pd.date_range(start="2024-01-01", periods=1000),
            "y": np.random.randint(0, 100, size=1000).astype(int),
        }
    )


if __name__ == "__main__":
    df = create_dataframe()
    print(df["y"][0])
