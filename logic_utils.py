"""Pure game rules for Glitch Hunt."""

from __future__ import annotations

DIFFICULTIES = {
    "Easy": {"low": 1, "high": 20, "attempts": 6},
    "Normal": {"low": 1, "high": 100, "attempts": 8},
    "Hard": {"low": 1, "high": 500, "attempts": 9},
}


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    settings = DIFFICULTIES.get(difficulty, DIFFICULTIES["Normal"])
    return settings["low"], settings["high"]


def get_attempt_limit(difficulty: str) -> int:
    return DIFFICULTIES.get(difficulty, DIFFICULTIES["Normal"])["attempts"]


def parse_guess(raw: str | None, low: int | None = None, high: int | None = None):
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."
    try:
        value = int(raw.strip())
    except ValueError:
        return False, None, "Use a whole number."
    if low is not None and high is not None and not low <= value <= high:
        return False, None, f"Guess between {low} and {high}."
    return True, value, None


def check_guess(guess: int, secret: int):
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go lower."
    return "Too Low", "📈 Go higher."


def proximity_hint(guess: int, secret: int, low: int, high: int) -> str:
    distance_ratio = abs(guess - secret) / max(high - low, 1)
    if distance_ratio <= 0.05:
        return "You are extremely close."
    if distance_ratio <= 0.15:
        return "You are warm."
    return "You are cold."


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome != "Win":
        return current_score
    return current_score + max(10, 100 - 10 * (attempt_number - 1))
