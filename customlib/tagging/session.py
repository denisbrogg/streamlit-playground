class TaggingSession:
    def __init__(self) -> None:
        self.tags = ["right", "wrong", "dk", "bad"]
        self.tag_counts: dict = { k: 0 for k in self.tags }

    def inc_tags(self, field: str) -> None:
        self.tag_counts[field] += 1

    def sum_tags(self) -> int:
        return sum([v for k, v in self.tag_counts.items()])