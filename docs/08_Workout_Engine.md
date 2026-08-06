Perfect.

This is the **heart of ASTRA**.

Everything else (AI, UI, database, voice) exists to support this engine.

If the Workout Engine is designed correctly, ASTRA will feel like a real coach instead of a chat app.

---

# 📄 08_Workout_Engine.md

# PART 1 / FINAL

---

# ASTRA

# Workout Engine

Version

1.0.0

Status

Production Draft

Priority

**Highest**

Owner

ASTRA Project

---

# 1. Purpose

The Workout Engine is responsible for planning, executing, tracking, adapting, and completing every workout session.

It is the core business engine of ASTRA.

Responsibilities include:

* Selecting today's workout
* Executing exercises
* Logging sets
* Managing rest periods
* Tracking progression
* Handling skipped exercises
* Managing interruptions
* Completing workouts

The AI **does not replace** the Workout Engine.

The AI explains and guides decisions made by the engine.

---

# 2. Design Philosophy

The Workout Engine follows one simple principle:

> **The user should never wonder what to do next.**

At every moment ASTRA knows:

* Current workout
* Current exercise
* Current set
* Remaining sets
* Next exercise
* Rest status
* Workout completion

The engine always exposes exactly one next action.

---

# 3. Workout Lifecycle

Every workout follows the same lifecycle.

```text id="wrk001"
Planned
      ↓
Ready
      ↓
Started
      ↓
Warm-up
      ↓
Working Sets
      ↓
Rest
      ↓
Next Exercise
      ↓
Workout Summary
      ↓
Completed
```

A workout can also be:

* Paused
* Resumed
* Cancelled
* Rescheduled

---

# 4. Workout Selection

When the user opens ASTRA, the engine determines today's workout.

Inputs considered:

* Training program
* Weekly schedule
* Recovery status
* Missed workouts
* Manual changes
* Deload status

The engine selects the most appropriate session before the AI is involved.

---

# 5. Workout States

The engine maintains exactly one active state.

```text id="wrk002"
Idle

Ready

Exercise

Rest

Paused

Finished
```

Only one state can exist at any time.

This simplifies both the UI and the AI.

---

# 6. Exercise Lifecycle

Every exercise follows the same flow.

```text id="wrk003"
Pending
      ↓
Started
      ↓
Working Set
      ↓
Rest
      ↓
Next Set
      ↓
Completed
```

The user never sees multiple active exercises simultaneously.

---

# 7. One Exercise Rule

ASTRA always displays **one exercise at a time**.

Visible:

* Exercise name
* Target sets
* Target reps
* Previous performance
* Current set
* Rest timer
* Coaching note

Hidden:

* Future exercises
* Workout analytics
* Chat history
* Nutrition
* Progress graphs

This minimizes distractions during training.

---

# 8. Set Logging

Every completed set records:

* Weight
* Repetitions
* RIR (or RPE, depending on program)
* Completion timestamp
* Notes (optional)

The engine validates the data before saving.

---

# 9. Rest Engine

After each working set:

```text id="wrk004"
Set Complete
      ↓
Rest Timer Starts
      ↓
Countdown
      ↓
Rest Complete
      ↓
Prompt Next Set
```

The user may:

* Skip rest
* Extend rest
* Pause timer

The engine records actual rest duration for future analysis.

---

# 10. Progression Engine

The Workout Engine delegates progression decisions to a deterministic Progression Engine.

Inputs:

* Previous performance
* Target rep range
* Recovery status
* Program rules

Outputs:

* Increase weight
* Maintain weight
* Reduce weight
* Deload

The AI explains the recommendation but does not calculate it.

---

# 11. Exercise Substitutions

When an exercise cannot be performed:

Reasons may include:

* Equipment unavailable
* Injury
* Pain
* Travel

The engine retrieves approved substitutions from the reference database.

Substitutions preserve training intent whenever possible.

---

# 12. Workout Completion

A workout is complete when:

* All required exercises are completed, or
* The user intentionally ends the session.

The engine then generates:

* Total duration
* Total volume
* Exercises completed
* PRs achieved
* Recovery recommendations
* Next scheduled workout

These outputs become available to ASTRA for post-workout coaching.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2
# 📄 08_Workout_Engine.md

# PART 2 / FINAL

---

# 13. Adaptive Progression Engine

## Purpose

The Adaptive Progression Engine determines how the training load should change over time.

Progression is **rule-based**, not AI-generated.

The objective is:

* Progressive overload
* Long-term consistency
* Injury prevention
* Sustainable improvement

---

## Decision Inputs

The engine evaluates:

* Previous workout performance
* Target rep range
* RIR / RPE
* Recovery score
* Missed workouts
* Deload status
* Injury flags

Example

```text id="wrk005"
Previous Session
      ↓
Performance Analysis
      ↓
Recovery Check
      ↓
Progression Rules
      ↓
Recommendation
```

---

# 14. Workout Recovery Integration

The Workout Engine communicates with the Recovery Engine before every session.

Possible outcomes:

```text id="wrk006"
Ready
↓

Normal Workout
```

```text id="wrk007"
Moderate Fatigue
↓

Reduce Volume
```

```text id="wrk008"
Poor Recovery
↓

Recovery Workout
```

The user always has the final decision, but ASTRA explains the recommendation.

---

# 15. Pause & Resume

A workout may be interrupted.

Examples:

* Phone call
* Water break
* Equipment unavailable
* Gym interruption

The engine saves:

* Current exercise
* Current set
* Rest timer
* Workout duration
* Completed sets

When reopened:

```text id="wrk009"
Resume Workout

↓

Continue Exactly Where User Left
```

No information should be lost.

---

# 16. Skip Logic

The engine allows controlled skipping.

### Skip Set

Skip one set.

### Skip Exercise

Skip one exercise.

### End Workout

Finish remaining workout early.

Every skipped action is recorded for analytics and future coaching.

---

# 17. Workout History

Every completed workout stores:

* Date
* Duration
* Exercises
* Sets
* Volume
* Rest times
* Notes
* Completion status

History becomes the foundation for:

* Progress
* AI coaching
* Analytics
* Recovery recommendations

---

# 18. Weekly Planning

At the start of each week, the engine evaluates:

* Scheduled workouts
* Recovery trends
* Missed sessions
* Upcoming constraints

It prepares the week's training schedule before the first workout begins.

---

# 19. Deload Engine

The Deload Engine follows deterministic rules.

Possible triggers:

* Plateau
* High accumulated fatigue
* Multiple poor recovery days
* Manual coach recommendation

A deload modifies:

* Load
* Volume
* Intensity

The AI explains why a deload is recommended.

---

# 20. Travel Mode

When Travel Mode is enabled:

The engine adapts workouts based on:

* Available equipment
* Workout duration
* Environment
* Recovery

Priority is maintaining training consistency rather than maximizing progression.

---

# 21. Workout Summary

At the end of every session, generate:

```text id="wrk010"
Duration

Exercises Completed

Total Volume

Estimated Effort

Personal Records

Coach Summary

Tomorrow's Workout
```

The summary should be concise and actionable.

---

# 22. Failure Recovery

If the application crashes during a workout:

```text id="wrk011"
App Restart
      ↓
Load Active Workout
      ↓
Restore Current Exercise
      ↓
Restore Current Set
      ↓
Restore Rest Timer
      ↓
Continue Session
```

No workout data should be lost.

---

# 23. Performance Targets

| Operation        |  Target |
| ---------------- | ------: |
| Start Workout    | <100 ms |
| Load Exercise    |  <50 ms |
| Log Set          |  <50 ms |
| Start Rest Timer | Instant |
| Resume Workout   | <150 ms |
| Finish Workout   | <200 ms |

The Workout Engine should feel instantaneous during normal use.

---

# 24. Acceptance Criteria

The Workout Engine is complete when:

* Today's workout is selected automatically.
* One exercise is shown at a time.
* Every set is logged reliably.
* Rest timing is tracked accurately.
* Progression follows deterministic rules.
* Workouts can be paused and resumed.
* Offline execution works correctly.
* Workout history is preserved.
* Recovery influences recommendations.
* AI explains, but does not replace, workout logic.

---

# 25. Summary

The Workout Engine is the central execution system of ASTRA.

```text id="wrk012"
Training Program
        ↓
Workout Selection
        ↓
Exercise Execution
        ↓
Set Logging
        ↓
Rest Management
        ↓
Progression
        ↓
Workout Summary
        ↓
History
        ↓
AI Coaching
```

The engine owns all workout decisions.

ASTRA's AI adds explanation, guidance, and personalization on top of a deterministic training foundation.

---

# END OF DOCUMENT

**Document:** 08_Workout_Engine.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `09_AI_Tool_Specification.md`
