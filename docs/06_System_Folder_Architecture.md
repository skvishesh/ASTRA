
# 📄 06_System_Folder_Architecture.md

# PART 1 / FINAL

---

# ASTRA

# System Folder Architecture

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

This document defines the complete folder structure for ASTRA.

Objectives:

* Consistent organization
* High maintainability
* AI-friendly development
* Clear ownership
* Low coupling
* High cohesion

Every file in the project must have a logical home.

---

# 2. Architecture Philosophy

The project is organized by **domain**, not by file type.

❌ Avoid

```text
components/
pages/
hooks/
utils/
services/
```

These folders eventually become dumping grounds.

---

✅ Prefer

```text
Workout/
Recovery/
Nutrition/
Coach/
Progress/
```

Each domain owns everything it needs.

---

# 3. High-Level Repository Structure

```text
ASTRA/
│
├── apps/
├── backend/
├── packages/
├── docs/
├── prompts/
├── infrastructure/
├── scripts/
├── assets/
├── tests/
├── .github/
├── .vscode/
├── README.md
├── LICENSE
└── .gitignore
```

Each top-level folder has one responsibility.

---

# 4. Apps

The `apps` directory contains user-facing applications.

```text
apps/
│
├── mobile/
├── web/
└── admin/
```

---

## mobile

Primary Android application.

Contains:

* UI
* Navigation
* Local state
* Offline cache
* Device integrations

---

## web

Desktop companion.

Used primarily for:

* Reviewing analytics
* Viewing history
* Administrative tasks
* Future expansion

---

## admin

Internal tooling.

Examples:

* Database inspection
* Development utilities
* Debug panels

Never exposed in production.

---

# 5. Backend

```text
backend/
│
├── api/
├── services/
├── repositories/
├── ai/
├── database/
├── middleware/
├── jobs/
├── config/
├── shared/
└── tests/
```

---

## api

Responsibilities

* Controllers
* Request handling
* Response formatting

No business logic.

---

## services

Business logic only.

Examples

```text
WorkoutService

RecoveryService

NutritionService

CoachService

MemoryService
```

---

## repositories

Responsible for database access.

No calculations.

No business decisions.

Only persistence.

---

## ai

Contains:

* AI Orchestrator
* Prompt Builder
* Tool Router
* Provider Layer
* Context Builder
* Memory Retrieval

---

## database

Contains:

* Schema
* Migrations
* Seed data
* Query helpers

---

## middleware

Examples

* Authentication
* Validation
* Logging
* Rate limiting
* Exception handling

---

## jobs

Background workers.

Examples

* Weekly reports
* Backup
* Analytics generation
* Sync retries

---

## config

Application configuration.

Environment loading.

Feature flags.

Constants.

---

## shared

Reusable backend utilities.

Examples

* Date helpers
* Validation utilities
* Error types
* Logging utilities

---

# 6. Packages

Packages contain reusable code shared across applications.

```text
packages/
│
├── ui/
├── types/
├── analytics/
├── voice/
├── config/
└── utils/
```

---

## ui

Reusable UI components.

Examples

* Buttons
* Cards
* Dialogs
* Progress bars
* Exercise cards

---

## types

Shared TypeScript types.

Single source of truth.

---

## analytics

Shared analytics calculations.

Example

* Volume calculations
* Estimated 1RM
* Weekly consistency

---

## voice

Voice abstraction layer.

Responsible for:

* Speech-to-text
* Text-to-speech
* Voice command parsing

---

## config

Shared application configuration.

---

## utils

Pure utility functions.

No business logic.

---

# 7. Documentation

All project documentation lives inside:

```text
docs/
```

Suggested organization:

```text
docs/
│
├── architecture/
├── backend/
├── frontend/
├── ai/
├── database/
├── roadmap/
└── decisions/
```

Documentation should evolve alongside the codebase.

---

# 8. Prompts

```text
prompts/
│
├── identity/
├── workout/
├── recovery/
├── nutrition/
├── planning/
├── education/
├── memory/
└── weekly-review/
```

Each prompt category has one responsibility.

Avoid a single monolithic system prompt.

---

# 9. Assets

```text
assets/
│
├── icons/
├── images/
├── sounds/
├── animations/
├── exercise-images/
└── illustrations/
```

Assets should be organized by purpose, not by file extension.

---

# 10. Tests

Testing mirrors the application structure.

```text
tests/
│
├── unit/
├── integration/
├── e2e/
├── ai/
└── performance/
```

Every major module should have corresponding tests.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2

# 📄 06_System_Folder_Architecture.md

# PART 2 / FINAL

---

# 11. Mobile Application Structure

The mobile application follows **Domain-Driven Design (DDD)**.

```text id="w8m3fd"
apps/
└── mobile/
    │
    ├── src/
    │
    ├── app/
    ├── domains/
    ├── shared/
    ├── navigation/
    ├── hooks/
    ├── services/
    ├── state/
    ├── theme/
    ├── assets/
    └── tests/
```

---

## app/

Application bootstrap.

Contains:

* App initialization
* Dependency registration
* Global providers
* Error boundaries

---

## domains/

Every feature has its own domain.

Example

```text id="d2x7pg"
domains/

Workout/

Recovery/

Nutrition/

Coach/

Progress/

Settings/

Profile/
```

Nothing outside the domain should know its internal implementation.

---

# Domain Structure

Every domain follows the same layout.

```text id="c58wgr"
Workout/

components/

screens/

hooks/

services/

state/

types/

utils/

tests/
```

This consistency makes navigation predictable for both developers and AI coding agents.

---

# 12. Backend AI Structure

```text id="7gjq1w"
backend/

ai/

orchestrator/

providers/

tools/

memory/

reasoning/

prompts/

context/

intent/

response/
```

---

## orchestrator/

Coordinates the entire AI request lifecycle.

Never contains provider-specific logic.

---

## providers/

Individual AI providers.

Example

```text id="u41kfw"
GeminiProvider

OpenAIProvider

LocalProvider
```

Every provider implements the same interface.

---

## tools/

Contains all callable AI tools.

Example

```text id="92meqw"
getTodayWorkout()

logSet()

recommendProgression()

searchMemory()
```

---

## memory/

Responsible for:

* Retrieval
* Ranking
* Storage
* Updates

---

## reasoning/

Transforms structured outputs into natural coaching responses.

---

## prompts/

Stores modular prompt templates.

One file per responsibility.

---

## context/

Builds the final context passed to the LLM.

---

## intent/

Intent classification.

Maps user requests to internal actions.

---

## response/

Formats AI responses before sending them to the frontend.

---

# 13. Database Folder

```text id="jxg5er"
backend/

database/

schema/

migrations/

repositories/

seed/

queries/

backups/
```

---

## schema/

Database definitions.

---

## migrations/

Schema evolution.

Never edit old migrations.

Always create new ones.

---

## repositories/

Database access layer.

One repository per domain.

---

## seed/

Reference data.

Examples:

* Exercise library
* Progression rules
* Exercise substitutions

---

## queries/

Complex reusable SQL queries.

---

## backups/

Database backup scripts.

Not backup files.

---

# 14. Infrastructure

```text id="7lq5gw"
infrastructure/

docker/

firebase/

postgres/

sqlite/

monitoring/

deployment/
```

Each infrastructure technology remains isolated.

---

# 15. Scripts

Automation scripts.

```text id="gnbptl"
scripts/

setup/

backup/

import/

export/

maintenance/
```

Scripts should never contain business logic.

---

# 16. Naming Conventions

## Folders

Use:

```text id="3jv41i"
Workout

Recovery

Nutrition
```

Avoid:

```text id="5uwn9d"
workoutStuff

misc

helpers2
```

---

## Files

Use descriptive names.

Examples

```text id="pwj84t"
WorkoutService.ts

RecoveryCalculator.ts

ExerciseRepository.ts

CoachResponseBuilder.ts
```

Avoid abbreviations unless universally understood.

---

# 17. Dependency Rules

Dependencies must flow downward only.

```text id="9dwyqp"
UI
   ↓
Application
   ↓
Domain
   ↓
Services
   ↓
Repositories
   ↓
Database
```

Never reverse this direction.

Examples of invalid dependencies:

* Repository importing UI.
* Database importing AI.
* Prompt importing frontend components.

---

# 18. Shared Code Policy

Code should be moved into `shared/` or `packages/` only after it is genuinely reused.

Do not create shared modules "just in case."

---

# 19. Documentation Policy

Every major folder should include a README describing:

* Purpose
* Ownership
* Responsibilities
* Public interfaces
* Dependencies

This helps both developers and AI agents understand the project quickly.

---

# 20. Future Expansion

The folder architecture should support future additions without major restructuring.

Potential future modules:

* Camera Analysis
* Wearables
* Mobility
* Injury Assessment
* Smart Recommendations
* Team Coaching (if ever needed)

Each future capability should become its own domain rather than being merged into existing ones.

---

# 21. Acceptance Criteria

The architecture is considered complete when:

* Every file has a logical location.
* Domains are isolated.
* Shared code is minimized.
* Dependencies remain one-directional.
* Backend and frontend responsibilities are clearly separated.
* AI modules remain independent from storage implementation.
* New features can be added without restructuring the project.

---

# 22. Summary

ASTRA follows a **domain-driven, modular architecture**.

```text id="5t0nqx"
Apps
   ↓
Domains
   ↓
Services
   ↓
Repositories
   ↓
Database
```

This structure improves:

* Maintainability
* Scalability
* Testability
* AI-assisted development
* Long-term project evolution

It also ensures that both human developers and AI coding agents can navigate the project with minimal ambiguity.

---

# END OF DOCUMENT

**Document:** 06_System_Folder_Architecture.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `07_Prompt_Architecture.md`

