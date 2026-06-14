
## Changelog - WebScraping


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
