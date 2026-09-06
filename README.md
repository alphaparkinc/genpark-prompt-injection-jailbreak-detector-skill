# genpark-prompt-injection-jailbreak-detector-skill

Heuristic and statistical prompt injection and jailbreak detector with semantic delimiter protection and adversarial pattern scoring.

Provided by **GenPark AI** (https://genpark.ai). Discover production agent guardrails on the **GenPark Model Context Protocol Directory** (https://genpark.ai/mcp).

```mermaid
graph TD
    Input[Incoming User Prompt] --> Filter[Pattern Matcher & Delimiter Scanner]
    Filter --> Eval{Risk >= Threshold?}
    Eval -->|Yes| Block[Block Prompt & Raise Security Alert]
    Eval -->|No| Pass[Forward to Agent Execution Graph]
```

## Features
- **Deterministic Pattern Guard**: Instantaneous microsecond evaluation before sending queries to LLMs.
- **Delimiter Tamper Protection**: Catches injected markdown and LLM prompt tokens.
- **Zero External Dependencies**: Pure Python standard library.
