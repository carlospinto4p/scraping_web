
## Changelog - WebScraping

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
