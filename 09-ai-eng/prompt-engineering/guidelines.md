# Prompting Principles

## Principle 1 — Write Clear and Specific Instructions

### Topic 1 — Use Delimiters

- Use delimiters to clearly separate different parts of the input
    

Examples:

- `""" text """`
    
- HTML tags
    
- Markdown blocks
    

Underlying reality:

- LLMs process all context together as token sequences.
    
- Without clear boundaries, instructions and data can become mixed.
    

Why it matters:

- Clear boundaries improve context control and reduce ambiguity.
    

---

### Topic 2 — Ask for Structured Output

- Ask for outputs in formats such as JSON or HTML
    

Underlying reality:

- LLMs generate probabilistic natural language, while systems require stable structures.
    

Why it matters:

- Structured outputs make AI responses more predictable and machine-readable.
    

---

### Topic 3 — Check Whether Conditions Are Satisfied

- Check assumptions required to complete the task
    

Underlying reality:

- LLMs tend to continue generating responses even when information is incomplete.
    

Why it matters:

- Validation improves reliability and reduces incorrect responses.
    

---

### Topic 4 — Give Successful Examples of Completing Tasks

- Then ask the model to perform the task
    

This is related to few-shot prompting.

Underlying reality:

- LLMs are highly pattern-based systems and learn behavior from context examples.
    

Why it matters:

- Examples guide formatting, reasoning style, and response behavior more effectively than abstract instructions alone.
    

---

## Principle 2 — Give the Model Time to Think

### Topic 1 — Specify the Steps Required to Complete the Task

- Break complex tasks into smaller reasoning steps
    

Underlying reality:

- Multi-step reasoning is more stable when intermediate steps are explicitly represented.
    

Why it matters:

- Step-by-step reasoning improves stability and response quality.
    

---

### Topic 2 — Instruct the Model to Work Out Its Own Solution Before Reaching a Conclusion

- Encourage intermediate reasoning before generating the final answer
    

Underlying reality:

- Immediate generation may skip important reasoning paths.
    

Why it matters:

- Intermediate reasoning improves logical consistency and accuracy.
    

---

# Model Limitations

## Hallucination

- The model may generate responses that sound plausible but are not true
    

Underlying reality:

- LLMs predict statistically likely tokens rather than verified facts.
    

Why it matters:

- Reliability depends on grounding and validation, not generation alone.
    

---

## Reducing Hallucination

- First retrieve relevant information
    
- Then answer based on the retrieved information
    

Underlying reality:

- External information is often more reliable than parametric memory alone.
    

Why it matters:

- Grounded information improves factual accuracy and system reliability.