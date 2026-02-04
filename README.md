# Running Euroeval on a custom dataset

Below we check a variety of cases for evaluation.

## Classification using a csv and the CLI

```bash
# using models - untested
uv run euroeval --dataset my-dataset --model openai-community/gpt2
uv run euroeval --dataset my-dataset --model PleIAs/Monad
```

```bash
# using a (local) API, e.g. LM Studio
uv run euroeval --dataset my-dataset --model my-model --api-base http://localhost:1234
```


## Classification using a csv and a Script

```bash
uv run classification_from_script.py
```