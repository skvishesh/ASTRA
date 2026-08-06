
---

# 📄 04_API_Architecture.md

# PART 1 / FINAL

---

# ASTRA

# API Architecture

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

This document defines the complete API architecture for ASTRA.

It specifies:

* API philosophy
* endpoint design
* communication standards
* request lifecycle
* authentication
* validation
* error handling
* versioning
* service boundaries

This document does **not** define database tables or business logic.

Those are covered in separate documents.

---

# 2. API Philosophy

The API exists to expose business capabilities, **not database tables**.

Clients should request actions such as:

* Start workout
* Log set
* Finish workout
* Get today's workout
* Ask ASTRA

They should **not** manipulate database structures directly.

---

## Guiding Principles

### Principle 1

APIs represent **business actions**, not CRUD whenever possible.

Good

```text
POST /workouts/start
```

Better than

```text
POST /workout_sessions
```

because it represents intent.

---

### Principle 2

The frontend never accesses the database.

Everything flows through backend services.

```text
Frontend
      ↓
REST API
      ↓
Service Layer
      ↓
Repository
      ↓
Database
```

---

### Principle 3

Every endpoint has one responsibility.

Example

```text
POST /workouts/log-set
```

Only logs one set.

It should never:

* update nutrition
* calculate analytics
* modify goals

---

### Principle 4

Responses should be predictable.

Every response follows a consistent format.

---

# 3. API Layers

```text
Mobile App
      ↓
API Gateway
      ↓
Controllers
      ↓
Application Services
      ↓
Repositories
      ↓
Database
```

Each layer has exactly one responsibility.

---

# 4. Request Lifecycle

Every request follows this pipeline.

```text
Request
   ↓
Authentication
   ↓
Validation
   ↓
Controller
   ↓
Application Service
   ↓
Repository
   ↓
Database
   ↓
Response Builder
   ↓
Client
```

No layer should bypass another.

---

# 5. API Modules

The API is divided into business modules.

```text
/auth

/profile

/workouts

/exercises

/recovery

/nutrition

/progress

/memory

/chat

/settings

/system
```

Each module owns its own endpoints.

---

# 6. Authentication Module

Responsibilities

* Login
* Logout
* Token refresh
* Session validation

Authentication should remain independent of workout logic.

---

# 7. Profile Module

Responsibilities

* User profile
* Goals
* Preferences
* Schedule
* Training settings

Example endpoints

```text
GET  /profile

PUT  /profile

PUT  /profile/preferences

PUT  /profile/goals
```

---

# 8. Workout Module

Core API of ASTRA.

Example endpoints

```text
GET  /workouts/today

POST /workouts/start

POST /workouts/pause

POST /workouts/resume

POST /workouts/finish
```

These endpoints manage the workout lifecycle.

---

# 9. Exercise Module

Example

```text
GET /exercises/current

POST /exercises/complete

POST /exercises/replace

GET /exercises/history
```

Each endpoint focuses on one exercise operation.

---

# 10. Set Logging Module

Example

```text
POST /sets/log

PUT /sets/update

DELETE /sets/delete

POST /sets/undo
```

This module must be optimized for speed because it is used repeatedly during workouts.

---

# 11. Recovery Module

Responsibilities

* Sleep
* Fatigue
* Readiness
* Recovery logs

Example endpoints

```text
GET /recovery/today

POST /recovery/update

GET /recovery/history
```

---

# 12. Nutrition Module

Example

```text
POST /nutrition/log

GET /nutrition/today

GET /nutrition/protein
```

Nutrition APIs should return structured summaries rather than raw calculations.

---

# END OF PART 1

# 📄 04_API_Architecture.md

# PART 2 / FINAL

---

# 13. Progress Module

## Purpose

The Progress Module provides all historical and analytical information related to the user's training performance.

Unlike the Workout Module, this module never modifies workout data.

It only retrieves processed information.

---

## Responsibilities

* Workout history
* Exercise history
* Strength trends
* Estimated 1RM
* Weekly volume
* Monthly volume
* Consistency metrics
* Personal records

---

## Example Endpoints

```text
GET /progress/dashboard

GET /progress/workouts

GET /progress/exercises/{exerciseId}

GET /progress/personal-records

GET /progress/strength-trends
```

---

# 14. Memory Module

## Purpose

Provides controlled access to ASTRA's long-term memory.

The frontend never accesses memory storage directly.

All memory operations go through dedicated APIs.

---

## Responsibilities

* Retrieve relevant memories
* Save new memories
* Update existing memories
* Archive memories
* Search memories

---

## Example Endpoints

```text
GET /memory/search

POST /memory/save

PUT /memory/update

POST /memory/archive
```

---

# 15. AI Chat Module

## Purpose

Acts as the communication gateway between the frontend and the AI Orchestrator.

The Chat Module never performs reasoning.

It only:

* receives requests
* forwards them
* streams responses
* returns structured outputs

---

## Example Endpoints

```text
POST /chat/message

POST /chat/voice

GET /chat/history

DELETE /chat/history
```

---

# AI Request Pipeline

```text
User

↓

Chat API

↓

AI Orchestrator

↓

Context Builder

↓

Memory Retrieval

↓

Tool Engine

↓

Rule Engine

↓

LLM

↓

Structured Response

↓

Frontend
```

---

# 16. Settings Module

Responsibilities

* Theme
* Voice settings
* Notification preferences
* AI provider
* Backup settings
* Units

---

## Example Endpoints

```text
GET /settings

PUT /settings

PUT /settings/theme

PUT /settings/voice
```

---

# 17. System Module

Provides maintenance functionality.

Examples

```text
POST /system/backup

POST /system/restore

GET /system/status

GET /system/version

POST /system/export
```

---

# 18. Request Format

Every API request should use structured JSON.

Example

```json
{
  "exerciseId": "bench_press",
  "weight": 60,
  "reps": 8,
  "rir": 2
}
```

---

# 19. Response Format

Every successful response follows one standard.

```json
{
  "success": true,
  "message": "Set logged successfully.",
  "data": {}
}
```

---

Every failed response follows one standard.

```json
{
  "success": false,
  "error": {
    "code": "WORKOUT_NOT_ACTIVE",
    "message": "No active workout found."
  }
}
```

No endpoint should invent its own response structure.

---

# 20. Validation

Every request passes through validation before reaching business logic.

Validation includes:

* Required fields
* Data types
* Value ranges
* Authentication
* Authorization
* Business rule validation

Example

Invalid

```json
{
  "weight": -20
}
```

Rejected before reaching the service layer.

---

# 21. API Versioning

The API must be versioned.

Example

```text
/api/v1/workouts/start

/api/v1/chat/message

/api/v1/progress/dashboard
```

Future versions must not break existing clients unexpectedly.

---

# 22. Rate Limiting

Apply rate limits where appropriate.

Examples

High Priority

* Chat API
* Authentication
* Export

Lower Priority

* Progress retrieval
* Exercise history
* Dashboard

Workout logging should not be aggressively rate-limited because rapid set logging is a normal use case.

---

# 23. Authentication & Authorization

Protected endpoints require authentication.

Examples

Protected

* Workout
* Recovery
* Nutrition
* Progress
* Memory
* Settings

Public (if any)

* Health check
* Application version

Authorization should follow the principle of least privilege.

---

# 24. Performance Targets

| Endpoint                     |  Target |
| ---------------------------- | ------: |
| Start Workout                | <100 ms |
| Log Set                      |  <50 ms |
| Finish Workout               | <150 ms |
| Dashboard                    | <300 ms |
| Memory Search                | <200 ms |
| Chat (excluding LLM latency) | <100 ms |

---

# 25. Logging

Each API request should log:

* Request ID
* Timestamp
* Endpoint
* User ID
* Duration
* Status Code

Sensitive data such as tokens and secrets must never be written to logs.

---

# 26. Error Handling

Every error must provide:

* Error code
* Human-readable message
* Recoverability (when applicable)

Examples

```text
AUTH_INVALID_TOKEN

WORKOUT_NOT_ACTIVE

INVALID_SET_DATA

MEMORY_NOT_FOUND

SYNC_FAILED
```

Avoid generic "Unknown Error" responses whenever possible.

---

# 27. API Design Rules

Every endpoint must:

* Have one responsibility.
* Return consistent responses.
* Validate input.
* Use service-layer business logic.
* Never access the database directly.
* Be independently testable.
* Be documented.

---

# 28. Acceptance Criteria

The API architecture is complete when:

* Modules are clearly separated.
* Request and response formats are standardized.
* Validation occurs before business logic.
* Authentication protects sensitive endpoints.
* Business logic remains inside services.
* The API supports the documented frontend workflows.
* Performance targets are achievable.

---

# 29. Summary

The ASTRA API is organized around business capabilities rather than raw database operations.

```text
Frontend
     ↓
REST API
     ↓
Controllers
     ↓
Application Services
     ↓
Repositories
     ↓
Database
```

This architecture keeps the frontend simple, the backend maintainable, and the AI independent from storage implementation.

---

# END OF DOCUMENT

**Document:** 04_API_Architecture.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

