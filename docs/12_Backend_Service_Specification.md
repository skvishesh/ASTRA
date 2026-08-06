Perfect.

We're now entering the **implementation layer**.

Everything we've designed so far (AI, Database, API, UI, Workout Engine) now gets connected through backend services.

This is the document that tells an AI coding agent exactly **where business logic belongs**.

---

# 📄 12_Backend_Service_Specification.md

# PART 1 / 2

---

# ASTRA

# Backend Service Specification

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

This document defines the backend service layer of ASTRA.

The Service Layer contains all business logic.

Responsibilities include:

* Executing business rules
* Coordinating repositories
* Validating workflows
* Calling AI tools
* Managing transactions
* Returning domain objects

Services **must not** contain presentation logic or direct SQL queries.

---

# 2. Backend Architecture

```text id="svc001"
Frontend
      ↓
API Controllers
      ↓
Application Services
      ↓
Repositories
      ↓
Database
```

Only the Service Layer understands business rules.

---

# 3. Service Design Principles

Every service must:

* Have one responsibility.
* Be independently testable.
* Avoid circular dependencies.
* Use dependency injection.
* Return domain models rather than raw SQL results.

Business logic should never exist in:

* Controllers
* Repositories
* Frontend
* AI prompts

---

# 4. Service Categories

```text id="svc002"
Authentication

Profile

Workout

Recovery

Nutrition

Progress

Coach

Memory

Planning

Analytics

Settings

Synchronization

Backup
```

Each category owns one primary service.

---

# 5. AuthenticationService

## Responsibilities

* Login
* Logout
* Token validation
* Session management
* Refresh tokens

Public Methods

```text id="svc003"
login()

logout()

refreshToken()

validateSession()
```

This service should never interact with workout logic.

---

# 6. ProfileService

## Responsibilities

* Update profile
* Retrieve profile
* Manage goals
* Update preferences

Public Methods

```text id="svc004"
getProfile()

updateProfile()

updateGoals()

updatePreferences()
```

---

# 7. WorkoutService

The most important backend service.

Responsibilities:

* Start workout
* Resume workout
* Pause workout
* Complete workout
* Select today's workout
* Coordinate progression
* Trigger workout summary

Public Methods

```text id="svc005"
getTodayWorkout()

startWorkout()

pauseWorkout()

resumeWorkout()

finishWorkout()
```

WorkoutService orchestrates multiple services but does not perform low-level database operations directly.

---

# 8. ExerciseService

Responsibilities

* Load current exercise
* Complete exercise
* Replace exercise
* Retrieve exercise history

Methods

```text id="svc006"
getCurrentExercise()

finishExercise()

replaceExercise()

getExerciseHistory()
```

---

# 9. SetService

Handles all set-level operations.

Methods

```text id="svc007"
logSet()

updateSet()

deleteSet()

undoLastSet()
```

Every operation should execute within a transaction where necessary.

---

# 10. RecoveryService

Responsibilities

* Readiness calculation
* Recovery logging
* Recovery recommendations

Methods

```text id="svc008"
calculateReadiness()

getRecovery()

updateRecovery()
```

Recovery calculations remain deterministic.

---

# 11. NutritionService

Responsibilities

* Meal logging
* Daily nutrition summary
* Protein tracking

Methods

```text id="svc009"
logMeal()

getNutritionSummary()

getProteinStatus()
```

Version 1 focuses on coaching-relevant metrics rather than detailed calorie tracking.

---

# 12. ProgressService

Responsibilities

* Workout history
* Strength trends
* Estimated 1RM
* Consistency calculations

Methods

```text id="svc010"
getDashboard()

calculateProgress()

getExerciseProgress()

detectPlateau()
```

Progress calculations should be reusable across mobile, web, and AI.

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2 (CoachService, MemoryService, PlanningService, AnalyticsService, SyncService, BackupService, Dependency Rules, Transactions, Acceptance Criteria)
# 📄 12_Backend_Service_Specification.md

# PART 2 / 2 (FINAL)

---

# 13. CoachService

## Purpose

The `CoachService` is the central orchestration layer between the application and ASTRA's AI system.

It does **not** contain LLM logic.

Instead, it coordinates:

* Intent Detection
* Context Builder
* Memory Service
* Tool Layer
* Prompt Builder
* AI Provider
* Response Validation

---

## Responsibilities

* Build AI request context
* Select required tools
* Invoke the AI Orchestrator
* Validate AI responses
* Store relevant memories
* Return structured coaching responses

---

## Public Methods

```text id="svc011"
chat()

voiceChat()

buildContext()

generateResponse()

validateResponse()
```

---

# 14. MemoryService

## Purpose

Manages ASTRA's long-term memory.

Memory is separate from chat history.

---

## Responsibilities

* Search memories
* Save memories
* Update memories
* Archive memories
* Generate embeddings
* Rank relevance

---

## Public Methods

```text id="svc012"
searchMemory()

saveMemory()

updateMemory()

archiveMemory()

generateEmbedding()
```

---

# 15. PlanningService

## Purpose

Manages workout scheduling and long-term planning.

---

## Responsibilities

* Weekly planning
* Missed workout recovery
* Travel mode
* Deload scheduling
* Goal planning

---

## Public Methods

```text id="svc013"
generateWeeklyPlan()

rescheduleWorkout()

enableTravelMode()

recommendDeload()

updateTrainingPlan()
```

---

# 16. AnalyticsService

## Purpose

Generates higher-level insights from historical data.

---

## Responsibilities

* Weekly review
* Monthly review
* Long-term trends
* Consistency reports
* Volume analysis

---

## Public Methods

```text id="svc014"
generateWeeklyReview()

generateMonthlyReview()

analyzeConsistency()

calculateTrainingVolume()
```

---

# 17. SettingsService

## Responsibilities

* Theme
* Voice
* Units
* Notifications
* AI Provider
* User preferences

---

## Public Methods

```text id="svc015"
getSettings()

updateSettings()

resetSettings()
```

---

# 18. SyncService

## Purpose

Synchronizes local SQLite data with PostgreSQL.

---

## Responsibilities

* Queue synchronization
* Conflict detection
* Conflict resolution
* Retry failed operations
* Upload changes
* Download updates

---

## Public Methods

```text id="svc016"
enqueueChange()

sync()

retryFailedOperations()

resolveConflict()
```

Synchronization should run in the background without interrupting workouts.

---

# 19. BackupService

## Responsibilities

* Create backup
* Restore backup
* Validate backup
* List backups

---

## Public Methods

```text id="svc017"
createBackup()

restoreBackup()

validateBackup()

listBackups()
```

Every restore operation should create a safety backup first.

---

# 20. Service Communication Rules

Services communicate only through public interfaces.

```text id="svc018"
WorkoutService
       │
       ├── ExerciseService
       ├── SetService
       ├── ProgressService
       └── RecoveryService
```

Avoid circular dependencies.

Example:

❌ `WorkoutService` → `ProgressService` → `WorkoutService`

Instead, move shared logic into a dedicated domain service if necessary.

---

# 21. Dependency Rules

Allowed:

```text id="svc019"
Controller
      ↓
Service
      ↓
Repository
```

Not Allowed:

* Controller → Repository
* Controller → Database
* Service → UI
* Repository → Service
* AI Provider → Database

This separation keeps responsibilities clear and testable.

---

# 22. Transaction Management

The following operations require transactions:

* Start workout
* Finish workout
* Log set
* Replace exercise
* Restore backup
* Synchronize data

Example:

```text id="svc020"
Begin Transaction
        ↓
Save Set
        ↓
Update Workout
        ↓
Update Progress
        ↓
Commit
```

If any step fails:

```text id="svc021"
Rollback
```

---

# 23. Error Handling

Every service should return structured domain errors.

Examples

```text id="svc022"
WorkoutNotFound

ActiveWorkoutExists

RecoveryDataMissing

InvalidProgression

MemoryNotFound

BackupFailed
```

Errors should be meaningful and actionable.

---

# 24. Logging

Each service should log:

* Request ID
* Service name
* Method
* Duration
* Success/Failure
* Error code (if applicable)

Sensitive user information must never be logged unnecessarily.

---

# 25. Testing Strategy

Every service requires:

### Unit Tests

Verify business logic.

---

### Integration Tests

Verify repository interactions.

---

### Failure Tests

Verify:

* Invalid input
* Missing records
* Rollback behavior
* Conflict handling

---

### Performance Tests

Ensure services meet documented response targets.

---

# 26. Performance Targets

| Service                             |               Target |
| ----------------------------------- | -------------------: |
| WorkoutService                      |              <100 ms |
| ExerciseService                     |               <50 ms |
| SetService                          |               <50 ms |
| RecoveryService                     |               <75 ms |
| MemoryService                       |              <150 ms |
| CoachService (excluding AI latency) |              <100 ms |
| SyncService                         |           Background |
| BackupService                       | Depends on data size |

---

# 27. Acceptance Criteria

The backend service layer is complete when:

* Business logic exists only in services.
* Repositories contain only persistence logic.
* Controllers remain thin.
* Transactions protect critical workflows.
* Services communicate through public interfaces.
* Circular dependencies are eliminated.
* All services are independently testable.

---

# 28. Summary

The backend service layer is the operational core of ASTRA.

```text id="svc023"
Frontend
      ↓
Controllers
      ↓
Services
      ↓
Repositories
      ↓
Database

             +

CoachService
      ↓
AI Orchestrator
      ↓
Tool Layer
      ↓
LLM
```

This architecture keeps the application modular, testable, and scalable while ensuring that deterministic business logic remains separate from AI reasoning.

---

# END OF DOCUMENT

**Document:** 12_Backend_Service_Specification.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `13_Prompt_Library.md`

