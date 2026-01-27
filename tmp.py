# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "euroeval[generative]>=16.11.0",
# ]
# ///

"""
Run using:
uv run tmpy.py
"""

from euroeval import Benchmarker

benchmarker = Benchmarker()
benchmarker.benchmark(
    model="openai-community/gpt2", task="sentiment-classification", language="da"
)
