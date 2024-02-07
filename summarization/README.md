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
TODO
