import functions_fe
import numpy as np
import pandas as pd
import pytest


def test_create_dataframe():
    df = functions_fe.create_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ["ds", "y"]
    assert df.shape == (1000, 2)
    assert isinstance(df["ds"][0], pd.Timestamp)
    assert isinstance(df["y"][0], np.int64)


if __name__ == "__main__":
    pytest.main()
