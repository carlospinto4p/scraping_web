# Optimization Areas

Project-specific performance areas to watch for when
running `/optimize` or noticing issues during normal work.

## Common Signals

     limit)
   - O(n^2) or worse patterns in hot paths

## What to Look For

- **Memory**: unbounded growth, large object retention, unnecessary
  copies, missing cleanup/eviction
- **CPU**: hot loops, redundant computation, expensive operations in
  tight paths, regex compiled per call
- **I/O / Async**: sequential awaits that could use `asyncio.gather`,
  missing connection reuse, redundant HTTP calls
- **Data structures**: lists used for lookups (should be sets/dicts),
  string concatenation in loops, repeated serialization
