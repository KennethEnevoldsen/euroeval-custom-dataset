# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "openai>=2.16.0",
# ]
# ///
from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.2.15:1234/v1",
    api_key="lm-studio"  # can be anything, not validated
)

response = client.chat.completions.create(
    model="liquid/lfm2-1.2b",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content)