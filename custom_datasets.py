from euroeval import TEXT_CLASSIFICATION, DatasetConfig
from euroeval.languages import ENGLISH

MY_CONFIG = DatasetConfig(
    name="my-dataset",
    pretty_name="My Dataset",
    source=dict(train="data/train.csv", test="data/test.csv", val="data/val.csv"),
    task=TEXT_CLASSIFICATION,
    languages=[ENGLISH],
    _labels=["yes", "no"],
)
