#!/usr/bin/env python3
"""Escalated to Tier 2 — "Have You Tried Turning It Off?"

Writes one funny line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt.

The line subverts the escalation trope instead of repeating the
"turn it off and on again" cliche: Tier 2 turns out to be the same
agent, in a different chair, with the same manual.

Deterministic: no network, no randomness, no clock, no environment input.
"""

import os

LINE = (
    "Your ticket has been escalated to Tier 2, which is me, "
    "in a different chair, with the same manual."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one line, under 200 characters, one sentence,
    # spoken directly to the customer.
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) < 200, "entry must be under 200 characters"
    assert LINE.endswith("."), "entry must end with a period"
    assert LINE.strip() == LINE, "entry must not have extra whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
