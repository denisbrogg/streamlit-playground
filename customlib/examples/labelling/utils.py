from typing import List
import pandas as pd
import numpy as np

def get_fake_timeseries(n: int=10) -> pd.DataFrame:
    data_vectors: List[np.ndarray] = [np.sin(np.arange(0, 100, 0.1)) * np.random.random(1000) for i in range(n)]
    time_vectors: List[np.ndarray] = [np.arange(0, 100, 0.1) for i in range(n)]
    index: List[int] = list(range(n))

    df = pd.DataFrame([{"DATA": d, "TIME": t} for d, t in zip(data_vectors, time_vectors)], index=index)

    return df