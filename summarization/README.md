# Text Summarization

## Usage
1. Collect system provenance using Thoth.
2. Use raw log as edge reduction input to reduce log size.
3. Use natural language format to prepare human-readable log in natural language.
4. Input as GPT prompt

### 2. Edge Reduction
Run `python summarize.py <input>` to remove repeated edges in provenance graph.

### 3. Natural Language Format
Run `python format.py <input>` to convert from JSON to natural language format.

### 4. Prompting
We used the OpenAI Python library and the GPT4-0613 mdoel to create text summaries. 
The prompt includes the instruction in [prompt.txt](https://github.com/nboufford/prov-comprehension-artifacts/blob/main/summarization/prompt.txt) and the provenance log to be summarized.

Instructions for the OpenAI API are [here](https://platform.openai.com/docs/quickstart?context=python).

Below is a code sample with our prompt and messages. An API key is required to access the model.

```
from openai import OpenAI
client = OpenAI()

system_message = "You are a helpful assistant to a data scientist."
prompt = "The following log describes a task performed by a data scientist. Summarize the following log with enough detail that another researcher could reproduce the task. Include the following if applicable: \n-file downloads\n-script executions\n-notebook executions\n-virtual environments\n-localhost connections-\remote connections\n-dataset operations\n-outputs\n-saved models. Be specific with file names and locations. Do not include irrelevant system information such as process IDs or uname commands."

completion = client.chat.completions.create(
  model="gpt-4-0613",
  messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompt + <prov_log>} # read prov log from file as string and add to message
  ]
)

print(completion.choices[0].message)
```

 
