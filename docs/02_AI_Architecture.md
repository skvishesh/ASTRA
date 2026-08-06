

# DOCUMENT 02

# AI_ARCHITECTURE.md




---

# ASTRA

# AI Architecture

Version

1.0.0

Status

Production Draft

Priority

Critical

Owner

ASTRA Project

---

# Document Purpose

This document defines the complete artificial intelligence architecture powering ASTRA.

Unlike a traditional chatbot, ASTRA is designed as an intelligent coaching system composed of structured modules that cooperate to deliver evidence-based fitness guidance.

This document defines:

* AI philosophy
* reasoning pipeline
* orchestration
* memory retrieval
* tool calling
* decision hierarchy
* communication rules
* safety principles

This document intentionally excludes implementation details such as frontend code, backend framework configuration, and database schema. Those are covered in separate documents.

---

# Table of Contents

1. Vision

2. AI Philosophy

3. System Overview

4. Core Principles

5. AI Layers

6. Decision Pipeline

7. Context Pipeline

8. Memory Retrieval

9. Tool Calling

10. Reasoning

11. Response Generation

12. Safety Rules

13. Failure Handling

14. Future Expansion

---

# 1 Vision

ASTRA is not designed to answer fitness questions.

ASTRA is designed to become a long-term strength coach.

Traditional assistants answer questions.

ASTRA makes coaching decisions.

The difference is significant.

Instead of asking

> What workout should I do?

The user asks

> Astra, start today's workout.

ASTRA retrieves today's program, verifies recovery status, checks for missed sessions, evaluates progression history, and begins guiding the session.

The language model is only one component in this process.

---

# 2 AI Philosophy

The AI follows five permanent principles.

## Principle 1

Context before conversation.

ASTRA should never answer using conversation history alone.

Instead it retrieves structured context.

Example

Bad

```
User:

Should I increase bench?

↓

LLM guesses.
```

Good

```
User

↓

Retrieve Bench History

↓

Retrieve Recovery

↓

Retrieve Progression Rules

↓

Generate Recommendation
```

---

## Principle 2

Tools before reasoning.

Whenever deterministic information exists, retrieve it using tools.

Never ask the LLM to estimate values that already exist.

Examples

Instead of

> Calculate my protein.

Use

```
getNutritionSummary()
```

Instead of

> What was my last bench?

Use

```
getExerciseHistory()
```

---

## Principle 3

Structured data before memory.

Priority

1

Database

↓

2

Coach Memory

↓

3

Recent Conversation

↓

4

LLM reasoning

Never reverse this order.

---

## Principle 4

Explain recommendations.

Every recommendation must answer

* What?
* Why?
* Next?

Example

Recommendation

Increase bench to 62.5 kg.

Reason

You completed all working sets within the progression rule for two consecutive sessions while maintaining target RIR.

Next

Maintain the new load until you again satisfy the progression criteria.

---

## Principle 5

Never guess.

If confidence is low,

ask one question.

Never invent data.

---

# 3 System Overview

```
                    USER

                      │

        Voice / Text / Buttons

                      │

────────────────────────────────

        Intent Detection Layer

────────────────────────────────

         Context Builder

────────────────────────────────

        Memory Retrieval

────────────────────────────────

          Tool Engine

────────────────────────────────

      Rule Engine

────────────────────────────────

        AI Reasoning

────────────────────────────────

     Structured Response

────────────────────────────────

             ASTRA
```

This pipeline is mandatory.

No shortcut is allowed.

---

# 4 Core Objectives

Every AI decision must satisfy all four objectives.

## Objective 1

Increase coaching accuracy.

---

## Objective 2

Reduce hallucination.

---

## Objective 3

Improve consistency.

---

## Objective 4

Keep responses explainable.

---

# 5 AI Architecture Layers

ASTRA consists of eight logical layers.

---

Layer 1

Input Layer

Responsibilities

Receive

* voice
* text
* button actions

Normalize them into one request.

Voice

↓

Speech-to-text

↓

Same pipeline.

Buttons

↓

Same pipeline.

Everything becomes

```
UserRequest
```

---

Layer 2

Intent Detection

Responsibilities

Determine exactly

what the user wants.

Supported intents

Workout

Recovery

Nutrition

Education

Progress

Planning

Pain

Scheduling

Memory Update

General Conversation

Only one primary intent exists.

Secondary intents are optional.

---

Layer 3

Context Builder

The Context Builder decides

what information is required.

Example

Question

Should I increase bench?

Needed

Bench History

Recovery

Progression Rules

Ignored

Protein

Calendar

Sleep Notes

Old conversations

Only relevant context enters the prompt.

---

Layer 4

Memory Retrieval

Purpose

Retrieve only long-term coaching information.

Examples

Preferred split

Shoulder pain history

Pull-up goal

Morning workouts

College schedule

Equipment

Nothing else.




# 6. Tool Engine

## Purpose

The Tool Engine enables ASTRA to interact with structured application data and backend services instead of relying on language-model memory.

The LLM **never** accesses the database directly.

All external information is retrieved through tools.

---

## Responsibilities

The Tool Engine:

* Executes backend functions.
* Retrieves structured data.
* Validates requests.
* Formats tool results.
* Returns deterministic outputs.

---

## Tool Categories

### Workout

Examples

```text
getTodayWorkout()

startWorkout()

getCurrentExercise()

logSet()

finishExercise()

finishWorkout()
```

---

### Progress

```text
getExerciseHistory()

calculateEstimated1RM()

recommendProgression()

detectPlateau()
```

---

### Recovery

```text
calculateReadiness()

getRecoverySummary()

updateRecovery()
```

---

### Nutrition

```text
logMeal()

proteinStatus()

dailyNutritionSummary()
```

---

### Memory

```text
searchMemory()

saveMemory()

updateMemory()
```

---

### Planning

```text
rescheduleWorkout()

travelMode()

updateGoal()
```

---

### Analytics

```text
generateWeeklyReview()

generateMonthlyReview()

analyzeConsistency()
```

---

# Tool Calling Rules

The LLM should call tools whenever:

* Historical data is required.
* Calculations are required.
* User information exists.
* Workout information exists.
* Progress information exists.

The LLM should **not** answer from memory when reliable data can be retrieved.

---

# 7. Rule Engine

The Rule Engine is completely deterministic.

No AI reasoning is used.

---

## Responsibilities

* Progression rules
* Deload rules
* Workout scheduling
* Exercise substitutions
* Safety rules
* Recovery thresholds

---

## Example

Question

> Should I increase bench?

Pipeline

```text
Exercise History
        ↓
Progression Rule
        ↓
Recovery Status
        ↓
Decision
```

The Rule Engine decides.

The LLM explains.

---

# Rule Hierarchy

Priority

```text
Safety
    ↓
Workout Rules
    ↓
Progression Rules
    ↓
Recovery Rules
    ↓
User Preferences
```

Safety always overrides everything.

---

# 8. Reasoning Engine

Purpose

The Reasoning Engine converts structured outputs into coaching advice.

---

## Responsibilities

* Explain recommendations.
* Ask follow-up questions.
* Compare options.
* Resolve ambiguity.
* Educate the user.

---

The Reasoning Engine does **not**:

* Calculate progression.
* Calculate nutrition.
* Search history.
* Replace deterministic services.

---

# Example

Input

```text
Bench Progression

Recommended:
Increase to 62.5 kg

Confidence:
97%
```

Output

> I recommend increasing your bench press to **62.5 kg** next session because you successfully completed all target sets at your previous weight while maintaining the planned effort level. Continue with the new weight and monitor your technique.

---

# 9. Confidence Engine

Every recommendation includes an internal confidence score.

Example

```text
95–100%
High Confidence

80–94%
Moderate Confidence

Below 80%
Clarification Required
```

---

## Example

User

> My shoulder hurts.

Confidence

Low.

ASTRA asks

> Which movement causes the pain?

instead of making assumptions.

---

# 10. Response Generator

Every response follows the same structure.

```
Recommendation

↓

Reason

↓

Next Step
```

Optional

* Clarification question
* Warning
* Reference to previous performance

---

## Example

Recommendation

Maintain your current bench weight.

Reason

You did not reach the upper target rep range on your final working set.

Next Step

Attempt the same load again next session.

---

# 11. Context Window Strategy

ASTRA should never send the entire conversation to the LLM.

Instead:

```
Current Question

↓

Relevant Memory

↓

Relevant Workout Data

↓

Relevant Recovery Data

↓

Rules

↓

Prompt
```

This minimizes token usage while improving consistency.

---

# 12. Multi-Provider Architecture

The AI Provider Layer must support multiple LLM providers.

Initial design:

```
ASTRA

↓

AI Provider Interface

↓

Gemini

↓

OpenAI

↓

Local Models
```

The application communicates only with the Provider Interface.

Changing providers must not require changes to business logic.

---

# 13. Local vs Cloud AI

Local AI should be used for:

* Fast summaries
* Small educational questions
* Offline functionality (where feasible)

Cloud AI should be used for:

* Complex coaching conversations
* Long-context reasoning
* Weekly reviews
* Planning

The Provider Interface selects the most appropriate provider.

---

# 14. Error Recovery

If a tool fails:

1. Retry if appropriate.
2. Use cached data when safe.
3. Explain the limitation.
4. Never fabricate information.

Example

> I couldn't retrieve your workout history right now. I can continue the current workout, but I won't make progression recommendations until your history is available.

---





# 15. Memory Integration

## Purpose

Memory allows ASTRA to provide long-term personalized coaching instead of restarting every conversation from scratch.

Memory is divided into distinct categories.

---

## Memory Types

```text
Profile Memory
```

Stores long-term profile information.

Examples:

* Height
* Weight
* Preferred training split
* Gym availability
* Equipment
* Training time

---

```text
Goal Memory
```

Examples:

* Body recomposition
* First pull-up
* Improve posture
* Athletic performance
* Increase upper-body strength

---

```text
Preference Memory
```

Examples:

* One exercise at a time
* Morning workouts
* Voice-first interaction
* Professional coaching style
* 60-minute sessions

---

```text
Performance Memory
```

Examples:

* Bench progression
* Pull-up progression
* Weekly volume
* Estimated 1RM trends

---

```text
Recovery Memory
```

Examples:

* Shoulder discomfort history
* Deload history
* Recovery trends

---

## Memory Retrieval Rules

Only retrieve memory that directly supports the user's request.

Example:

Question

> How is my bench improving?

Retrieve

* Bench history
* Previous recommendations
* Current progression status

Do **not** retrieve unrelated nutrition or scheduling memories.

---

# 16. AI Lifecycle

Every request follows the same lifecycle.

```text
User Request
      ↓
Normalize Input
      ↓
Detect Intent
      ↓
Build Context
      ↓
Retrieve Memory
      ↓
Call Required Tools
      ↓
Apply Rule Engine
      ↓
LLM Reasoning
      ↓
Validate Response
      ↓
Return Answer
      ↓
Update Memory (if needed)
```

No stage may be skipped.

---

# 17. Safety Principles

ASTRA must prioritize user safety over convenience.

### Never

* Ignore pain reports.
* Recommend unsafe training.
* Fabricate exercise history.
* Pretend confidence when uncertain.
* Recommend progression without supporting data.

---

### Always

* Ask for clarification when confidence is low.
* Recommend professional medical evaluation when symptoms exceed normal training discomfort.
* Explain why a recommendation is being made.

---

# 18. Performance Targets

| Component           |  Target |
| ------------------- | ------: |
| Intent Detection    |  <50 ms |
| Context Builder     | <100 ms |
| Memory Retrieval    | <150 ms |
| Tool Execution      | <200 ms |
| Rule Engine         |  <50 ms |
| Prompt Assembly     |  <50 ms |
| AI Response (Cloud) |    <3 s |
| AI Response (Local) |  <1.5 s |

These targets guide engineering decisions but may be refined during implementation.

---

# 19. Testing Strategy

Every AI capability requires automated testing.

### Intent Tests

Verify correct intent classification.

Examples:

* "Start workout"
* "How much protein have I eaten?"
* "Should I increase bench?"

---

### Tool Tests

Verify:

* Correct tool selection
* Correct inputs
* Correct outputs
* Error handling

---

### Memory Tests

Verify:

* Relevant memories are retrieved.
* Irrelevant memories are ignored.
* Memory updates occur only when appropriate.

---

### Safety Tests

Examples:

Input:

> My shoulder hurts during pressing.

Expected behavior:

* Clarify severity/location if needed.
* Avoid unsafe recommendations.
* Suggest appropriate substitutions when supported.

---

# 20. Logging & Observability

Each AI request should record:

* Request ID
* Timestamp
* Intent
* Tools used
* Response duration
* Success/failure
* Provider used

Sensitive personal content should not be unnecessarily logged.

---

# 21. Architecture Decision Records (ADR)

## ADR-001

**Decision:** Tool-first architecture.

**Reason:** Improves accuracy and reduces hallucinations.

---

## ADR-002

**Decision:** Rule Engine handles deterministic logic.

**Reason:** Keeps progression and safety consistent across providers.

---

## ADR-003

**Decision:** Modular Prompt Library.

**Reason:** Easier maintenance and independent prompt evolution.

---

## ADR-004

**Decision:** Single AI agent in Version 1.

**Reason:** Simpler implementation and debugging while remaining extensible for future specialist agents.

---

# 22. Future Expansion

The architecture should allow future support for:

* Multiple AI agents
* Wearable integrations
* Camera-based movement analysis
* External health platforms
* Advanced recovery models
* Personalized predictive analytics

These additions should extend existing interfaces rather than replace them.

---

# 23. Acceptance Criteria

This document is considered implemented when:

* AI uses structured tools before reasoning.
* Context retrieval is selective.
* Rule Engine handles deterministic decisions.
* Memory retrieval is relevant.
* Responses are explainable.
* Safety rules are enforced.
* Multiple AI providers can be supported through a common interface.

---

# 24. Summary

The AI architecture is built on four pillars:

```text
Structured Data
        +
Tool Engine
        +
Rule Engine
        +
Language Model
        =
ASTRA
```

The language model is **one component**, not the entire system.

This separation improves reliability, maintainability, and long-term scalability.

---

# END OF DOCUMENT

**Document Status:** ✅ COMPLETE

**Version:** 1.0.0

**Next Document:** `03_Database_Architecture.md`

