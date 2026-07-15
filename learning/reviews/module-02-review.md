# Module 2 review — PLC and machine control

Answer without opening the weekly lessons.

1. Trace a start request through three scans.

<details><summary>Answer</summary>

Show input image, edge detection, permission evaluation, state transition, and output update.

</details>

2. Separate mode from state with an example.

<details><summary>Answer</summary>

Mode AUTO, state READY; or mode MANUAL, state RUNNING.

</details>

3. What is the difference between acknowledgement and reset?

<details><summary>Answer</summary>

Acknowledgement records that an alarm was seen; reset requests recovery after the cause is clear.

</details>

4. Why return to IDLE after fault reset?

<details><summary>Answer</summary>

To prevent automatic restart and restore a known non-running state.

</details>

5. What should a rejected transition expose?

<details><summary>Answer</summary>

A stable reason code and relevant state/permission values.

</details>
