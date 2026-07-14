# Lab 03 — Equipment State and Interlocks

## Question

How can a technician determine why a start request was rejected?

## Baseline

```bash
python -m industrial_controls_lab run machine
```

## Experiments

- open the simulated guard before start
- lose motion permission while running
- try resetting while the cause is still active
- verify clearing a fault does not automatically restart
- add a sequence timeout reason

## Evidence

Publish a state diagram, transition table, test cases, and observable block/fault reasons.
