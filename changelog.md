
## Changelog - WebScraping


### v0.3.27 - 25th July 2026

- Added `[tool.ruff.lint] select = ["E4", "E7", "E9", "F"]` to
  `pyproject.toml`, pinning ruff's default rule set explicitly
  (verified via `ruff check --show-settings` against the project's
  locked 0.15.9 — identical enabled-rule list before and after). A
  future ruff release can no longer silently turn on new default
  rules underneath the project. Part of a fleet-wide pass; see
  programme's backlog and v4.91.1/v4.92.0.


### v0.3.26 - 24th July 2026

- `CLAUDE.md`: replaced the superseded **Core Rules** periodic-review
  trigger with the backlog-depth rule — when `/backlog` shows fewer
  than 5 open items, propose `/scan`, `/improvements`, and `/prune`.
  The old "Every 6-7 versions" cadence also named `/refactor` and
  `/optimize`, neither of which is a real skill. Pushed from the
  programme registry via `sync-config --types section`.


### v0.3.25 - 24th July 2026

- Updated `.claude/rules/committing.md`: adds the canonical
  `Pull First — Before Any Work` section — `git pull` is the first step
  of every session, run before reading, planning, or editing, not just
  before pushing. Synced from the programme registry (rule v1.4).


### v0.3.24 - 24th July 2026

- Updated `.claude/rules/committing.md` from canonical: `uv.lock` is
  committed whenever it changed, and a lock-only diff takes no version
  bump or changelog entry (bumping `pyproject.toml` would push it ahead
  again and recreate the drift, so it never converges).


### v0.3.23 - 24th July 2026

- Updated `.pre-commit-config.yaml`: the ruff hooks now run
  `uv run --no-sync ruff` instead of `uvx ruff`.
  - `uvx` resolves whatever ruff PyPI serves that day, so the commit
    gate and this project's own lock-pinned ruff were different
    versions — and any upstream ruff release could change the enforced
    rule set with no local change. `uv run` uses this project's ruff,
    so local and commit-time linting always agree.
  - `--no-sync` is required, not an optimization: a bare `uv run`
    re-syncs first, which on a version-bump commit rewrites `uv.lock`
    mid-hook and leaves pre-commit's stash/restore cycle fighting its
    own linter. Verified in programme v4.83.1.
  - `ruff format` loses its `.` argument: pre-commit already passes the
    staged files, and a literal `.` overrode that to format the whole
    tree.
  - Pushed from programme's canonical `python-base` skeleton (v4.83.1).


### v0.3.22 - 3rd July 2026

- Synced the canonical `check-version-changelog` pre-commit guard:
  manifests under `reservations/` are now excluded from the
  version-changelog check (defensive package-name placeholders carry
  their own versions, independent of the app release).


### v0.3.21 - 20th June 2026

- Added `scripts/changelog-add.sh` (safe changelog-prepend helper) and the `check-version-changelog` pre-commit guard, distributed in the programme fleet rollout.
- Restored `.pre-commit-scripts/check_unstaged_claude.py` and removed the
  stray `.pre-commit-scripts/` `.gitignore` entry so local hook scripts
  are tracked like the rest of the fleet.


### v0.3.20 - 14th June 2026

- Added the `check-changelog-headers` pre-commit guard
  (`.pre-commit-scripts/check_changelog_headers.sh` + the `.pre-commit-config.yaml`
  stanza): blocks a changelog edit that overwrites an existing version
  header (the bug that silently lost manifold's `v0.1.35`).


### v0.3.19 - 8th June 2026

- Synced reworded `versioning.md` changelog-prepend guidance from programme — insert a new entry above the top header instead of replacing it.


### v0.3.18 - 4th June 2026

- Synced `.claude/rules/committing.md` from the programme registry: step 6 now scopes `uv.lock` regeneration to code-related bumps only — non-code patch bumps (`.claude/` config, docs, changelog, rule syncs) skip `uv lock`.


### v0.3.17 - 3rd June 2026

- Synced `.claude/rules/testing.md` from the programme registry: added the SQLite-backed fixtures pointer to the session-scoped template pattern (see the shared `testing-python` rule).


### v0.3.16 - 1st June 2026

- Updated `.claude/rules/committing.md`: no-parallel-git-command rule and `-m` flag guidance.


### v0.3.15 - 10th May 2026

- Synced canonical `testing.md` from `programme` v2.55.2 (blank line trim before `## Running Tests` section).


### v0.3.14 - 9th May 2026

- Added `When to Skip Tests` section to `.claude/rules/committing.md`: explicit allowlist (markdown, version bump, lock file, `.claude/` config, `CLAUDE.md`) of diffs where tests can be safely skipped.


### v0.3.13 - 9th May 2026

- Updated `.claude/rules/versioning.md` (1.0 → 1.1): rewrote changelog-format section to fix rule/example contradiction; threshold now stated as "3+ top-level bullets touching the same module → group under a parent"; sub-bullet patterns reorganised; added "When NOT to group" section. Synced from programme v2.52.144.


### v0.3.12 - 8th May 2026

- Synced canonical rules from `programme` v2.52.139/v2.52.140: `backlog`, `refactoring`, `optimization`, `improvements` rules promoted to global (`~/.claude/rules/`) and removed locally; `versioning.md` updated with depth-based-cadence batch exception.


### v0.3.11 - 20th April 2026

- Synced canonical `.gitignore` from programme (direnv block).


### v0.3.10 - 17th April 2026

- `.gitattributes`: Added LF line ending normalization.


### v0.3.9 - 15th April 2026

- `.claude/`: cross-project migration landed today:
  - Removed `.claude/hooks/pre-commit-tests.sh`; replaced by a global dispatcher at `~/.claude/hooks/pre-commit-tests.sh` that invokes `scripts/pre-commit.sh` on `git commit`. Added `scripts/pre-commit.sh` with the project-local test command.


### v0.3.8 - 11th April 2026

- `.claude/rules/`:
  - Decoupled `/refactor` rule: canonical
    `refactoring.md` is now procedural only.
  - Added `refactoring-areas.md` with
    project-specific code smells to watch.
- `.claude/skills/refactor/`:
  - Updated `SKILL.md` to read both canonical
    procedure and per-project areas.


### v0.3.7 - 11th April 2026

- `.claude/rules/`:
  - Decoupled `/optimize` rule: canonical
    `optimization.md` is now procedural only.
  - Added `optimization-areas.md` with
    project-specific performance areas.
- `.claude/skills/optimize/`:
  - Updated `SKILL.md` to read both canonical
    procedure and per-project areas.


### v0.3.6 - 10th April 2026

- `.claude/rules/`:
  - Decoupled `/improvements` rule: canonical
    `improvements.md` is now procedural only.
  - Added `improvement-areas.md` with
    project-specific areas to watch.
- `.claude/skills/improvements/`:
  - Updated `SKILL.md` to read both canonical
    procedure and per-project areas.


### v0.3.5 - 7th April 2026

- Updated `scripts/playwright_tutorial.py`:
  - Added timestamps to logging format (`%H:%M:%S`)
  - Wait 5 seconds after the signup modal loads (not before),
    then collect page info and close


### v0.3.4 - 7th April 2026

- Updated `scripts/playwright_tutorial.py`:
  - Added step 7: click "Crear cuenta" and wait for the signup
    dialog using `wait_for_selector` instead of a fixed timeout
  - Added third `get_page_info()` call capturing the modal state


### v0.3.3 - 7th April 2026

- Updated `scripts/playwright_tutorial.py`:
  - Replaced all `print()` calls with `logging` module
  - Configured `basicConfig` with `format="%(message)s"` for
    clean output


### v0.3.2 - 7th April 2026

- Updated `scripts/playwright_tutorial.py`:
  - Moved `explore_x()` above helper functions for readability
  - Added 5-second pause before closing so students can see the result
  - Fixed missing tildes in all Spanish text (comments, prints,
    docstrings)


### v0.3.1 - 7th April 2026

- Updated `scripts/playwright_tutorial.py`:
  - Extracted reusable helper functions: `get_screenshot()`,
    `get_links()`, `get_buttons()`, `get_headings()`,
    `get_cookies()`, `get_page_info()`
  - Moved browser logic into `explore_x()` function
  - Added cookie banner acceptance with `wait_for_load_state()`
  - Script now collects page info before and after accepting cookies


### v0.3.0 - 7th April 2026

- Added `scripts/playwright_tutorial.py`: tutorial script that
  explores X.com with a clean browser (no cache, no cookies),
  extracts links, headings, cookies, and takes a screenshot
- Updated `.gitignore`: exclude `*.png` files


### v0.2.1 - 7th April 2026

- Updated `README.md`: added installation guide for Playwright
  browsers (in Spanish)


### v0.2.0 - 7th April 2026

- Added `playwright>=1.40.0` dependency for browser automation


### v0.1.0 - 6th April 2026

- Initial project setup with Claude Code canonical skeleton.
- Migrated from Poetry to uv.
- Added `.claude/` configuration:
  - 8 canonical rules (committing, versioning, testing, shell, backlog, improvements, optimization, refactoring).
  - 5 skills (backlog, refactor, optimize, improvements, self-refinement).
  - 4 hooks (block-chained-commands, block-raw-python, format-python, pre-commit-tests).
- Added `.pre-commit-config.yaml` with ruff hooks.
- Added `.python-version` (3.14).
