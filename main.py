"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt, as the program/v1 harness
requires. The line is fixed and hand-written: a broadcast-style forecast
for the invented city of Nimbostratus Falls, with one concrete commuter
detail (the 8:04 bus) and one small joke (the clouds stopping to admire
themselves) to make a bored commuter smile.
"""

import os

FORECAST = (
    "Nimbostratus Falls: 14\u00b0C, light drizzle easing by 9am. "
    "The 8:04 bus is 6 minutes late \u2014 the clouds keep stopping "
    "to admire themselves."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = FORECAST.strip()
    assert 1 <= len(line) <= 140, f"forecast is {len(line)} chars, must be 1-140"
    assert line.strip(), "forecast must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
