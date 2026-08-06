

# 📄 05_UI_UX_Specification.md

# PART 1 / FINAL

---

# ASTRA

# UI / UX Specification

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

This document defines the visual and interaction design of ASTRA.

It covers:

* User experience philosophy
* Navigation
* Screen layouts
* Workout mode
* Voice interaction
* Accessibility
* Interaction principles

It does **not** define implementation details or component code.

---

# 2. Design Philosophy

ASTRA is **not** a social fitness application.

ASTRA is **not** a bodybuilding tracker.

ASTRA is **not** a calorie counter.

ASTRA is a **professional AI coaching system**.

Every screen must answer one question:

> **"What is the user trying to accomplish right now?"**

If a UI element does not help answer that question, it should not exist.

---

# 3. Core UX Principles

## Principle 1

One primary action per screen.

Example:

Workout Screen

Primary action:

```text id="4jphb6"
Complete Current Exercise
```

Nothing should compete with it.

---

## Principle 2

Reduce cognitive load.

The user should never wonder:

* What do I do next?
* Which button should I press?
* Which exercise is next?

ASTRA always guides the next action.

---

## Principle 3

Minimal interaction.

The fewer taps required, the better.

Examples:

Good

```text id="jzjlwm"
Tap

↓

Log Set
```

Better

```text id="vtp5xw"
Voice

↓

"Completed"

↓

Next Set
```

---

## Principle 4

Context-aware interface.

The interface changes depending on what the user is doing.

Examples:

Before workout

Mission dashboard.

During workout

Workout mode.

Rest

Rest screen.

Conversation

Coach interface.

Progress review

Analytics.

---

## Principle 5

Professional appearance.

No:

* Fireworks
* Badges
* XP points
* Coins
* Streak flames
* Cartoon animations

ASTRA behaves like a professional coach.

---

# 4. Navigation

The application uses five permanent tabs.

```text id="4jlwmk"
🏠 Home

🏋 Workout

📈 Progress

🧠 Astra

⚙ Settings
```

No hidden navigation.

No hamburger menu.

---

# 5. Home Screen

Purpose

Mission Control.

The Home screen should answer:

> What should I do today?

---

## Layout

```text id="jmb82z"
Greeting

↓

Today's Workout

↓

Recovery Score

↓

Today's Mission

↓

Quick Actions

↓

Coach Note

↓

Daily Metrics
```

---

# Home Sections

### Greeting

Example

> Good Morning.

> Ready for Upper Day?

---

### Today's Workout Card

Displays

* Workout name
* Estimated duration
* Focus
* Readiness
* Start button

---

### Recovery Card

Displays

* Sleep
* Fatigue
* Readiness Score

---

### Mission Card

Displays

Today's objective.

Example

```text id="kp9xq9"
Improve Pull-up Strength
```

---

### Daily Metrics

Shows

* Protein
* Water
* Weight
* Steps
* Sleep

No charts.

Only today's status.

---

### Coach Note

One recommendation.

Example

> Focus on controlled eccentric reps today.

Only one note.

---

# 6. Workout Mode

Workout Mode is the signature feature of ASTRA.

When started,

the interface changes completely.

---

Everything unrelated disappears.

```text id="yh92gm"
Workout

↓

Current Exercise

↓

Rest

↓

Next Exercise

↓

Finish
```

No dashboard.

No chat history.

No analytics.

No distractions.

---

# 7. Workout State Machine

The interface changes according to the workout state.

```text id="z9bfj8"
Ready

↓

Warm-up

↓

Exercise

↓

Rest

↓

Exercise

↓

Cooldown

↓

Summary
```

Only one state is visible.

---

# 8. Exercise Screen

One exercise only.

Displays

* Exercise Name
* Exercise Image
* Target Sets
* Target Reps
* Tempo
* Rest
* Previous Performance
* Today's Goal

---

## Layout

```text id="txkl8w"
Bench Press

━━━━━━━━━━

4 × 6–8

━━━━━━━━━━

Previous

60 × 8

━━━━━━━━━━

Today's Goal

60 × 9

━━━━━━━━━━

Start Set
```

Everything else is hidden.

---

# 9. Logging Interface

Supported methods

* Voice
* Buttons
* Text

All produce identical data.

Logging should require the minimum possible interaction.

---

# 10. Voice Experience

Voice is not a separate mode.

Voice is another way to control the application.

Examples

> Start workout

> Next exercise

> Completed

> Start rest

> Skip exercise

The same backend processes all commands.

---

# 11. Rest Screen

Purpose

Provide recovery between sets without distractions.

Displays

```text id="u0r7ja"
Timer

↓

Coach Tip

↓

Next Exercise Preview

↓

Skip Rest

↓

Extend Rest
```

Nothing more.

---

# 12. Summary Screen

After finishing a workout:

Display

* Duration
* Exercises completed
* Total volume
* Personal records
* Coach summary
* Tomorrow's workout

The summary should be readable in under 30 seconds.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2
# 📄 05_UI_UX_Specification.md

# PART 2 / FINAL

---

# 13. ASTRA Screen

## Purpose

The ASTRA screen is the primary communication interface between the user and the AI coach.

Unlike traditional AI chat applications, this screen is **context-aware**.

The conversation should always reflect what the user is currently doing.

Examples:

Before workout

* Today's plan
* Recovery
* Motivation
* Schedule

During workout

* Current exercise
* Technique
* Rest
* Progression

After workout

* Recovery
* Nutrition
* Review
* Tomorrow's plan

---

## Layout

```text id="7fybnd"
──────────────────────────────

ASTRA

──────────────────────────────

Conversation

──────────────────────────────

Suggested Actions

──────────────────────────────

🎤 Voice

⌨ Text

──────────────────────────────
```

---

## Suggested Actions

Examples

```text id="vjlwm1"
Today's workout

Increase bench?

Check recovery

Protein status

Explain RIR

Tomorrow's workout
```

These suggestions change depending on context.

---

# 14. Progress Screen

## Purpose

Display meaningful progress rather than overwhelming statistics.

---

## Sections

### Body Metrics

Displays

* Weight
* Body Fat %
* Waist
* Progress Photos (future)

---

### Strength

Displays

* Estimated 1RM
* Personal Records
* Strength Trend

---

### Workout History

Displays

* Previous sessions
* Weekly consistency
* Monthly consistency

---

### Pull-up Progress

Dedicated section.

Because one of the major goals is achieving the first strict pull-up.

Displays

* Assistance used
* Dead hang duration
* Negative reps
* Band progression
* First unassisted repetition milestone

---

### Recovery Trends

Displays

* Sleep
* Fatigue
* Recovery score

---

### Nutrition

Displays

* Protein consistency
* Water consistency
* Weight trend

---

# 15. Settings Screen

Purpose

Configuration only.

Never place coaching functionality here.

---

## Categories

```text id="jjr3h9"
Account

AI

Voice

Notifications

Appearance

Backup

Privacy

About
```

---

# 16. Design Language

The interface should communicate professionalism.

Avoid:

* Neon colors
* Excessive gradients
* Cartoon illustrations
* Flashy animations

Preferred style:

* Clean
* Spacious
* Minimal
* Athletic
* High contrast
* Functional

---

# 17. Typography

Typography hierarchy:

```text id="rfk81w"
Heading

↓

Section Title

↓

Body

↓

Caption
```

Readable typography takes priority over decorative fonts.

---

# 18. Color System

Primary colors should communicate function.

Examples

Green

* Success
* Completed

Blue

* Information

Orange

* Attention

Red

* Errors
* Warnings

Color should never be the only indicator of state.

---

# 19. Accessibility

ASTRA must support:

* Large touch targets
* Screen readers
* Voice navigation
* High contrast mode
* One-hand operation where practical

The interface should remain usable during workouts when the user is fatigued.

---

# 20. Animation Guidelines

Animations should communicate state.

Good examples:

* Exercise completion
* Rest timer transition
* Voice listening indicator
* Screen transition after workout

Avoid decorative animations that do not improve usability.

---

# 21. Empty States

Every screen should handle missing data gracefully.

Example:

Workout History

Instead of an empty list:

> "Complete your first workout to begin tracking progress."

Provide a clear next action.

---

# 22. Error States

Errors should be understandable.

Instead of:

```text id="6u3nj8"
500 Internal Server Error
```

Display:

> "Couldn't connect to ASTRA. Your workout is still available offline."

The user should know:

* What happened.
* Whether their data is safe.
* What to do next.

---

# 23. Offline Experience

If internet connectivity is lost:

Continue supporting:

* Workout execution
* Set logging
* Recovery tracking
* Progress viewing
* Local history

Unavailable features should clearly indicate they require connectivity without interrupting the workout.

---

# 24. Performance Goals

| Action                               |  Target |
| ------------------------------------ | ------: |
| Home Screen                          | <500 ms |
| Workout Screen                       | Instant |
| Exercise Transition                  | <100 ms |
| Log Set                              |  <50 ms |
| AI Screen Open                       | <300 ms |
| Chat Response (excluding AI latency) | <100 ms |

The application should feel responsive even on mid-range Android devices.

---

# 25. Acceptance Criteria

The UI/UX specification is complete when:

* Navigation is intuitive.
* Workout mode is distraction-free.
* One exercise is displayed at a time.
* Voice and text workflows are consistent.
* Accessibility requirements are met.
* Offline usage remains fully functional for workouts.
* Every screen has a single primary purpose.

---

# 26. Summary

ASTRA is designed around **states**, not just screens.

```text id="9ykb7m"
Home
    ↓
Workout
    ↓
Rest
    ↓
Summary
    ↓
Recovery
    ↓
Planning
```

The interface adapts to the user's current activity, ensuring that only relevant information is presented at any given time.

This approach minimizes distractions and creates a focused coaching experience.

---

# END OF DOCUMENT

**Document:** 05_UI_UX_Specification.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `06_System_Folder_Architecture.md`
