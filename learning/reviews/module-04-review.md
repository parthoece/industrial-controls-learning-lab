# Module 4 review — PC controller software

Answer without opening the weekly lessons.

1. Define deadline, jitter, and overrun.

<details><summary>Answer</summary>

Deadline: latest completion; jitter: timing variation; overrun: work misses the next release/deadline.

</details>

2. Why is mean interval insufficient?

<details><summary>Answer</summary>

Rare large delays can violate control requirements while the mean remains good.

</details>

3. What belongs outside the cyclic path?

<details><summary>Answer</summary>

Blocking I/O, databases, APIs, large logs, and unbounded work.

</details>

4. Why use bounded queues?

<details><summary>Answer</summary>

To bound memory and latency and define overload behavior.

</details>

5. What does a simulator not prove?

<details><summary>Answer</summary>

Hardware timing, fieldbus conformance, electrical/mechanical behavior, or safety integrity.

</details>
