# GitHub repository renamed to PySteak — 2026-10-21

## Scope and provenance

- Renamed `mcbutterfield/PyOK` to `mcbutterfield/PySteak` using GitHub's
  repository rename operation; the repository and its history are retained.
- Canonical URL: `https://github.com/mcbutterfield/PySteak`.
- Updated the local `origin` remote, active README/install instructions,
  distribution metadata links/description, and package CI display name.
- Retained distribution `br-steak`, imports `br.steak.core` and
  `br.steak.extensions`, and the existing `pyok-migration-assistant` CLI.
- Preserved earlier milestone records as historical evidence.
- Pre-rename source commit: `c4c526478af9df9e8c8d84a4663c91d1d1086114`.
- This record's commit is discoverable with
  `git log -- docs/milestones/2026-10-21-pysteak-repository.md`.

## Validation

- Rebuilt the `br-steak` source distribution and wheel after the link changes.
- Installed the wheel in the isolated CPython 3.12.13 environment and ran
  `python -m pytest tests/test_pyok_package.py -q`: **13 passed**.
- `git diff --check` passed. No API implementation or namespace change was
  part of this repository rename.
- Verified the renamed repository through GitHub's API and updated `origin`.
- The existing GitHub package workflow runs its full test matrix after push;
  this record reports local results without claiming a later hosted outcome.

Install from the new URL:

```sh
python -m pip install "br-steak @ git+https://github.com/mcbutterfield/PySteak.git"
```

```python
import br.steak.core
```
