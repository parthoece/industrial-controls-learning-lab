# Publishing Checklist

## Repository identity

- [ ] Repository name is `industrial-controls-learning-lab`
- [ ] Description states the three target role families
- [ ] Topics include `control-systems`, `motion-control`, `industrial-automation`, `ethercat`, `plc`, and `smart-manufacturing`
- [ ] `YOUR_GITHUB_HANDLE` placeholders are replaced
- [ ] Maintainer and private security contacts are replaced

## GitHub settings

- [ ] Default branch is `main`
- [ ] Pull requests require CI to pass
- [ ] Direct pushes to `main` are restricted when collaborators join
- [ ] Private vulnerability reporting is enabled
- [ ] Discussions are enabled only when someone will moderate them
- [ ] Issue labels from [the label guide](maintainer/labels.md) are created

## First release

- [ ] `make check` passes from a clean clone
- [ ] README commands work on the supported Python versions
- [ ] Mermaid diagrams render on GitHub
- [ ] Changelog and citation version agree
- [ ] A `v0.1.0` release explains that examples are simulation-first

## Future capstone link

Do not add an empty capstone repository merely to remove a placeholder. Create it after the learning gates are complete, then replace `CAPSTONE_REPOSITORY_URL` in the [capstone handoff](07-future-capstone-handoff.md).
