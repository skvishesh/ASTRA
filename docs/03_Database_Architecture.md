

# 📄 03_Database_Architecture.md

# PART 1 / FINAL

---

# ASTRA

# Database Architecture

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

This document defines the overall database architecture of ASTRA.

It explains:

* how data is stored
* where data is stored
* synchronization strategy
* offline-first architecture
* caching
* backups
* data ownership
* scalability

This document **does not define individual tables**.

Tables are defined later in **11_Database_Schema.md**.

---

# 2. Philosophy

ASTRA is an **offline-first AI fitness operating system**.

The database exists to support coaching decisions.

Not merely to store information.

Every piece of stored data should improve future coaching.

---

# Database Principles

### Principle 1

Local first.

Every workout must function without internet.

---

### Principle 2

Cloud second.

Cloud improves convenience.

Cloud never blocks workouts.

---

### Principle 3

Structured over unstructured.

Workout history belongs in structured tables.

Not chat messages.

---

### Principle 4

Never duplicate truth.

One authoritative source exists for every data type.

---

### Principle 5

Everything is recoverable.

Backups.

Synchronization.

Version history.

---

# 3. Storage Layers

ASTRA uses three storage layers.

```text id="1rxl4d"
User

↓

Mobile App

↓

SQLite

↓

Synchronization Engine

↓

PostgreSQL

↓

Backup
```

---

## Layer 1

SQLite

Purpose

Primary local database.

Responsibilities

* workouts
* recovery
* nutrition
* progress
* cache
* active workout

SQLite is always available.

---

## Layer 2

PostgreSQL

Purpose

Primary cloud database.

Responsibilities

* long-term storage
* synchronization
* analytics
* reporting
* cloud backup

---

## Layer 3

Backup

Automatic exports.

Disaster recovery.

Version history.

---

# 4. Data Ownership

Every category has one owner.

---

Workout History

Owner

SQLite

Cloud receives synchronized copy.

---

Exercise Library

Owner

Reference Database

Read only.

---

Coach Memory

Owner

PostgreSQL

Cached locally.

---

Recovery

Owner

SQLite

Synced.

---

Nutrition

Owner

SQLite

Synced.

---

Analytics

Owner

PostgreSQL

Generated.

Cached locally.

---

# 5. Offline First

Internet disappears.

What happens?

Everything below continues.

```text id="9xkh5k"
Workout

Logging

History

Progress

Recovery

Nutrition

Calendar

Current Session
```

Unavailable

```text id="up0tcm"
Cloud Backup

Cloud AI

Synchronization
```

The user must still finish today's workout.

---

# 6. Synchronization Philosophy

Synchronization should be invisible.

The user never presses

Sync.

Instead

```text id="v0pn52"
Local Change

↓

Queue

↓

Internet Available

↓

Background Sync

↓

Cloud Updated
```

The user should rarely think about synchronization.

---

# 7. Conflict Resolution

Suppose

Phone

Logs

Bench

60 × 8

Cloud

Already has

60 × 7

Which wins?

Rule

Newest valid record wins.

Every update stores:

* timestamp
* device ID
* version number

Conflicts are logged.

Never silently discarded.

---

# 8. Database Domains

The database is divided into independent domains.

```text id="38vx17"
Profile

Workout

Recovery

Nutrition

Analytics

Memory

Chat

Settings

Reference
```

Domains communicate through services.

Never through direct table coupling.

---

# 9. Reference Data

Reference data rarely changes.

Examples

* exercises
* muscles
* equipment
* progression rules
* substitution rules

Reference data is read-only during normal operation.

---

# 10. User Data

User data changes continuously.

Examples

* workouts
* sets
* meals
* recovery
* body weight
* goals
* memory

User data is always editable.

---

# 11. Active Workout State

The current workout has special handling.

Requirements

If the application closes unexpectedly:

```text id="ofow0l"
Reopen App

↓

Resume Workout

↓

Continue Exactly Where User Stopped
```

Nothing should be lost.

---

# 12. Data Integrity

Every database write must satisfy:

* validation
* constraints
* transaction safety
* rollback on failure

Partial writes are not acceptable.

---

# END OF PART 1

# 📄 03_Database_Architecture.md

# PART 2 / FINAL

---

# 13. Database Modules

To keep the system maintainable, the database is organized into logical modules rather than one large collection of unrelated tables.

```text
Database
│
├── Profile
├── Workout
├── Recovery
├── Nutrition
├── Memory
├── Analytics
├── Chat
├── Settings
└── Reference
```

Each module owns its own tables and is accessed through its corresponding backend service.

---

# 14. Synchronization Engine

## Purpose

The Synchronization Engine keeps the local SQLite database and the cloud PostgreSQL database consistent.

Synchronization must be:

* Automatic
* Incremental
* Reliable
* Recoverable

---

## Synchronization Flow

```text
Local Change
      ↓
Sync Queue
      ↓
Network Available?
      ↓
      Yes
      ↓
Upload Changes
      ↓
Validate
      ↓
Apply to Cloud
      ↓
Mark as Synced
```

If the network is unavailable:

```text
Queue Change
      ↓
Wait
      ↓
Retry Automatically
```

The user should never lose workout data because of connectivity.

---

# 15. Caching Strategy

Not every request should query the cloud.

Cache locally:

* Exercise library
* User profile
* Workout plans
* Recent workout history
* Coach memory (relevant subset)
* Current recovery data

Do **not** cache:

* Authentication tokens in insecure storage.
* Temporary API secrets.
* Sensitive server configuration.

---

# 16. Transactions

All critical operations must use transactions.

Examples:

### Workout Completion

```text
Finish Workout
      ↓
Save Exercise Sessions
      ↓
Save Set Logs
      ↓
Update Workout Summary
      ↓
Commit
```

If any step fails:

```text
Rollback Transaction
```

Never leave partially completed workout data.

---

# 17. Data Validation

Every write must be validated before reaching the database.

Examples:

* Weight ≥ 0
* Repetitions > 0
* Sleep between 0 and 24 hours
* Protein ≥ 0
* Workout duration > 0

Validation belongs in the service layer, with database constraints acting as a final safeguard.

---

# 18. Security

Database security principles:

* Parameterized queries only.
* No raw SQL built from user input.
* Encrypt sensitive credentials.
* Least-privilege database access.
* Audit important changes.

Examples of audited events:

* Goal changes
* Workout plan modifications
* Memory edits
* Data restore operations

---

# 19. Performance Strategy

Performance goals:

| Operation      |  Target |
| -------------- | ------: |
| Read workout   | <100 ms |
| Log set        |  <50 ms |
| Resume workout | <150 ms |
| Search memory  | <200 ms |
| Dashboard load | <300 ms |

The most common operations should be optimized first.

---

# 20. Indexing Philosophy

Indexes should support the application's primary access patterns.

Examples:

* User workout history
* Exercise history
* Active workout lookup
* Daily recovery logs
* Nutrition by date
* Memory search

Avoid unnecessary indexes that slow writes.

---

# 21. Backup Strategy

Three levels of protection:

### Local

SQLite database remains on the device.

### Cloud

Automatic synchronization to PostgreSQL.

### Export

User can export data in supported formats (e.g., JSON or CSV) for long-term backup.

Backups should be versioned where practical.

---

# 22. Data Lifecycle

Every record follows a lifecycle.

```text
Created
    ↓
Updated
    ↓
Archived (if applicable)
    ↓
Deleted (only when appropriate)
```

Some records, such as workout history, should generally never be deleted automatically.

---

# 23. Error Recovery

If synchronization fails:

1. Keep the local record.
2. Record the failure.
3. Retry automatically.
4. Notify the user only if manual action is required.

The workout experience should continue uninterrupted.

---

# 24. Future Expansion

The architecture should support future additions without redesign.

Examples:

* Wearable device data
* Heart-rate tracking
* Camera-based movement analysis
* Mobility assessments
* Multiple workout programs
* Advanced recovery metrics

These should integrate through new modules rather than altering existing foundations.

---

# 25. Acceptance Criteria

This architecture is considered complete when:

* Workouts function fully offline.
* Synchronization is automatic.
* No data is silently lost.
* Transactions protect critical writes.
* Validation exists at multiple layers.
* Database modules remain independent.
* Backup and recovery are supported.
* Performance targets are achievable.

---

# 26. Summary

ASTRA follows an offline-first architecture.

```text
User
   ↓
SQLite (Primary Runtime)
   ↓
Synchronization Engine
   ↓
PostgreSQL (Cloud Source)
   ↓
Backups & Analytics
```

The database exists to support long-term coaching, not simply to store records.

---

# END OF DOCUMENT

**Document Status:** ✅ COMPLETE

**Version:** 1.0.0

**Next Document:** `04_API_Architecture.md`

---

