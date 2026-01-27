from euroeval import Benchmarker

from .custom_datasets import MY_CONFIG

benchmarker = Benchmarker()
benchmarker.benchmark(model="openai-community/gpt2", dataset=MY_CONFIG)
