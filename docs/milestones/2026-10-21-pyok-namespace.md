# PyOK distribution and namespace — 2026-10-21

## Scope and provenance

- Repository: `https://github.com/mcbutterfield/PyOK`, forked from `ansys/pystk`.
- Upstream baseline: `669a4921c6ee9838aa757e726e0e171305bb6fe9`.
- Distribution: `br-ok`; Python namespaces: `br.ok.core` and `br.ok.extensions`.
- Moved the source tree and API reference tree, updated imports, examples,
  tests, documentation tooling, bundled migration mappings, extras, coverage,
  and package metadata. The CLI is `pyok-migration-assistant`.
- Preserved the upstream version (`0.4.dev0`), license, copyright notices,
  attribution, native STK interfaces, identifiers, and optional dependencies.
- Added a package CI workflow for Python 3.10, 3.12, and 3.14. This record
  reports local results; it does not claim those hosted jobs have run.
- The implementation commit containing this record is available through
  `git log -- docs/milestones/2026-10-21-pyok-namespace.md`.

## Validation

Native macOS ARM64, CPython 3.12.13, isolated virtual environments:

- `python -m build --no-isolation`: built `br_ok-0.4.dev0.tar.gz` and
  `br_ok-0.4.dev0-py3-none-any.whl`; the wheel was built from the sdist.
- Installed the wheel and ran
  `python -m pytest tests/test_pyok_package.py tests/api_migration_assistant_tests -q`:
  **56 passed**, including all 43 upstream migration tests.
- Installed the wheel without dependencies in a separate clean environment.
  Isolated-mode imports of `br.ok.core`, `br.ok.extensions`, `STKObjectType`,
  and `STKEngine` succeeded; no `ansys` modules were loaded.
- Verified distribution identity, version, extras, console entry point,
  packaged namespace, gRPC import, migration targets, and representative
  enum/color behavior. The CLI and module CLI both display help successfully.
- Compared all **106** packaged source/resource files against the baseline:
  byte-identical after the exact substitution `ansys.stk` → `br.ok`.
- All **3,833** generated API documentation files retain upstream bytes except
  namespace/distribution substitutions. This preserves generated RST headings
  and trailing blank lines that Git's generic whitespace/conflict-marker check
  flags when a renamed page is classified as an added file.
- `python -m compileall -q src scripts` passed. Staged whitespace verification
  used `git -c core.whitespace=cr-at-eol diff --cached --check -- .
  ':(exclude)doc/source/api'`: source CRLF endings are intentionally preserved;
  generated API documentation is covered by the byte comparison above.

## Remaining gates and limits

- Native STK execution and its generated integration/graphics tests require
  compatible STK software, a supported runtime platform, and a license. They
  were not run on this Mac. Import success is not runtime qualification.
- The upstream mappings include a target for a missing
  `core.utilities.exceptions` module. This pre-existing mapping is preserved;
  the package checks verify namespace conversion without asserting that every
  upstream mapping resolves to an implemented module.
- No PyPI publication, STK deployment, runtime installation, or licensing change
  is part of this milestone. Install from the GitHub repository or a local wheel.
- There is no `pyok` alias, and this wheel does not supply `ansys.stk`.
