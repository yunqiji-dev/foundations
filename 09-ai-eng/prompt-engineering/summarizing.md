# Summarizing

## Core Idea

Summarization is not simply shortening text.

It is a process of controlling:

- focus
    
- relevance
    
- compression
    
- information selection
    

through prompt design.

---

# Basic Summarization

- Generate a short summary of a text
    

Example:

- Summarize a product review
    

Underlying reality:

- LLMs compress information by predicting contextually important patterns.
    

Why it matters:

- Summarization reduces information overload while preserving key meaning.
    

---

# Summarize with a Word / Sentence / Character Limit

- Specify output constraints such as:
    

Examples:

- “In at most 30 words”
    
- “Use one sentence”
    

Underlying reality:

- Output constraints influence how the model compresses information.
    

Why it matters:

- Constraints improve controllability and consistency.
    

---

# Summarize with a Focus on Specific Topics

Examples:

- Shipping and delivery
    
- Price and value
    

Underlying reality:

- Prompts guide the model’s attention toward specific parts of the context.
    

Why it matters:

- Different tasks require different information priorities.
    

---

# Use “Extract” Instead of “Summarize”

- Extract only information relevant to a specific goal
    

Example:

- Extract shipping-related information from a review
    

Underlying reality:

- “Summarize” encourages broad compression.
    
- “Extract” encourages selective retrieval.
    

Why it matters:

- Extraction improves precision and reduces unrelated information.
    

---

# Summarize Multiple Product Reviews

- Summarize multiple reviews individually or collectively
    

Underlying reality:

- LLMs can identify repeated patterns across multiple inputs.
    

Why it matters:

- Multi-input summarization helps detect common themes, trends, and recurring issues.
    

---

# Fundamental Insight

Summarization is fundamentally a process of attention control.

Prompting determines:

```text
what information matters
what information is ignored
what information is compressed
```

---

# Underlying Reality

LLMs do not truly understand importance like humans.

They estimate importance through:

- contextual patterns
    
- token relationships
    
- prompt guidance
    
- attention mechanisms
    

Because of this, different prompts can produce different summaries from the same text.

---

# Why This Matters

Modern AI systems increasingly rely on summarization for:

- information filtering
    
- context compression
    
- retrieval systems
    
- memory systems
    
- workflow efficiency
    

Because LLM context windows are limited, summarization becomes an important mechanism for managing information complexity and preserving relevant context.