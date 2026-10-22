# PyOK namespace change to br.steak.core — 2026-10-21

## Scope and provenance

- Repository remains `https://github.com/mcbutterfield/PyOK`.
- Previous PyOK commit: `2d27302090fc515465b5613d1a353ffa34cd3120`.
- Upstream baseline: `669a4921c6ee9838aa757e726e0e171305bb6fe9`.
- Distribution changes from `br-ok` to `br-steak`; the primary import becomes
  `br.steak.core`, with extensions under `br.steak.extensions`.
- Updated package paths, imports, metadata, extras, examples, bundled migration
  mappings, documentation, coverage, tooling, and regression tests together.
- Retained the PyOK repository name, `pyok-migration-assistant` command,
  version `0.4.dev0`, upstream licensing/attribution, and native STK interfaces.
- Preserved the earlier milestone record. The commit containing this new
  record is discoverable with
  `git log -- docs/milestones/2026-10-21-br-steak-namespace.md`.

## Validation

Native macOS ARM64, CPython 3.12.13:

- Built `br_steak-0.4.dev0.tar.gz` and `br_steak-0.4.dev0-py3-none-any.whl`
  using `python -m build --no-isolation --outdir dist/steak`.
- Removed the earlier distribution from the isolated test environment,
  installed the new wheel, and passed all **56** package/migration tests.
- A second clean environment installed the wheel without dependencies and
  imported the core, extensions, `STKObjectType`, and `STKEngine` successfully.
  `br.ok` was absent, and no `ansys` modules were loaded.
- The package tests check that neither `ansys/` nor `br/ok/` ships in the wheel,
  neither earlier distribution is a dependency, and migration mappings target
  `br.steak.core` without either earlier import namespace.
- Compared all **106** packaged source/resource files against upstream:
  byte-identical after `ansys.stk` → `br.steak` substitution.
- Compared all **3,833** generated API documentation files against upstream:
  byte-identical after namespace/distribution substitutions.
- `python -m compileall -q src scripts` passed. Whitespace checks account for
  preserved upstream CRLF source endings and exclude generated API pages,
  which are verified by the byte comparison above.

## Remaining gates and installation

- Native STK execution/integration tests require the same compatible STK runtime
  and license as before; they were not run on this Mac.
- The existing package CI workflow tests Python 3.10, 3.12, and 3.14 on push.
  This record reports local results and does not claim the new hosted run passed.
- Nothing was published to PyPI. Install with
  `python -m pip install "br-steak @ git+https://github.com/mcbutterfield/PyOK.git"`.
- Users of the earlier distribution should uninstall `br-ok` before installing
  `br-steak`; the new package does not provide an old-namespace alias.
