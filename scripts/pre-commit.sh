#!/bin/bash
# Project-local pre-commit checks. Invoked by the global
# ~/.claude/hooks/pre-commit-tests.sh when a Bash tool runs
# `git commit`. Exit non-zero to block the commit.
set +e
uv run --extra dev pytest tests/unit/ --tb=short -q
status=$?
# Exit code 5 = pytest collected zero tests. This tutorial repo has
# never had a tests/unit/*.py file, so that is the expected state,
# not a failure — only a real test failure (any other nonzero code)
# blocks the commit.
if [ "$status" -eq 5 ]; then
    exit 0
fi
exit "$status"
