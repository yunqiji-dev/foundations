# folder-rules
---

**Author:** Yunqi Ji  
**Role:** First-year CS student building the habits and structure of an engineer  
**Version:** 1.0  
**Last Updated:** 2026-01-04  

This document defines the **physical constraints** and **operational protocols** of the Foundations repository. It ensures the file system remains a "High-Performance Brain" rather than a cluttered archive.

---
## 1. Numerical Prefixing (The 00-99 Protocol)

- **Global Hierarchy**: All top-level folders use two-digit prefixes to represent the **abstraction layers** of engineering, moving from meta-cognition (00) to advanced integration (09).
    
- **Local Sequence**: Leaf files use two-digit prefixes to define the logical dependency of concepts within a module (e.g., understanding memory must precede advanced concurrency).
    
- **Alignment**: Numbering ensures the file tree remains sorted by technical logic rather than arbitrary alphabetical order.
    

---

## 2. Naming Constraints (Short-ID Rule)

- **Minimalism**: Use the shortest unique identifier possible to ensure rapid navigation.
    
    - _Correct:_ `01-dsa`, `02-theory`
        
    - _Incorrect:_ `01-data-structures-and-algorithms`, `02-computation-theory`
        
- **Case & Delimiters**: Strict **all-lowercase** and **hyphens** (`-`). No spaces or underscores are permitted.
    
- **Goal**: Optimized for Obsidian’s `Ctrl+O` Quick Switcher—minimal keystrokes for zero-latency retrieval.
    

---

## 3. Structural Integrity

- **Flat Depth Policy**: Maximum **one level** of sub-directories. Deeply nested folders are prohibited to prevent "navigation friction."
    
- **Root Discipline**: The root directory is a protected zone. No files are permitted except for `README.md`.
    
- **Frozen Modules**: As specified in the system design, the structure of `03-systems` is **locked** to maintain cross-module reference integrity.
    

---

## 4. Markdown Anatomy

- **H1-Filename Sync**: The first H1 header must match the short-id filename (e.g., `# folder-rules`).
    
- **Metadata Block**: Every file must start with the standardized header (Author, Role, Version, Date).
    
- **Scan-ability**: Use horizontal rules (`---`) to separate sections and blockquotes (`>`) to highlight non-negotiable principles.
    

---

## 5. Knowledge Flow & Offloading

- **Logic over Implementation**: This repo is for **ideas and mental models**. All actual experiments and code must be offloaded to the `ai-backend-labs` repository.
    
- **Atomic Linking**: Connect modules using Wiki-links `[[ ]]`. If a note becomes too large, refactor it into smaller, atomic components.
    
- **Stability**: Refactor the file structure only when the underlying logic of the technical stack changes.
    

---

## 6. Core Principles

1. **Consistency over Complexity**: A rigid, simple rule is superior to a flexible, complex one.
    
2. **Predictable Location**: You must know where a file belongs before you open the sidebar.
    
3. **Zero-Thought Retrieval**: Filenames must be short enough to be typed from muscle memory.
    
4. **Professionalism**: Treat the repository as a high-stakes engineering product, not a casual notepad.
    

---

_This document serves as the operational constitution for the Foundations repository._