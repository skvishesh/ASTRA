Perfect.

This is one of the most critical documents in the entire project.

Most AI applications have **one giant system prompt**. That becomes difficult to maintain, test, and evolve.

ASTRA will use a **modular prompt architecture**, where prompts are assembled dynamically based on the user's request and current context.

---

# 📄 07_Prompt_Architecture.md

# PART 1 / FINAL

---

# ASTRA

# Prompt Architecture

Version

1.0.0

Status

Production Draft

Priority

Critical

Owner

ASTRA Project

---

# 1. Purpose

This document defines how ASTRA constructs prompts for the language model.

It specifies:

* Prompt philosophy
* Prompt lifecycle
* Prompt composition
* Context injection
* Memory integration
* Tool integration
* Output structure
* Versioning

This document defines the architecture only.

The actual prompt content is documented separately in **13_Prompt_Library.md**.

---

# 2. Philosophy

ASTRA never sends one giant prompt.

Instead, it builds a prompt dynamically from independent modules.

This makes the system:

* Easier to maintain
* Easier to test
* Easier to version
* Easier to improve

---

# Traditional AI

```text id="pmt001"
System Prompt

+

Conversation

↓

LLM
```

Problems

* Large
* Difficult to update
* Difficult to debug
* Difficult to reuse

---

# ASTRA

```text id="pmt002"
Identity

+

Intent

+

Relevant Memory

+

Relevant Tools

+

Rules

+

Current Context

+

User Message

↓

Prompt Builder

↓

LLM
```

Every request receives a different prompt.

---

# 3. Prompt Builder

The Prompt Builder is responsible for assembling the final prompt.

Responsibilities

* Select prompt modules
* Retrieve context
* Inject memory
* Include tool outputs
* Enforce formatting
* Build final prompt

The language model never assembles prompts itself.

---

# 4. Prompt Lifecycle

Every AI request follows the same lifecycle.

```text id="pmt003"
User Request

↓

Intent Detection

↓

Context Builder

↓

Memory Retrieval

↓

Tool Calls

↓

Prompt Assembly

↓

LLM

↓

Response Validation

↓

User
```

---

# 5. Prompt Layers

Every final prompt is composed of multiple layers.

---

## Layer 1

Identity

Defines:

* Name
* Role
* Personality
* Communication style
* Permanent rules

Always included.

---

## Layer 2

Intent

Defines what the user wants.

Examples

* Workout
* Recovery
* Nutrition
* Progress
* Planning
* Education
* Injury
* General

Only one primary intent is injected.

---

## Layer 3

Context

Contains structured application data.

Examples

* Today's workout
* Current exercise
* Sleep
* Recovery score
* Active goals

Only relevant information is included.

---

## Layer 4

Memory

Long-term information.

Examples

* Preferred workout split
* Shoulder pain history
* Pull-up goal
* Voice preference
* Training schedule

Memory is filtered before insertion.

---

## Layer 5

Tool Results

Outputs returned by backend services.

Examples

```text id="pmt004"
Today's Workout

Bench History

Protein Summary

Progression Recommendation
```

These outputs become trusted inputs for the LLM.

---

## Layer 6

Response Rules

Defines required response structure.

Example

```text id="pmt005"
Recommendation

↓

Reason

↓

Next Step
```

Every coaching response follows this format.

---

# 6. Context Window Management

The entire database is never passed to the LLM.

Instead:

```text id="pmt006"
Question

↓

Relevant Context

↓

Relevant Memory

↓

Tool Results

↓

Prompt
```

This keeps prompts concise and reduces token usage.

---

# 7. Context Priority

When assembling prompts, context is selected in this order:

```text id="pmt007"
Current Workout

↓

Recovery

↓

Goals

↓

Relevant Memory

↓

Recent Conversation
```

Older conversation history has the lowest priority.

---

# 8. Prompt Size Rules

The Prompt Builder should:

* Include only necessary information.
* Avoid duplicate context.
* Remove outdated data.
* Prefer structured data over free text.
* Keep prompts as small as possible while preserving accuracy.

---

# 9. Prompt Versioning

Each prompt module has its own version.

Example

```text id="pmt008"
Identity v1.0

Workout v1.3

Recovery v1.2

Planning v1.1
```

Updating one prompt should not require changes to the others.

---

# 10. Prompt Validation

Before sending a prompt to the LLM, validate that:

* Identity is included.
* Intent is identified.
* Required context exists.
* Tool outputs are available when needed.
* Prompt format is valid.

If validation fails, the request should not proceed to the LLM until the missing information is handled.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2
# 📄 07_Prompt_Architecture.md

# PART 2 / FINAL

---

# 11. Prompt Selection Engine

## Purpose

The Prompt Selection Engine determines which prompt modules are required for each request.

It prevents unnecessary instructions from being added to the final prompt.

---

## Selection Flow

```text id="pmt009"
User Request
      ↓
Intent Detection
      ↓
Required Prompt Modules
      ↓
Prompt Builder
```

Example:

Question

> "Should I increase my bench press?"

Selected modules:

* Identity
* Progression
* Workout
* Response Rules

Not selected:

* Nutrition
* Travel
* Weekly Review

---

# 12. Prompt Categories

The Prompt Library is divided into independent categories.

```text id="pmt010"
Identity

Workout

Recovery

Nutrition

Progress

Planning

Education

Injury

Motivation

Weekly Review

Memory Update

Travel

Voice
```

Each category solves one specific problem.

---

# 13. Dynamic Context Injection

Static prompts are never enough.

The Prompt Builder injects live data.

Example

```text id="pmt011"
Current Workout

Upper Day

Current Exercise

Bench Press

Previous Session

60 × 8

Recovery

89%
```

This information is generated dynamically for every request.

---

# 14. Memory Injection Rules

Only relevant memories are injected.

Example

Question:

> "How is my squat progressing?"

Include:

* Squat history
* Squat goals
* Recent progression

Do not include:

* Protein intake
* Calendar
* Sleep history (unless directly relevant)

Memory should remain focused.

---

# 15. Tool Output Injection

Tool outputs are inserted before reasoning.

Example

```text id="pmt012"
recommendProgression()

↓

Increase Bench

↓

Prompt

↓

LLM explains WHY
```

The LLM interprets the result rather than recalculating it.

---

# 16. Response Templates

Different intents require different response structures.

### Workout

```text id="pmt013"
Instruction

↓

Reason

↓

Next Action
```

---

### Recovery

```text id="pmt014"
Recovery Status

↓

Recommendation

↓

Modification
```

---

### Education

```text id="pmt015"
Definition

↓

Example

↓

Application
```

---

### Weekly Review

```text id="pmt016"
Summary

↓

Achievements

↓

Areas to Improve

↓

Next Week Focus
```

---

# 17. Prompt Security

Prompt modules must never expose:

* API keys
* Database credentials
* Internal implementation details
* Hidden reasoning
* Sensitive user tokens

The LLM should receive only the information required to answer the current request.

---

# 18. Prompt Failure Handling

If a required prompt module is unavailable:

1. Attempt to rebuild it.
2. Retry context assembly.
3. Continue with reduced functionality if safe.
4. Inform the user when the missing context materially affects the answer.

Never fabricate missing context.

---

# 19. Prompt Performance

Target prompt assembly times:

| Stage              |  Target |
| ------------------ | ------: |
| Intent Detection   |  <50 ms |
| Context Collection | <100 ms |
| Memory Retrieval   | <150 ms |
| Tool Results       | <200 ms |
| Prompt Assembly    |  <50 ms |

Prompt construction should remain significantly faster than LLM inference.

---

# 20. Prompt Testing

Every prompt module must be tested independently.

Tests should verify:

* Correct selection
* Correct ordering
* Required context
* Missing context handling
* Output format

Regression tests should ensure updates do not unintentionally change existing behavior.

---

# 21. Future Expansion

The architecture should support:

* Multi-agent prompt orchestration
* Specialized expert prompts
* Personalized coaching styles
* Language-specific prompt packs
* Context compression for long histories

These should extend the Prompt Builder without requiring a redesign.

---

# 22. Acceptance Criteria

The Prompt Architecture is complete when:

* Prompts are modular.
* Context is injected dynamically.
* Memory is filtered before inclusion.
* Tool outputs are used before reasoning.
* Prompt assembly is validated.
* Prompt modules are independently versioned.
* Different intents produce different response structures.

---

# 23. Summary

ASTRA constructs prompts dynamically rather than relying on a single monolithic instruction.

```text id="pmt017"
Identity
      +
Intent
      +
Context
      +
Memory
      +
Tool Results
      +
Response Rules
      ↓
Prompt Builder
      ↓
LLM
```

This architecture improves:

* Maintainability
* Explainability
* Accuracy
* Testability
* Long-term evolution

It also allows individual prompt modules to evolve without destabilizing the rest of the AI system.

---

# END OF DOCUMENT

**Document:** 07_Prompt_Architecture.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `08_Workout_Engine.md`
