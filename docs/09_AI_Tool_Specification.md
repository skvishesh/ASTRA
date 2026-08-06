Perfect.

This document is **the bridge between the AI and your application**.

Without tools, ASTRA is just another chatbot.

With tools, ASTRA becomes an intelligent coach that can actually interact with your data and perform actions.

---

# 📄 09_AI_Tool_Specification.md

# PART 1 / FINAL

---

# ASTRA

# AI Tool Specification

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

This document defines every tool that the AI is allowed to use.

The AI **never**:

* accesses the database directly
* modifies application state directly
* performs business logic

Instead, it communicates through a controlled Tool Layer.

This guarantees:

* Security
* Consistency
* Deterministic behavior
* Testability

---

# 2. Tool Philosophy

Every tool must:

* Do one thing.
* Return structured data.
* Be deterministic.
* Be independently testable.
* Be reusable.
* Never call another tool internally.

---

# 3. Tool Categories

```text id="tool001"
Workout

Recovery

Nutrition

Progress

Memory

Planning

Analytics

Settings

System
```

Each category owns its own tools.

---

# 4. Tool Lifecycle

Every tool follows the same execution flow.

```text id="tool002"
AI Request
      ↓
Tool Selection
      ↓
Input Validation
      ↓
Business Service
      ↓
Database
      ↓
Structured Response
      ↓
LLM
```

The LLM never bypasses this pipeline.

---

# 5. Workout Tools

---

## getTodayWorkout()

### Purpose

Returns today's planned workout.

---

### Input

None.

---

### Output

```text id="tool003"
Workout Name

Workout ID

Focus

Estimated Duration

Exercises
```

---

## startWorkout()

Purpose

Begins today's workout.

Output

```text id="tool004"
Workout Started

Current Exercise

Start Time
```

---

## getCurrentExercise()

Purpose

Returns the currently active exercise.

Output

```text id="tool005"
Exercise Name

Target Sets

Target Reps

Tempo

Rest Time
```

---

## logSet()

Purpose

Logs one completed set.

Input

```text id="tool006"
Exercise

Weight

Reps

RIR

Notes (optional)
```

Output

```text id="tool007"
Success

Current Set

Remaining Sets
```

---

## finishExercise()

Purpose

Marks the current exercise as complete.

Output

```text id="tool008"
Exercise Complete

Next Exercise
```

---

## finishWorkout()

Purpose

Completes the workout.

Output

```text id="tool009"
Workout Summary

Duration

Volume

PRs

Recovery Advice
```

---

# 6. Progress Tools

---

## getExerciseHistory()

Purpose

Returns historical performance for one exercise.

Input

Exercise ID

Output

```text id="tool010"
Previous Sessions

Best Weight

Best Reps

Estimated 1RM
```

---

## recommendProgression()

Purpose

Runs the deterministic progression algorithm.

Input

Exercise ID

Output

```text id="tool011"
Increase

Maintain

Reduce

Deload

Reason
```

---

## detectPlateau()

Purpose

Checks whether progress has stalled.

Output

```text id="tool012"
Plateau

Confidence

Suggested Action
```

---

# 7. Recovery Tools

---

## getRecoverySummary()

Returns:

```text id="tool013"
Sleep

Fatigue

Readiness

Recovery Score
```

---

## calculateReadiness()

Purpose

Computes the readiness score using deterministic rules.

The AI explains the score but never calculates it.

---

## updateRecovery()

Purpose

Stores new recovery information.

Examples

* Sleep
* Fatigue
* Muscle soreness

---

# 8. Nutrition Tools

---

## getNutritionSummary()

Returns

```text id="tool014"
Calories

Protein

Water

Meals
```

---

## logMeal()

Purpose

Stores a meal.

Input

Meal details.

Output

Updated daily nutrition summary.

---

## proteinStatus()

Returns

```text id="tool015"
Current Protein

Target Protein

Remaining Protein
```

---

# 9. Memory Tools

---

## searchMemory()

Purpose

Retrieves only relevant long-term memories.

Input

Search context.

Output

Relevant memory objects.

---

## saveMemory()

Purpose

Stores new long-term memory.

Used only when information should persist beyond the current conversation.

---

## updateMemory()

Purpose

Updates existing memories while preserving version history where appropriate.

---

# 10. Planning Tools

---

## rescheduleWorkout()

Purpose

Adjusts the training calendar after missed sessions or schedule changes.

---

## enableTravelMode()

Purpose

Activates travel-specific workout adaptations.

---

## updateGoal()

Purpose

Updates long-term training goals.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2
Perfect.

This finishes **09_AI_Tool_Specification.md**.

---

# 📄 09_AI_Tool_Specification.md

# PART 2 / FINAL

---

# 11. Analytics Tools

## generateWeeklyReview()

### Purpose

Generates a structured weekly coaching report.

### Output

```text id="tool016"
Workout Completion %

Strength Progress

Recovery Summary

Nutrition Summary

Coach Recommendations
```

---

## generateMonthlyReview()

### Purpose

Produces a long-term progress report.

### Output

```text id="tool017"
Monthly Volume

Best Lifts

Consistency

Recovery Trends

Goal Progress
```

---

## analyzeConsistency()

### Purpose

Evaluates adherence to the training program.

### Output

```text id="tool018"
Workout Consistency

Nutrition Consistency

Sleep Consistency

Overall Score
```

---

# 12. Settings Tools

## getSettings()

Returns current application settings.

Examples

* Theme
* Voice
* Units
* AI Provider
* Notifications

---

## updateSettings()

Updates user preferences.

Every update should be validated before saving.

---

# 13. System Tools

## exportData()

Purpose

Exports user data.

Supported formats

* JSON
* CSV

Future

* PDF reports

---

## importData()

Purpose

Imports previously exported data.

Validation is required before importing.

---

## createBackup()

Creates a backup of local user data.

---

## restoreBackup()

Restores a previously created backup.

The user must confirm before overwriting existing data.

---

# 14. Tool Response Standard

Every tool returns the same response format.

Success

```json id="tool019"
{
  "success": true,
  "data": {},
  "message": "Operation completed successfully."
}
```

Failure

```json id="tool020"
{
  "success": false,
  "error": {
    "code": "WORKOUT_NOT_ACTIVE",
    "message": "No active workout is currently running."
  }
}
```

Consistency is mandatory across all tools.

---

# 15. Tool Naming Rules

Tool names must:

* Begin with a verb.
* Clearly describe the action.
* Be concise.
* Avoid abbreviations.

Examples

Good

```text id="tool021"
getTodayWorkout()

logSet()

finishWorkout()

searchMemory()
```

Avoid

```text id="tool022"
doWorkout()

run()

calc()

executeThing()
```

---

# 16. Tool Security

Every tool must validate:

* Authentication
* Authorization
* Input
* Business rules

The AI cannot bypass these validations.

Tools must never expose:

* API keys
* Database credentials
* Internal infrastructure details
* Hidden implementation logic

---

# 17. Tool Error Handling

Every tool should return structured errors.

Examples

```text id="tool023"
WORKOUT_NOT_ACTIVE

INVALID_REPS

INVALID_WEIGHT

MEMORY_NOT_FOUND

RECOVERY_DATA_MISSING

GOAL_NOT_FOUND

SYNC_FAILED
```

Errors should always include:

* Error code
* Human-readable message
* Recovery guidance (when applicable)

---

# 18. Tool Performance Targets

| Tool                 |  Target |
| -------------------- | ------: |
| getTodayWorkout      |  <50 ms |
| getCurrentExercise   |  <30 ms |
| logSet               |  <50 ms |
| finishWorkout        | <150 ms |
| searchMemory         | <150 ms |
| getRecoverySummary   |  <75 ms |
| recommendProgression | <100 ms |
| proteinStatus        |  <50 ms |

Tool execution should be significantly faster than AI response generation.

---

# 19. Tool Testing

Every tool requires:

### Unit Tests

Verify logic in isolation.

---

### Integration Tests

Verify interaction with services and database.

---

### Error Tests

Verify:

* Invalid inputs
* Missing data
* Authentication failures
* Network failures

---

### Performance Tests

Verify response times remain within documented targets.

---

# 20. Tool Registry

Every tool should be registered in a central registry.

Example

```text id="tool024"
Workout

getTodayWorkout

logSet

finishWorkout

-------------------

Recovery

calculateReadiness

updateRecovery

-------------------

Memory

searchMemory

saveMemory

-------------------

Analytics

generateWeeklyReview
```

The AI Orchestrator discovers tools through this registry rather than hardcoded references.

---

# 21. Future Expansion

The Tool Layer should support future capabilities.

Examples

* Camera analysis
* Wearable integration
* Heart-rate monitoring
* Mobility assessment
* Exercise recognition
* Nutrition barcode scanning

These should be added as new tool categories without modifying existing interfaces.

---

# 22. Acceptance Criteria

The Tool Layer is complete when:

* Every tool has a single responsibility.
* Inputs and outputs are structured.
* Security validation is enforced.
* Response formats are standardized.
* Errors are consistent.
* Tools remain deterministic.
* The AI never accesses storage directly.
* All tools are independently testable.

---

# 23. Summary

The Tool Layer is the controlled interface between ASTRA's intelligence and the application.

```text id="tool025"
User Request
      ↓
AI Orchestrator
      ↓
Tool Registry
      ↓
Selected Tool
      ↓
Application Service
      ↓
Database
      ↓
Structured Response
      ↓
LLM Explanation
      ↓
User
```

By separating reasoning from execution, ASTRA remains:

* Accurate
* Explainable
* Secure
* Maintainable
* Scalable

The language model focuses on coaching, while the Tool Layer performs deterministic operations.

---

# END OF DOCUMENT

**Document:** 09_AI_Tool_Specification.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `10_Frontend_Component_Specification.md`
