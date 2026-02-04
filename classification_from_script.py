from euroeval import Benchmarker

from custom_datasets import MY_CONFIG

benchmarker = Benchmarker()
benchmarker.benchmark(
    model="liquid/lfm2-1.2b",
    api_base="http://192.168.2.15:1234/v1",
    dataset=MY_CONFIG,
    few_shot=False,
    num_iterations=1,
)
