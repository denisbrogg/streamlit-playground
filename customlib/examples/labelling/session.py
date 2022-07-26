from typing import Union
import pandas as pd

class LabellingSession:

    def __init__(self, df: pd.DataFrame) -> None:

         # Labels

        self.labels = ["yes", "no", "dk"]
        self.labels_record = []

        # Stats

        self.label_counts: dict = { k: 0 for k in self.labels }

        # Data

        self.df = df
        self.df_iterator = self.df.iterrows()
        self.current_obs_index = None

       

    def inc_labels(self, field: str) -> None:
        self.label_counts[field] += 1
        self.labels_record.append((self.current_obs_index, field))

    def sum_labels(self) -> int:
        return sum([v for k, v in self.label_counts.items()])

    def n_obs(self) -> int:
        return len(self.df)

    def get_next_obs(self) -> Union[None, pd.Series]:
        try:
            idx, obs = next(self.df_iterator)
            self.current_obs_index = idx
            return obs
        except StopIteration:
            print("No more data label!")
            return None

    def get_session_labels(self) -> pd.DataFrame:
        df_labels = pd.DataFrame([{"idx": idx, "label": label} for idx, label in self.labels_record])
        return df_labels