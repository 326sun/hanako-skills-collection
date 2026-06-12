---
name: tdd
description: "Test-driven development: red-green-refactor loop. Behavior tests over implementation tests. Vertical slices (one test, one implementation). Triggers: TDD, test first, test-driven, red-green-refactor, write tests."
---

# Test-Driven Development

Tests describe what the system does, not how. Good tests survive refactors.

## Core Principle

**Behavior tests, not implementation tests.** Test through public interfaces. A test that reads like a specification — "user can checkout with valid cart" — tells you what capability exists. These tests survive internal refactoring.

**Bad test sign:** rename an internal function, tests break. Behavior unchanged, tests testing implementation.

## Anti-Pattern: Horizontal Slicing

Never write all tests first, then all implementation. This tests imagined behavior, not actual behavior. Tests become insensitive to real changes.

**Correct: vertical slices.** One test → one implementation → repeat.

```
Wrong (horizontal):  RED: test1-5 → GREEN: impl1-5
Right (vertical):    RED→GREEN per test, one at a time
```

## Workflow

### 1. Plan
- Confirm public interface
- Confirm which behaviors to test (prioritize)
- List behaviors, not implementation steps
- Get user approval

### 2. Tracer Bullet
Write ONE test for ONE behavior → fail → minimal code → pass. Proves the path end-to-end.

### 3. Incremental Loop
For each remaining behavior: RED (write next test) → GREEN (minimal code). One test at a time. No speculative features.

### 4. Refactor
Only after all tests pass (GREEN). Extract duplication, deepen modules, apply SOLID where natural. Run tests after each step. Never refactor while RED.

## Per-Cycle Checklist
```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```

## Choosing Test Seams

- **Unit tests** for pure logic: calculations, transformations, validation
- **Integration tests** for cross-module paths: API → service → database
- **E2E tests** for critical user-visible flows only — they are slow and fragile

If a bug needs multiple callers to trigger, a single-caller unit test gives false confidence. Note "no correct test seam exists" — that is an architectural finding.

## Constraints

- Never horizontal-slice (all tests first)
- Never test private methods or internals
- Never verify through database queries directly (use public interface)
- Never refactor while RED
- Never write tests for future requirements
- Mock module boundaries, not internal collaborators
