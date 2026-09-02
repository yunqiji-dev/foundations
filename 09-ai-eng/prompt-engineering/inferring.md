# Inferring

## Core Idea

Inferring is the process of deriving information or conclusions from text based on a specific task.

Unlike summarization, which focuses on compressing information, inference focuses on identifying or determining specific information from the given context.

---

# Classification

- Determine sentiment such as positive or negative
- Identify specific emotions
- Determine whether a particular emotion or attribute is present

Underlying reality:

- LLMs can infer semantic attributes from patterns and relationships within the text, even when the information is not explicitly stated as a label.

Why it matters:

- Classification turns unstructured language into defined categories that can be processed by a system.

---

# Information Extraction

- Extract specific information from text
- Identify entities such as products and companies
- Return the result in a defined structure such as JSON
- Use a default value such as `unknown` when information is missing

Underlying reality:

- LLMs can map information expressed in natural language to predefined fields.

Why it matters:

- Extraction converts unstructured language into structured data that can be used by other parts of a system.

---

# Multiple Tasks

- Perform multiple related inference tasks on the same text
- Return the results in a structured format

Underlying reality:

- The same context can contain information relevant to multiple inference tasks.

Why it matters:

- Related tasks can sometimes be combined into a single model interaction, reducing repeated processing and producing a unified result.

---

# Topic Inference

- Identify the main topics discussed in a text
- Determine whether specific topics are present

Underlying reality:

- LLMs can identify higher-level patterns and concepts across a larger piece of text.

Why it matters:

- Topic inference can turn unstructured text into categories that can be used for organization, filtering, or routing.

---

# Fundamental Insight

Inference is not simply asking an LLM to understand text.

It is defining what information should be derived from the context.

The same text can therefore produce different results depending on the task:

```text
same text
→ different task
→ different inference
````

---

# Underlying Reality

LLMs can transform unstructured language into task-specific information through contextual pattern recognition.

This allows the same model to perform different kinds of inference, such as:

```text
text
→ classification
→ extraction
→ topic identification
```

---

# Why This Matters

Inference provides a bridge between natural language and structured system behavior.

```text
unstructured language
→ inferred information
→ structured data
→ downstream action
```

This makes LLMs useful not only for generating text, but also for interpreting information that other parts of a system can use.