Perfect.

This document defines **every reusable UI building block** of ASTRA.

The goal is simple:

> **Build once, reuse everywhere.**

This prevents duplicate components, inconsistent UI, and makes AI-generated code much more maintainable.

---

# 📄 10_Frontend_Component_Specification.md

# PART 1 / FINAL

---

# ASTRA

# Frontend Component Specification

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

This document defines the reusable frontend component library used throughout ASTRA.

It specifies:

* Component philosophy
* Component hierarchy
* Reusability rules
* State ownership
* Communication patterns
* UI consistency

This document defines components, **not screens**.

Screens are composed from these reusable components.

---

# 2. Component Philosophy

Every UI element should be reusable.

Avoid creating components for a single screen unless there is a clear reason.

Goals:

* Consistency
* Reusability
* Testability
* Accessibility
* Predictability

---

# 3. Component Hierarchy

```text id="cmp001"
Application

↓

Screens

↓

Sections

↓

Components

↓

Primitive UI
```

Example

```text id="cmp002"
Workout Screen

↓

Exercise Card

↓

Set Row

↓

Button

↓

Text
```

---

# 4. Component Categories

```text id="cmp003"
Layout

Navigation

Workout

Recovery

Nutrition

Progress

Coach

Input

Feedback

Charts

Dialogs
```

Each category owns its own reusable components.

---

# 5. Layout Components

## AppLayout

Purpose

Provides the root layout structure.

Responsibilities

* Safe area
* Navigation container
* Theme
* Global providers

---

## ScreenContainer

Standard wrapper used for every screen.

Responsibilities

* Padding
* Scroll behavior
* Background
* Responsive spacing

---

## Section

Groups related information.

Example

```text id="cmp004"
Recovery

Workout

Nutrition
```

---

## Card

Reusable information container.

Examples

* Recovery Card
* Workout Card
* Progress Card

Cards should be composable rather than specialized.

---

# 6. Navigation Components

## Bottom Navigation

Five permanent tabs.

```text id="cmp005"
Home

Workout

Progress

Astra

Settings
```

---

## Header

Displays:

* Title
* Back button (when required)
* Context actions

---

## Breadcrumb (Future)

Reserved for future desktop/web experience.

Not required for Version 1 mobile.

---

# 7. Workout Components

## Workout Card

Displays:

* Workout Name
* Duration
* Focus
* Start Button

---

## Exercise Card

Displays:

* Exercise Name
* Previous Performance
* Target Sets
* Target Reps
* Tempo

One exercise only.

---

## Set Row

Displays:

* Set Number
* Weight
* Reps
* RIR
* Completion State

Each row represents one working set.

---

## Rest Timer

Displays:

* Remaining Time
* Skip Button
* Extend Button

Supports pause and resume.

---

## Workout Summary Card

Displays:

* Duration
* Volume
* Exercises
* PRs
* Coach Summary

---

# 8. Recovery Components

## Recovery Score Card

Displays:

* Recovery Score
* Readiness Status
* Recommendation

---

## Sleep Card

Displays:

* Hours
* Quality
* Trend

---

## Fatigue Card

Displays:

* Fatigue Level
* Recent Trend

---

# 9. Nutrition Components

## Protein Card

Displays:

* Current Intake
* Goal
* Remaining

---

## Water Card

Displays:

* Current Intake
* Goal
* Progress

---

## Nutrition Summary

Displays:

* Calories
* Protein
* Water

Version 1 keeps nutrition intentionally simple.

---

# 10. Progress Components

## Personal Record Card

Displays:

* Exercise
* Best Lift
* Date

---

## Strength Trend Card

Displays:

* Estimated 1RM
* Trend
* Recent Progress

---

## Workout History Card

Displays:

* Date
* Workout
* Duration
* Completion Status

---

## Consistency Card

Displays:

* Weekly
* Monthly
* Percentage

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2
Perfect.

This completes **10_Frontend_Component_Specification.md**.

---

# 📄 10_Frontend_Component_Specification.md

# PART 2 / FINAL

---

# 11. Coach Components

## Coach Message

Purpose

Displays a single ASTRA response.

Types

* Recommendation
* Information
* Warning
* Question
* Summary

Every message should have a consistent layout.

---

## Suggested Action Chips

Purpose

Provide quick actions based on the current context.

Examples

```text id="cmp006"
Today's Workout

Increase Bench?

Protein Status

Recovery

Next Exercise
```

These change dynamically.

---

## Voice Indicator

Displays:

* Listening
* Processing
* Speaking
* Idle

Voice status must always be obvious.

---

## Coach Summary Card

Used after:

* Workout
* Weekly review
* Monthly review

Contains:

* Summary
* Key observations
* Recommended next step

---

# 12. Input Components

## Primary Button

Used for the main action on every screen.

Examples

* Start Workout
* Complete Set
* Finish Workout

Only one primary button should exist per screen.

---

## Secondary Button

Used for optional actions.

Examples

* Skip Rest
* Extend Rest
* View History

---

## Icon Button

Examples

* Back
* Settings
* Microphone
* Search

Should include accessible labels.

---

## Text Input

Used for:

* Notes
* Search
* Chat

Supports validation and clear error messages.

---

## Number Input

Used for:

* Weight
* Repetitions
* Protein
* Water

Should support fast numeric entry.

---

# 13. Feedback Components

## Loading Indicator

Displayed during:

* AI response generation
* Data synchronization
* Initial loading

Loading indicators should communicate progress without blocking unnecessarily.

---

## Success Banner

Examples

* Workout saved.
* Goal updated.
* Backup completed.

Automatically dismisses after a short duration.

---

## Error Banner

Displays:

* Human-readable message
* Optional retry action

Avoid technical jargon.

---

## Empty State

Examples

* No workout history.
* No meals logged.
* No recovery data.

Always provide a meaningful next action.

---

# 14. Dialog Components

## Confirmation Dialog

Used before irreversible actions.

Examples

* End Workout
* Delete Workout
* Restore Backup

---

## Selection Dialog

Examples

* Choose Exercise
* Select Goal
* Pick AI Provider

---

## Bottom Sheet

Used for quick contextual actions.

Examples

* Exercise options
* Rest options
* Workout options

Preferred over full-screen dialogs for small tasks.

---

# 15. Chart Components

Version 1 keeps charts simple.

Supported:

* Line Chart
* Bar Chart
* Progress Ring

Avoid excessive visualization.

The focus is actionable information rather than analytics for its own sake.

---

# 16. Component Communication

Components communicate only through defined interfaces.

```text id="cmp007"
Screen
    ↓
Section
    ↓
Component
    ↓
Primitive UI
```

Components should not directly manipulate global application state.

---

# 17. State Ownership

State should exist at the lowest practical level.

Examples:

Local Component State

* Input value
* Expanded/collapsed section
* Loading spinner

Domain State

* Active workout
* Recovery
* Nutrition
* Progress

Global State

* Authentication
* Theme
* User profile
* AI session

---

# 18. Accessibility

Every component must support:

* Screen readers
* Large touch targets
* Keyboard navigation (where applicable)
* High contrast
* Voice interaction

Interactive elements should include descriptive accessibility labels.

---

# 19. Component Testing

Every reusable component requires:

### Rendering Tests

Verify correct display.

---

### Interaction Tests

Verify:

* Button presses
* Input handling
* State updates

---

### Accessibility Tests

Verify:

* Labels
* Focus order
* Touch targets

---

### Snapshot Tests

Used sparingly to detect unintended visual regressions.

---

# 20. Naming Convention

Use descriptive PascalCase names.

Examples

```text id="cmp008"
WorkoutCard

ExerciseCard

RecoveryScoreCard

CoachMessage

RestTimer

ProteinCard

PrimaryButton
```

Avoid generic names such as:

```text id="cmp009"
Card2

Widget

Helper

Box

Thing
```

---

# 21. Future Expansion

The component system should support future additions such as:

* Camera preview
* Wearable widgets
* Live heart-rate display
* Mobility assessment
* AI coaching overlays
* Desktop-specific layouts

New components should extend the existing design language rather than introducing a separate visual style.

---

# 22. Acceptance Criteria

The frontend component library is complete when:

* Components are reusable.
* Responsibilities are clearly separated.
* State ownership is well-defined.
* Accessibility is supported.
* Components are independently testable.
* Naming is consistent.
* Screens can be composed entirely from reusable building blocks.

---

# 23. Summary

ASTRA's frontend is built from modular, reusable components.

```text id="cmp010"
Primitive UI
      ↓
Reusable Components
      ↓
Sections
      ↓
Screens
      ↓
Application
```

This architecture ensures:

* Consistency
* Maintainability
* Faster development
* Easier testing
* Better AI-assisted code generation

The component library becomes the foundation for every screen in the application.

---

# END OF DOCUMENT

**Document:** 10_Frontend_Component_Specification.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `11_Database_Schema.md`

---
