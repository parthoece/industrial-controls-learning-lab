# Contributing

Thank you for making industrial controls more approachable to software engineers.

## Ways to contribute

- clarify a concept or fix terminology
- add a small reproducible experiment
- improve diagrams, accessibility, or translations
- add tests or failure cases
- improve vendor-neutral Structured Text examples
- propose learning resources with an accompanying explanation
- improve the future capstone handoff without implementing the capstone here

## Before opening work

1. Search existing issues and pull requests.
2. Use a proposal issue for a new module, major reorganization, public interface, or repository-policy change.
3. Keep beginner material vendor-neutral when practical.
4. Never submit proprietary code, confidential diagrams, employer/customer data, vendor license files, credentials, or copied safety logic.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
make check
```

Windows users can run the equivalent commands directly without `make`:

```powershell
python -m compileall -q src tests scripts
pytest
python scripts/check_repo.py
```

## Content expectations

Every learning contribution should answer:

1. What problem does this concept solve?
2. Where does it sit in the control stack?
3. Which assumptions, units, timing, or states matter?
4. What can go wrong?
5. How can the behavior be observed or tested?
6. What is intentionally deferred as advanced work?

## Code expectations

- keep examples small and explainable
- use type hints and explicit validation
- separate state, command, status, and diagnostics
- add a normal and failure test when behavior changes
- state whether work is simulation, pseudocode, or hardware-tested
- never imply that standard logic is functional safety
- keep generated databases, videos, and large binaries out of Git

## Pull requests

A pull request should:

- explain the problem and proposed change
- remain focused enough to review
- include tests or evidence when behavior changes
- update links and documentation
- pass CI
- complete the pull-request checklist

Suggested commit prefixes: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, and `chore:`.

## Licensing

By submitting a contribution, you agree that it will be licensed under the Apache License 2.0. You retain copyright to your contribution.

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report security problems privately according to [SECURITY.md](SECURITY.md).
