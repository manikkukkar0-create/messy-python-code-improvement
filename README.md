# Messy Python Code Improvement (Using AI)

This repository demonstrates the process of refactoring unoptimized, monolithic Python scripts into clean, maintainable, and modular Python code adhering to modern standards and PEP 8 best practices.

**Author:** Manik Kukkar  
**Degree:** B.Tech Computer Science and Engineering  
**University:** JECRC University, Jaipur  

---

## Refactoring Overview

### Identified Code Smells in `before_refactor.py`:
1. **Single-letter and cryptic identifiers:** `d`, `x`, `s`, `t`, `res`.
2. **Monolithic code structure:** No modular functions or classes; all code executed in global scope.
3. **Manual iterations for standard aggregations:** `t = t + y` instead of built-in `sum()`.
4. **Fragile string concatenations:** Difficult to read and prone to type errors.
5. **Lack of type hints and documentation:** Zero docstrings or typing metadata.

### Improvements Applied in `after_refactor.py`:
- **Dataclass Representation:** `StudentRecord` encapsulates data and related calculations (`average_score`, `letter_grade`).
- **Encapsulated Business Logic:** `GradeReport` handles aggregation and formatted report output.
- **Type Annotations & PEP 8:** Full Python type hints (`List`, `Optional`) and clean naming conventions.
- **Python Built-ins:** Using Pythonic functions like `max(..., key=...)` for readability and performance.

---

## How to Run & Compare

```bash
# Run original messy script
python before_refactor.py

# Run AI-refactored script
python after_refactor.py
```
