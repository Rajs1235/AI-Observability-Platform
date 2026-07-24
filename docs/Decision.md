# Architecture Decisions

This document records important architectural decisions made during the development of the platform.

---

## ADR-001

Decision

Keep Raw Logs and Templates separately.

Reason

- Preserve original logs
- Easier debugging
- Better ML training
- Better analytics

---

## ADR-002

Decision

Use SQLite during initial development.

Reason

- Zero setup
- Lightweight
- Fast iteration

Future

MongoDB / PostgreSQL

---

## ADR-003

Decision

Use Drain3 for template extraction.

Reason

- Industry standard
- Research-backed
- Fast
- Proven

---

## ADR-004

Decision

Collector watches log files instead of applications.

Reason

- Language independent
- Works with any application
- Easier deployment

---

## ADR-005

Decision

Separate NLP, ML and DL pipelines.

Reason

Different objectives require different preprocessing and models.

---

## ADR-006

Decision

Use Docker as the primary deployment method.

Reason

- Platform independent
- Easy onboarding
- Production friendly

---

## ADR-007

Decision

RAG is not part of Version 1.

Reason

Platform should provide value even without an LLM.
