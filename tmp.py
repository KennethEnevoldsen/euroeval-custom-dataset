# /// script
# requires-python = "==3.12"
# dependencies = [
#     "euroeval[generative]>=16.11.1",
#     "vllm-metal",
#     "vllm==0.11.0",
#     "transformers>=4.56,<5",
# ]
# ///


from vllm import LLM, SamplingParams

if __name__ == "__main__":
    print("import works with vllm!")

    llm = LLM(model="PleIAs/Monad")
    # Generate a simple prompt to test
    params = SamplingParams(max_tokens=5)
    response = llm.generate(["Hello, world!"], sampling_params=params)
    for r in response:
        print(r)

    print("Generation works with vllm!")

    from euroeval import Benchmarker

    benchmarker = Benchmarker()
    benchmarker.benchmark(
        model="openai-community/gpt2", task="sentiment-classification", language="da"
    )
