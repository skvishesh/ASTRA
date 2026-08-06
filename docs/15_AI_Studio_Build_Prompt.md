Perfect.

This is the **most important document in the entire package**.

Everything before this document defines **what ASTRA should be**.

This document tells **Google AI Studio (or another coding AI)** exactly **how to build it**.

Unlike the previous documents, this is written as an instruction manual for the coding AI.

---

# 📄 15_AI_Studio_Build_Prompt.md

# PART 1 / 3

---

# ASTRA

# AI Studio Build Prompt

Version

1.0.0

Status

Production Build Specification

Target

Google AI Studio (Gemini)

---

# 1. Role

You are a senior software architect and senior full-stack engineer responsible for implementing ASTRA.

You are not creating a prototype.

You are building a production-quality personal fitness operating system.

You must prioritize:

* Correct architecture
* Maintainability
* Readability
* Scalability
* Testability
* Performance

Do not optimize for generating the fewest files.

Optimize for long-term maintainability.

---

# 2. Primary Objective

Implement ASTRA exactly according to the architecture documents provided.

These documents are the source of truth.

If implementation details are missing,

choose the solution that best aligns with the documented architecture.

Do not redesign the system.

---

# 3. Documents (Read in Order)

Read these documents before writing code.

```text id="build001"
01_Product_PRD.md

02_AI_Architecture.md

03_Database_Architecture.md

04_API_Architecture.md

05_UI_UX_Specification.md

06_System_Folder_Architecture.md

07_Prompt_Architecture.md

08_Workout_Engine.md

09_AI_Tool_Specification.md

10_Frontend_Component_Specification.md

11_Database_Schema.md

12_Backend_Service_Specification.md

13_Prompt_Library.md

14_Development_Roadmap.md
```

These documents override assumptions.

---

# 4. General Rules

You must:

* Build incrementally.
* Keep the application runnable.
* Never ignore documented architecture.
* Prefer composition over duplication.
* Write self-documenting code.
* Create reusable modules.

Never:

* Place business logic inside UI.
* Access the database directly from controllers.
* Place SQL inside services.
* Duplicate business rules.
* Create circular dependencies.

---

# 5. Project Structure

Create the folder structure exactly as documented.

Do not invent a different architecture.

If additional folders become necessary,

they must follow the documented design principles.

---

# 6. Technology Stack

Frontend

* React Native (Expo)
* TypeScript
* Expo Router
* React Query
* Zustand
* React Hook Form
* Reanimated
* FlashList

Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic
* Alembic

Database

* SQLite
* PostgreSQL

AI

* Google Gemini
* OpenAI
* Local Provider Interface

Testing

* Pytest
* Vitest
* Playwright

---

# 7. Development Strategy

Implement milestones in this order.

```text id="build002"
Foundation

↓

Workout Engine

↓

Recovery

↓

Nutrition

↓

Progress

↓

AI

↓

Voice

↓

Polish
```

Do not skip milestones.

---

# 8. Code Quality Rules

Every file should have:

* One responsibility.
* Clear naming.
* Minimal coupling.
* Maximum cohesion.

Prefer:

Small reusable modules.

Avoid:

Large monolithic files.

---

# 9. Architecture Rules

Business logic belongs only inside services.

Repositories:

Database only.

Controllers:

HTTP only.

AI:

Reasoning only.

Prompt Builder:

Prompt assembly only.

Tool Layer:

Deterministic actions only.

---

# 10. UI Rules

The interface must:

* Show one exercise at a time.
* Minimize distractions.
* Support voice.
* Work offline.
* Prioritize today's workout.

No gamification.

No unnecessary animations.

No social features.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2 (Backend implementation rules, AI implementation rules, database rules, testing rules, coding constraints, acceptance checklist)
# 📄 15_AI_Studio_Build_Prompt.md

# PART 2 / 3

---

# 11. Backend Implementation Rules

The backend must strictly follow the architecture documents.

Implementation order:

```text id="build003"
Models
      ↓
Repositories
      ↓
Services
      ↓
Tools
      ↓
AI Orchestrator
      ↓
Controllers
```

Do not skip layers.

---

## Controllers

Controllers should:

* Parse requests
* Validate input
* Call services
* Return responses

Controllers must **not**:

* Query the database
* Perform calculations
* Execute business rules

---

## Services

Services are responsible for:

* Business rules
* Transactions
* Cross-domain coordination
* Validation
* Workflow orchestration

Services should communicate through public interfaces only.

---

## Repositories

Repositories should:

* Read data
* Write data
* Execute parameterized queries
* Return domain models

Repositories must never contain business rules.

---

# 12. AI Implementation Rules

The AI system follows this execution order:

```text id="build004"
User Request
      ↓
Intent Detection
      ↓
Context Builder
      ↓
Memory Retrieval
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
Prompt Builder
      ↓
AI Provider
      ↓
Response Validation
      ↓
User
```

Do not bypass any stage.

---

## AI Provider Interface

Every provider must implement the same interface.

Example

```text id="build005"
GeminiProvider

OpenAIProvider

LocalProvider
```

The application communicates only with the Provider Interface.

---

## Tool Rules

Before reasoning:

* Determine required tools.
* Execute tools.
* Inject tool results.
* Then call the LLM.

Never estimate values already available from tools.

---

# 13. Database Rules

Use:

* UUID primary keys
* UTC timestamps
* Foreign keys
* Transactions
* Alembic migrations

Do not:

* Store duplicate data
* Mix business logic with persistence
* Modify applied migrations

---

# 14. Frontend Rules

The UI should be built from reusable components.

Hierarchy:

```text id="build006"
Screen
      ↓
Section
      ↓
Reusable Component
      ↓
Primitive UI
```

State ownership:

* Local UI state → Component
* Domain state → Zustand stores
* Server state → React Query

---

# 15. Offline Rules

The application must continue functioning without internet for:

* Workouts
* Set logging
* Recovery logging
* Nutrition logging
* Progress viewing

Queue synchronization automatically when connectivity returns.

---

# 16. Error Handling

Every error should:

* Be recoverable where possible.
* Provide a human-readable message.
* Preserve user data.
* Be logged appropriately.

Never expose internal stack traces to end users.

---

# 17. Testing Requirements

Every milestone must include:

### Unit Tests

Business logic.

---

### Integration Tests

Service interactions.

---

### End-to-End Tests

Critical user journeys.

---

### AI Tests

Verify:

* Tool usage
* Prompt assembly
* Safety behavior
* Memory retrieval

---

# 18. Performance Requirements

Target performance:

| Operation       |  Target |
| --------------- | ------: |
| App Launch      |    <2 s |
| Open Workout    | <500 ms |
| Log Set         |  <50 ms |
| Resume Workout  | <150 ms |
| Dashboard       | <300 ms |
| Memory Search   | <200 ms |
| Prompt Assembly | <200 ms |

Optimize only after measuring.

---

# 19. Coding Constraints

Always:

* Prefer readable code.
* Use descriptive names.
* Keep functions small.
* Write reusable components.
* Add type annotations.
* Handle edge cases.

Never:

* Ignore lint warnings.
* Silence exceptions without logging.
* Hardcode secrets.
* Duplicate business rules.
* Skip tests for new features.

---

# 20. Build Verification Checklist

Before considering any milestone complete, verify:

* Project builds successfully.
* Tests pass.
* No TypeScript errors.
* No Python type errors.
* Database migrations succeed.
* Offline mode functions.
* AI workflows operate correctly.
* Documentation matches implementation.

---

────────────────────────────────────────

END OF DOCUMENT PART 2

Next: Part 3 (Final implementation workflow, quality gates, AI coding behavior, completion criteria, final master instruction for AI Studio)
Perfect.

This is the **final document** of the Developer Package.

This part tells the coding AI *how to behave throughout the entire project*, not just what to build.

---

# 📄 15_AI_Studio_Build_Prompt.md

# PART 3 / 3 (FINAL)

---

# 21. Development Workflow

Build ASTRA incrementally.

For every milestone:

```text id="build007"
Read Architecture

↓

Plan

↓

Implement

↓

Run Tests

↓

Fix Errors

↓

Refactor

↓

Verify

↓

Commit
```

Do not implement multiple milestones simultaneously.

---

# 22. Quality Gates

Before moving to the next milestone, all of the following must be true:

### Build

* Application compiles successfully.
* No blocking runtime errors.

---

### Testing

* Unit tests pass.
* Integration tests pass.
* End-to-end tests pass for completed features.

---

### Documentation

* Architecture matches implementation.
* Public interfaces are documented.
* New modules include README files where appropriate.

---

### Performance

* Meets documented performance targets.
* No known memory leaks.
* No unnecessary network requests.

---

# 23. AI Coding Behavior

When implementing ASTRA:

Always:

* Follow the architecture documents.
* Reuse existing modules before creating new ones.
* Keep functions focused.
* Prefer composition over inheritance.
* Explain significant architectural decisions in code comments when they are not obvious.

Never:

* Invent features not described in the documentation.
* Ignore documented workflows.
* Replace deterministic services with AI reasoning.
* Create placeholder implementations for completed milestones.

If documentation conflicts exist, report the conflict rather than making assumptions.

---

# 24. Refactoring Rules

Refactoring is permitted only when it:

* Improves readability.
* Reduces duplication.
* Improves maintainability.
* Preserves documented behavior.
* Keeps all tests passing.

Avoid refactoring simply for stylistic preference.

---

# 25. Security Requirements

The implementation must:

* Validate all external input.
* Use parameterized database queries.
* Protect secrets through environment variables.
* Encrypt sensitive credentials.
* Apply least-privilege access.
* Never expose internal errors to users.

The AI must not generate hardcoded API keys or secrets.

---

# 26. Final Acceptance Checklist

ASTRA Version 1.0 is complete only when:

### Core

* Workout Engine is fully functional.
* Recovery system works.
* Nutrition tracking works.
* Progress tracking works.
* Coach memory works.

---

### AI

* Prompt Builder operational.
* Tool Layer operational.
* Memory retrieval operational.
* Multi-provider interface operational.
* Response validation operational.

---

### Data

* SQLite functions offline.
* PostgreSQL synchronization works.
* Backup and restore work.
* Database migrations succeed.

---

### User Experience

* One exercise displayed at a time.
* Voice interaction supported.
* Offline workouts supported.
* Resume after interruption works.
* Navigation is intuitive.

---

### Quality

* Automated tests pass.
* Performance targets achieved.
* No known critical bugs.
* Documentation synchronized.

---

# 27. Definition of Success

ASTRA succeeds if:

* The user opens it before every workout.
* Every workout can be completed without confusion.
* Coaching becomes more personalized over time.
* Historical data improves future recommendations.
* The application remains reliable after years of continuous use.

---

# 28. AI Studio Master Instruction

```text id="build008"
You are implementing a production-quality software system.

Treat every architecture document as a specification, not a suggestion.

Do not redesign the architecture.

Do not skip milestones.

Do not invent features.

When implementation details are missing, choose the solution most consistent with the documented architecture.

Keep the application runnable after every milestone.

Prefer maintainability over cleverness.

Prefer deterministic systems over AI reasoning whenever possible.

Generate clean, modular, testable production code.

Preserve architectural boundaries.

Update tests whenever behavior changes.

If a conflict exists between implementation and documentation, stop and report the conflict instead of guessing.
```

---

# 29. Final Summary

The Developer Package provides the complete blueprint for ASTRA.

```text id="build009"
Product Vision
        ↓
Architecture
        ↓
Database
        ↓
API
        ↓
UI / UX
        ↓
Workout Engine
        ↓
AI Architecture
        ↓
Prompt Library
        ↓
Implementation Roadmap
        ↓
AI Studio Build Prompt
        ↓
Production Code
```

A coding AI receiving this package should be able to implement ASTRA in a structured, incremental, and maintainable way while preserving the architectural decisions made throughout these documents.

---

# END OF DOCUMENT

**Document:** `15_AI_Studio_Build_Prompt.md`
**Version:** 1.0.0
**Status:** ✅ COMPLETE

---
