Perfect.

This is the **most important backend document** in the entire project.

Everything in ASTRA eventually becomes data.

So the schema must be clean, normalized, scalable, and offline-friendly.

From here onward, I'm writing this as if it were going directly into production.

---

# 📄 11_Database_Schema.md

# PART 1 / 6

---

# ASTRA

# Database Schema

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

This document defines the complete relational database schema for ASTRA.

It specifies:

* Tables
* Columns
* Data types
* Relationships
* Primary keys
* Foreign keys
* Indexes
* Constraints
* Naming conventions

Implementation-specific migration scripts are documented separately.

---

# 2. Database Philosophy

The schema follows these principles:

* Normalize until it hurts performance, then optimize deliberately.
* One source of truth per entity.
* Soft-delete only where recovery is useful.
* Audit important changes.
* Use UUIDs for primary keys.
* Store timestamps in UTC.

---

# 3. Naming Convention

### Tables

Use plural nouns.

Examples

```text id="db001"
users

workouts

exercises

exercise_sets

recovery_logs
```

---

### Columns

Use snake_case.

Examples

```text id="db002"
created_at

updated_at

exercise_id

workout_id
```

---

### Primary Keys

Every table uses

```text id="db003"
id UUID PRIMARY KEY
```

---

### Foreign Keys

Examples

```text id="db004"
user_id

exercise_id

workout_id

goal_id
```

---

# 4. Entity Relationship Overview

```text id="db005"
User
 │
 ├──────── Goals
 │
 ├──────── Workouts
 │            │
 │            ├──── Workout Exercises
 │            │            │
 │            │            └──── Exercise Sets
 │
 ├──────── Recovery Logs
 │
 ├──────── Nutrition Logs
 │
 ├──────── Coach Memory
 │
 ├──────── Progress Metrics
 │
 └──────── Chat Sessions
```

---

# 5. Core Tables

The first version contains the following core domains.

```text id="db006"
users

profiles

goals

workouts

workout_exercises

exercise_sets

recovery_logs

nutrition_logs

coach_memory

progress_metrics

chat_sessions

chat_messages

settings

exercise_library

exercise_substitutions
```

Additional tables may be added in future versions without breaking existing relationships.

---

# 6. users

Purpose

Represents the authenticated owner of the application.

Version 1 is designed for a single user but retains a user table to simplify future expansion.

---

Columns

| Column        | Type      | Notes       |
| ------------- | --------- | ----------- |
| id            | UUID      | Primary Key |
| email         | TEXT      | Unique      |
| display_name  | TEXT      | Required    |
| created_at    | TIMESTAMP | UTC         |
| updated_at    | TIMESTAMP | UTC         |
| last_login_at | TIMESTAMP | Nullable    |

Indexes

```text id="db007"
PRIMARY KEY(id)

UNIQUE(email)
```

---

# 7. profiles

Purpose

Stores fitness-specific profile information.

---

Columns

| Column                  | Type      |
| ----------------------- | --------- |
| id                      | UUID      |
| user_id                 | UUID      |
| height_cm               | INTEGER   |
| current_weight          | DECIMAL   |
| target_weight           | DECIMAL   |
| body_fat_percent        | DECIMAL   |
| activity_level          | TEXT      |
| preferred_training_time | TEXT      |
| experience_level        | TEXT      |
| created_at              | TIMESTAMP |
| updated_at              | TIMESTAMP |

Relationship

```text id="db008"
User

1

↓

1

Profile
```

---

# 8. goals

Purpose

Stores long-term fitness goals.

---

Columns

| Column      | Type      |
| ----------- | --------- |
| id          | UUID      |
| user_id     | UUID      |
| title       | TEXT      |
| description | TEXT      |
| status      | TEXT      |
| priority    | INTEGER   |
| target_date | DATE      |
| created_at  | TIMESTAMP |
| updated_at  | TIMESTAMP |

Examples

* First Pull-up
* Reach 12% Body Fat
* Bench 100 kg

---

# 9. exercise_library

Purpose

Reference table.

Read only.

Contains every supported exercise.

---

Columns

| Column           | Type      |
| ---------------- | --------- |
| id               | UUID      |
| name             | TEXT      |
| muscle_group     | TEXT      |
| equipment        | TEXT      |
| movement_pattern | TEXT      |
| exercise_type    | TEXT      |
| instructions     | TEXT      |
| created_at       | TIMESTAMP |

This table rarely changes.

---

# 10. exercise_substitutions

Purpose

Defines approved substitutions.

---

Relationship

```text id="db009"
Bench Press

↓

Machine Chest Press

↓

Push-up
```

---

Columns

| Column        | Type |
| ------------- | ---- |
| id            | UUID |
| exercise_id   | UUID |
| substitute_id | UUID |
| reason        | TEXT |

---

# 11. workouts

Purpose

Represents one workout session.

---

Columns

| Column           | Type      |
| ---------------- | --------- |
| id               | UUID      |
| user_id          | UUID      |
| workout_name     | TEXT      |
| workout_type     | TEXT      |
| scheduled_date   | DATE      |
| started_at       | TIMESTAMP |
| completed_at     | TIMESTAMP |
| duration_minutes | INTEGER   |
| status           | TEXT      |
| total_volume     | DECIMAL   |
| notes            | TEXT      |

Status

```text id="db010"
Planned

Started

Paused

Completed

Cancelled
```

---

# 12. workout_exercises

Purpose

Represents every exercise inside a workout.

Relationship

```text id="db011"
Workout

↓

Workout Exercise

↓

Exercise Library
```

Columns

| Column         | Type    |
| -------------- | ------- |
| id             | UUID    |
| workout_id     | UUID    |
| exercise_id    | UUID    |
| exercise_order | INTEGER |
| target_sets    | INTEGER |
| target_reps    | TEXT    |
| target_rir     | DECIMAL |
| rest_seconds   | INTEGER |
| status         | TEXT    |

---

────────────────────────────────────────

END OF DOCUMENT PART 1

Next: Part 2 (Exercise Sets, Workout History, Recovery Logs, Nutrition Logs, Foreign Keys, Constraints)
Perfect.

This is where the database begins to capture the data that makes ASTRA intelligent.

---

# 📄 11_Database_Schema.md

# PART 2 / 6

---

# 13. exercise_sets

## Purpose

Stores every individual set performed during a workout.

This is one of the most frequently written tables in the system.

Every completed set becomes permanent historical data.

---

## Relationship

```text id="db012"
Workout
      ↓
Workout Exercise
      ↓
Exercise Set
```

---

## Columns

| Column              | Type      |
| ------------------- | --------- |
| id                  | UUID      |
| workout_exercise_id | UUID      |
| set_number          | INTEGER   |
| set_type            | TEXT      |
| planned_weight      | DECIMAL   |
| actual_weight       | DECIMAL   |
| planned_reps        | INTEGER   |
| actual_reps         | INTEGER   |
| planned_rir         | DECIMAL   |
| actual_rir          | DECIMAL   |
| rest_seconds        | INTEGER   |
| completed           | BOOLEAN   |
| completed_at        | TIMESTAMP |
| notes               | TEXT      |

---

## Set Types

```text id="db013"
Warm-up

Working

Back-off

Drop

Failure

AMRAP
```

---

## Indexes

```text id="db014"
PRIMARY KEY(id)

INDEX(workout_exercise_id)

INDEX(completed_at)
```

---

# 14. workout_history

## Purpose

Provides a lightweight historical summary for fast retrieval.

Instead of recalculating summaries repeatedly, important values are stored after workout completion.

---

## Columns

| Column           | Type      |
| ---------------- | --------- |
| id               | UUID      |
| workout_id       | UUID      |
| total_sets       | INTEGER   |
| total_reps       | INTEGER   |
| total_volume     | DECIMAL   |
| workout_duration | INTEGER   |
| personal_records | INTEGER   |
| average_rest     | INTEGER   |
| perceived_effort | DECIMAL   |
| created_at       | TIMESTAMP |

---

# 15. recovery_logs

## Purpose

Stores daily recovery information.

Only one recovery record should exist per day.

---

## Columns

| Column          | Type      |
| --------------- | --------- |
| id              | UUID      |
| user_id         | UUID      |
| log_date        | DATE      |
| sleep_hours     | DECIMAL   |
| sleep_quality   | INTEGER   |
| fatigue         | INTEGER   |
| soreness        | INTEGER   |
| stress          | INTEGER   |
| readiness_score | INTEGER   |
| notes           | TEXT      |
| created_at      | TIMESTAMP |

---

## Constraints

```text id="db015"
UNIQUE(user_id, log_date)
```

Prevents duplicate daily recovery entries.

---

# 16. nutrition_logs

## Purpose

Stores daily nutrition information.

Version 1 intentionally tracks only essential coaching metrics.

---

## Columns

| Column        | Type      |
| ------------- | --------- |
| id            | UUID      |
| user_id       | UUID      |
| log_date      | DATE      |
| calories      | INTEGER   |
| protein       | DECIMAL   |
| carbohydrates | DECIMAL   |
| fats          | DECIMAL   |
| water_liters  | DECIMAL   |
| meals_logged  | INTEGER   |
| created_at    | TIMESTAMP |

---

## Constraints

```text id="db016"
UNIQUE(user_id, log_date)
```

---

# 17. body_metrics

## Purpose

Tracks body composition changes over time.

---

## Columns

| Column           | Type      |
| ---------------- | --------- |
| id               | UUID      |
| user_id          | UUID      |
| measurement_date | DATE      |
| weight           | DECIMAL   |
| body_fat_percent | DECIMAL   |
| waist_cm         | DECIMAL   |
| chest_cm         | DECIMAL   |
| arm_cm           | DECIMAL   |
| thigh_cm         | DECIMAL   |
| notes            | TEXT      |
| created_at       | TIMESTAMP |

---

# 18. progress_metrics

## Purpose

Stores calculated performance indicators.

These values are generated by backend services rather than entered manually.

---

## Columns

| Column              | Type      |
| ------------------- | --------- |
| id                  | UUID      |
| user_id             | UUID      |
| metric_name         | TEXT      |
| metric_value        | DECIMAL   |
| metric_date         | DATE      |
| calculation_version | TEXT      |
| created_at          | TIMESTAMP |

---

## Examples

```text id="db017"
Estimated 1RM

Weekly Volume

Monthly Volume

Workout Consistency

Recovery Trend
```

---

# 19. Foreign Key Relationships

```text id="db018"
users.id
      ↓
profiles.user_id

users.id
      ↓
goals.user_id

users.id
      ↓
workouts.user_id

workouts.id
      ↓
workout_exercises.workout_id

exercise_library.id
      ↓
workout_exercises.exercise_id

workout_exercises.id
      ↓
exercise_sets.workout_exercise_id
```

Every foreign key should enforce referential integrity.

---

# 20. Constraints

Examples of database constraints:

```text id="db019"
actual_weight >= 0

actual_reps >= 0

sleep_hours BETWEEN 0 AND 24

protein >= 0

water_liters >= 0

duration_minutes >= 0
```

Validation should exist both in the application layer and the database.

---

# 21. Transactions

The following operations must execute within a transaction:

* Start workout
* Finish workout
* Log set
* Update progression
* Restore backup
* Synchronize changes

If any step fails, the entire transaction must roll back.

---

# 22. Audit Fields

Every mutable table should include:

```text id="db020"
created_at

updated_at
```

Optional fields where appropriate:

```text id="db021"
created_by

updated_by

deleted_at
```

These support future auditing and soft-delete strategies.

---

────────────────────────────────────────

END OF DOCUMENT PART 2

Next: Part 3 (Coach Memory, Chat System, Settings, Active Workout State, Sync Queue, Offline Storage, Index Strategy)
Perfect.

Now we define the tables that make ASTRA feel intelligent rather than just being a workout tracker.

These tables power memory, conversations, offline recovery, and synchronization.

---

# 📄 11_Database_Schema.md

# PART 3 / 6

---

# 23. coach_memory

## Purpose

Stores long-term memories that ASTRA uses to personalize coaching.

This is **not** a chat history table.

It stores only information that should persist across conversations.

Examples:

* Preferred workout time
* Training goals
* Shoulder injury history
* Equipment availability
* Coaching preferences

---

## Memory Categories

```text id="db022"
Profile

Goal

Preference

Workout

Recovery

Nutrition

Injury

Coach Decision

Custom
```

---

## Columns

| Column      | Type      |
| ----------- | --------- |
| id          | UUID      |
| user_id     | UUID      |
| memory_type | TEXT      |
| topic       | TEXT      |
| title       | TEXT      |
| content     | TEXT      |
| importance  | INTEGER   |
| confidence  | DECIMAL   |
| source      | TEXT      |
| created_at  | TIMESTAMP |
| updated_at  | TIMESTAMP |
| archived    | BOOLEAN   |

---

## Memory Importance

```text id="db023"
1

Low

↓

5

Critical
```

High-importance memories should always be considered first during retrieval.

---

## Indexes

```text id="db024"
INDEX(user_id)

INDEX(memory_type)

INDEX(topic)

INDEX(importance)
```

---

# 24. memory_embeddings

## Purpose

Stores vector embeddings for semantic memory retrieval.

The actual memory remains in the `coach_memory` table.

Embeddings are regenerated whenever memory content changes.

---

## Columns

| Column             | Type      |
| ------------------ | --------- |
| id                 | UUID      |
| memory_id          | UUID      |
| embedding_provider | TEXT      |
| embedding_model    | TEXT      |
| vector             | VECTOR    |
| updated_at         | TIMESTAMP |

---

Relationship

```text id="db025"
Coach Memory

↓

Memory Embedding
```

---

# 25. chat_sessions

## Purpose

Groups conversations into sessions.

Each session may represent:

* General coaching
* Workout
* Nutrition
* Recovery
* Planning

---

## Columns

| Column       | Type      |
| ------------ | --------- |
| id           | UUID      |
| user_id      | UUID      |
| title        | TEXT      |
| session_type | TEXT      |
| started_at   | TIMESTAMP |
| ended_at     | TIMESTAMP |
| active       | BOOLEAN   |

---

# 26. chat_messages

## Purpose

Stores conversation history.

Unlike coach memory, chat history is temporary conversational context.

---

## Columns

| Column      | Type      |
| ----------- | --------- |
| id          | UUID      |
| session_id  | UUID      |
| role        | TEXT      |
| message     | TEXT      |
| token_count | INTEGER   |
| created_at  | TIMESTAMP |

---

## Roles

```text id="db026"
System

User

Assistant

Tool
```

---

# 27. settings

## Purpose

Stores application configuration.

---

## Columns

| Column                | Type      |
| --------------------- | --------- |
| id                    | UUID      |
| user_id               | UUID      |
| theme                 | TEXT      |
| language              | TEXT      |
| units                 | TEXT      |
| ai_provider           | TEXT      |
| voice_enabled         | BOOLEAN   |
| notifications_enabled | BOOLEAN   |
| backup_enabled        | BOOLEAN   |
| created_at            | TIMESTAMP |
| updated_at            | TIMESTAMP |

---

# 28. active_workout

## Purpose

Stores the current workout state for crash recovery and resume functionality.

Only one active workout should exist per user.

---

## Columns

| Column               | Type      |
| -------------------- | --------- |
| id                   | UUID      |
| user_id              | UUID      |
| workout_id           | UUID      |
| current_exercise_id  | UUID      |
| current_set_number   | INTEGER   |
| rest_timer_remaining | INTEGER   |
| workout_state        | TEXT      |
| updated_at           | TIMESTAMP |

---

## Constraint

```text id="db027"
UNIQUE(user_id)
```

This guarantees only one active workout.

---

# 29. sync_queue

## Purpose

Tracks local changes waiting to be synchronized with the cloud.

This table is essential for offline-first operation.

---

## Columns

| Column      | Type      |
| ----------- | --------- |
| id          | UUID      |
| entity_type | TEXT      |
| entity_id   | UUID      |
| operation   | TEXT      |
| payload     | JSON      |
| created_at  | TIMESTAMP |
| synced      | BOOLEAN   |
| retry_count | INTEGER   |

---

## Operations

```text id="db028"
INSERT

UPDATE

DELETE
```

---

# 30. backup_history

## Purpose

Stores metadata about backup operations.

---

## Columns

| Column          | Type      |
| --------------- | --------- |
| id              | UUID      |
| user_id         | UUID      |
| backup_type     | TEXT      |
| backup_location | TEXT      |
| created_at      | TIMESTAMP |
| status          | TEXT      |

---

# 31. Index Strategy

Indexes should support the application's most common queries.

Recommended indexes:

```text id="db029"
workouts(user_id)

workouts(scheduled_date)

exercise_sets(workout_exercise_id)

recovery_logs(user_id, log_date)

nutrition_logs(user_id, log_date)

chat_messages(session_id)

coach_memory(user_id, memory_type)

active_workout(user_id)

sync_queue(synced)
```

Avoid excessive indexing that slows writes.

---

# 32. Data Retention

Retention policy:

| Data            | Policy                                 |
| --------------- | -------------------------------------- |
| Workout History | Permanent                              |
| Coach Memory    | Permanent unless archived              |
| Chat History    | Configurable                           |
| Sync Queue      | Remove after successful sync           |
| Backups         | Versioned according to backup settings |

---

# 33. Soft Delete Policy

Soft delete should be used selectively.

Suitable candidates:

* Goals
* Coach memory
* Chat sessions

Not recommended for:

* Exercise sets
* Workout history
* Recovery logs

Historical training data should remain intact.

---

────────────────────────────────────────

END OF DOCUMENT PART 3

Next: Part 4 (Migration Strategy, SQLite vs PostgreSQL Differences, ER diagrams, Full relationship matrix, Normalization rules, Performance optimization)
Perfect.

This part defines how the database evolves over time and how SQLite and PostgreSQL work together. A clean migration strategy is essential because changing schemas after users have data is much harder than designing it correctly now.

---

# 📄 11_Database_Schema.md

# PART 4 / 6

---

# 34. Migration Strategy

## Purpose

Database schemas will evolve throughout ASTRA's lifetime.

Every schema change must be handled through versioned migrations.

Never modify an existing migration after it has been applied.

---

## Migration Rules

Each migration should:

* Have a unique sequential version.
* Be reversible where practical.
* Execute inside a transaction.
* Be idempotent when appropriate.
* Be documented.

---

## Example Naming

```text id="db030"
001_initial_schema

002_add_recovery_logs

003_add_memory_embeddings

004_add_progress_metrics
```

---

## Migration Flow

```text id="db031"
Current Version
       ↓
Pending Migrations
       ↓
Validation
       ↓
Execute Migration
       ↓
Verification
       ↓
Update Schema Version
```

---

# 35. Schema Version Table

## Purpose

Tracks the database schema version.

---

## schema_versions

| Column      | Type      |
| ----------- | --------- |
| id          | UUID      |
| version     | TEXT      |
| description | TEXT      |
| applied_at  | TIMESTAMP |

Only the migration system should modify this table.

---

# 36. SQLite vs PostgreSQL

ASTRA uses both databases for different purposes.

## SQLite

Purpose

* Primary runtime database
* Offline operation
* Fast local reads and writes

Characteristics

* Embedded
* Local
* Offline-first
* Single-user

---

## PostgreSQL

Purpose

* Cloud synchronization
* Long-term storage
* Analytics
* Backup

Characteristics

* Centralized
* Reliable
* Scalable

---

## Synchronization Rules

SQLite is the runtime source while offline.

PostgreSQL becomes the cloud source after synchronization completes successfully.

Neither database should overwrite newer valid data without conflict resolution.

---

# 37. Relationship Matrix

```text id="db032"
users
   │
   ├── profiles
   ├── goals
   ├── workouts
   ├── recovery_logs
   ├── nutrition_logs
   ├── body_metrics
   ├── coach_memory
   ├── progress_metrics
   ├── chat_sessions
   ├── settings
   ├── active_workout
   └── backup_history

workouts
   │
   ├── workout_exercises
   │        │
   │        └── exercise_sets
   │
   └── workout_history

exercise_library
   │
   └── exercise_substitutions

coach_memory
   │
   └── memory_embeddings

chat_sessions
   │
   └── chat_messages
```

---

# 38. Normalization

The schema targets **Third Normal Form (3NF)**.

Guidelines:

* Store each fact once.
* Eliminate redundant columns.
* Avoid repeating groups.
* Separate reference data from transactional data.

Denormalization should only occur after measuring a real performance bottleneck.

---

# 39. Computed Values

Some values should **not** be stored permanently.

Examples:

* Current workout streak
* Total lifetime volume
* Weekly consistency
* Monthly averages

These should be calculated when needed or cached if profiling shows a performance benefit.

---

# 40. Derived Tables

Some summaries may be materialized for performance.

Examples:

```text id="db033"
daily_progress_summary

weekly_training_summary

monthly_training_summary
```

These tables are generated automatically and should never be edited directly.

---

# 41. Transactions

Critical operations must remain atomic.

Example:

```text id="db034"
Finish Workout
      ↓
Save Exercise Sets
      ↓
Update Workout
      ↓
Generate Workout History
      ↓
Update Progress Metrics
      ↓
Commit
```

If any step fails:

```text id="db035"
Rollback Entire Transaction
```

Partial completion is not acceptable.

---

# 42. Locking Strategy

During an active workout:

* Only one active workout record per user.
* Prevent duplicate workout starts.
* Prevent simultaneous modification of the same active workout.

This reduces synchronization conflicts and protects workout integrity.

---

# 43. Performance Optimization

Optimize for the application's primary workflows.

Priority:

1. Log set
2. Resume workout
3. Open today's workout
4. Load dashboard
5. Search memory
6. Generate reports

Less common administrative operations should not compromise these core experiences.

---

# 44. Integrity Rules

The database must enforce:

* Foreign keys
* Required fields
* Unique constraints
* Valid ranges
* Referential integrity

Business rules remain in the service layer, but the database provides the final safeguard against invalid data.

---

────────────────────────────────────────

END OF DOCUMENT PART 4

Next: Part 5 (Backup & Restore, Sync Conflict Resolution, Indexing Strategy, Security, Auditing, Future Expansion)
Perfect.

This part defines how ASTRA protects your data over years of use. Since this app is meant to become your long-term fitness operating system, backup, synchronization, auditing, and security are as important as the workout logic itself.

---

# 📄 11_Database_Schema.md

# PART 5 / 6

---

# 45. Backup Strategy

## Purpose

The backup system ensures that years of workout history, AI memories, and personal progress can always be recovered.

Backups should be:

* Automatic
* Versioned
* Verifiable
* Restorable

---

## Backup Types

```text id="db036"
Automatic Daily

↓

Manual Backup

↓

Pre-Migration Backup

↓

Pre-Restore Backup
```

---

## Backup Contents

Every backup should include:

* User profile
* Goals
* Workout history
* Exercise sets
* Recovery logs
* Nutrition logs
* Coach memory
* Progress metrics
* Settings

Temporary cache tables should **not** be included.

---

# 46. Restore Strategy

Restore operations must never overwrite existing data without confirmation.

Restore flow:

```text id="db037"
Select Backup

↓

Validate

↓

Create Safety Backup

↓

Restore

↓

Integrity Check

↓

Complete
```

If validation fails, the restore must be cancelled.

---

# 47. Synchronization Conflict Resolution

Conflicts occur when both the local and cloud databases contain different versions of the same record.

Resolution priority:

1. Newer timestamp
2. Higher version number
3. Manual review (if required)

---

## Conflict States

```text id="db038"
No Conflict

↓

Automatic Merge

↓

Manual Resolution
```

Every conflict should be logged for debugging.

---

# 48. Synchronization Audit

Each synchronization event records:

| Field              | Description       |
| ------------------ | ----------------- |
| Sync ID            | Unique identifier |
| Started At         | UTC timestamp     |
| Finished At        | UTC timestamp     |
| Records Uploaded   | Count             |
| Records Downloaded | Count             |
| Conflicts          | Count             |
| Result             | Success / Failed  |

These records simplify troubleshooting.

---

# 49. Security

The database must protect sensitive information.

Guidelines:

* Encrypt authentication secrets.
* Never store plaintext passwords.
* Use parameterized queries.
* Enforce least-privilege access.
* Validate all external input.

Sensitive personal fitness data should never be exposed through logs.

---

# 50. Audit Logging

Important changes should generate audit records.

Examples:

* Goal updates
* Workout plan changes
* Coach memory edits
* Backup restores
* Settings changes

Audit entries should contain:

* Action
* Timestamp
* User
* Previous value (when appropriate)
* New value

---

# 51. Index Review Strategy

Indexes should be reviewed periodically.

Remove indexes that:

* Are never used
* Slow write-heavy operations
* Duplicate existing indexes

Add indexes only after performance profiling.

---

# 52. Archiving

Some information may be archived instead of deleted.

Examples:

* Completed goals
* Old chat sessions
* Archived memories

Archived records remain searchable if requested.

Workout history should never be archived automatically.

---

# 53. Data Integrity Verification

Periodic integrity checks should verify:

* Foreign key consistency
* Missing references
* Duplicate records
* Invalid timestamps
* Corrupted synchronization queues

If problems are detected, ASTRA should report them before attempting repairs.

---

# 54. Monitoring Metrics

The backend should monitor:

* Database size
* Query latency
* Synchronization success rate
* Backup success rate
* Failed transactions
* Active workout recovery events

These metrics help maintain long-term reliability.

---

# 55. Future Schema Expansion

The schema is designed to support future domains without breaking existing tables.

Examples:

```text id="db039"
Wearables

Camera Analysis

Mobility Tests

Heart Rate

Blood Pressure

Body Scan

Exercise Video Analysis

Supplement Tracking
```

Each new capability should introduce new tables rather than modifying stable historical structures whenever possible.

---

────────────────────────────────────────

END OF DOCUMENT PART 5

Next: Part 6 (Final ER model, Data flow, Database standards, Acceptance criteria, Schema governance, Final summary and completion)
# 📄 11_Database_Schema.md

# PART 6 / 6 (FINAL)

---

# 56. Entity Relationship Diagram (Logical)

The following logical diagram represents the primary relationships between the core entities.

```text
                                 users
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
      profiles                  goals                  settings
          │
          │
      workouts ───────────────┐
          │                   │
          │                   └──── workout_history
          │
          ▼
workout_exercises
          │
          ▼
   exercise_sets

exercise_library ───── exercise_substitutions

users
  │
  ├──── recovery_logs
  ├──── nutrition_logs
  ├──── body_metrics
  ├──── progress_metrics
  ├──── coach_memory ───── memory_embeddings
  ├──── active_workout
  ├──── backup_history
  └──── chat_sessions ───── chat_messages

sync_queue (local synchronization layer)
```

---

# 57. Database Data Flow

The database follows a deterministic lifecycle.

```text id="db040"
User Action
      ↓
Frontend
      ↓
API
      ↓
Validation
      ↓
Business Service
      ↓
Repository
      ↓
SQLite
      ↓
Sync Queue
      ↓
PostgreSQL
      ↓
Analytics
      ↓
AI Context
```

Business logic never exists inside the database.

---

# 58. Database Standards

Every new table must follow the same standards.

### Required Fields

```text id="db041"
id

created_at

updated_at
```

---

### Recommended Fields

```text id="db042"
user_id

notes

status

version
```

---

### Naming Rules

Use:

* snake_case
* plural table names
* UUID primary keys
* UTC timestamps

Avoid:

* abbreviated column names
* mixed naming styles
* nullable fields unless justified

---

# 59. Query Standards

Repositories should:

* Use parameterized queries.
* Avoid `SELECT *`.
* Retrieve only required columns.
* Support pagination where appropriate.
* Keep transactions short.

Long-running analytical queries should execute outside critical workout operations.

---

# 60. Repository Pattern

Each domain owns its own repository.

```text id="db043"
WorkoutRepository

RecoveryRepository

NutritionRepository

MemoryRepository

ProgressRepository

ChatRepository

SettingsRepository
```

Repositories:

* Read data.
* Write data.
* Never contain business rules.

---

# 61. Data Access Rules

Only repositories communicate directly with the database.

```text id="db044"
Frontend

↓

API

↓

Services

↓

Repositories

↓

Database
```

The following are **not allowed**:

* Frontend → Database
* AI → Database
* UI → SQL
* Services bypassing repositories

---

# 62. Database Governance

Any schema modification must satisfy the following checklist:

* Migration created.
* Backward compatibility reviewed.
* Foreign keys validated.
* Performance impact evaluated.
* Documentation updated.
* Tests updated.

No schema change is complete until documentation and tests are updated.

---

# 63. Acceptance Criteria

The schema is considered complete when:

* All core entities are defined.
* Relationships are normalized.
* Primary and foreign keys are enforced.
* Transactions protect critical operations.
* Offline synchronization is supported.
* Historical workout data is immutable.
* AI memory is stored separately from chat history.
* Performance targets remain achievable.
* Backup and recovery are fully supported.

---

# 64. Final Architecture Summary

The schema is organized into independent domains.

```text id="db045"
Identity
      │
      ▼
Profile
      │
      ▼
Workout
      │
      ▼
Recovery
      │
      ▼
Nutrition
      │
      ▼
Progress
      │
      ▼
Memory
      │
      ▼
Chat
      │
      ▼
Settings
```

Each domain owns its own data while remaining connected through well-defined relationships.

---

# 65. Schema Evolution Policy

Version 1 establishes the foundation.

Future versions should:

* Prefer adding new tables over changing existing historical tables.
* Preserve backward compatibility whenever practical.
* Avoid destructive migrations.
* Version all schema changes.
* Maintain migration history indefinitely.

This ensures long-term stability as ASTRA evolves.

---

# 66. Closing Notes

The database schema is the foundation of the ASTRA platform.

It has been designed to support:

* Offline-first operation
* AI-assisted coaching
* Long-term fitness history
* Deterministic workout execution
* Reliable synchronization
* Scalable future expansion

Every higher-level system—API, AI, Workout Engine, Analytics, and UI—depends on this schema being stable, consistent, and well-defined.

---

# DOCUMENT METRICS

**Tables Defined:** 16 Core Tables + Supporting Tables

**Primary Domains:**

* Identity
* Profile
* Goals
* Workout
* Recovery
* Nutrition
* Progress
* Memory
* Chat
* Settings
* Synchronization
* Backup

**Database Type:**

* SQLite (Offline Runtime)
* PostgreSQL (Cloud Synchronization)

**Schema Version:** 1.0.0

---

# END OF DOCUMENT

**Document:** 11_Database_Schema.md
**Version:** 1.0.0
**Status:** ✅ COMPLETE

**Next Document:** `12_Backend_Service_Specification.md`

