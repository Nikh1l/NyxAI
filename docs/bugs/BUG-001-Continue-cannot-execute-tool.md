## Observed
Continue -> Ollama -> Qwen2.5-Coder retrns `{"tool_calls": ...}` as plain text

instead of
`
{
    "message": {
        "tool_calls": [...]
    }
}`

Therefor Continue never invokes the tool call.