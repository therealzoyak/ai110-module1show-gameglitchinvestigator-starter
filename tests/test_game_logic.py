import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import (
    check_guess,
    get_attempt_limit,
    get_range_for_difficulty,
    parse_guess,
    proximity_hint,
    update_score,
)


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_invalid_guess_does_not_parse():
    ok, value, error = parse_guess("4.2", 1, 20)
    assert not ok
    assert value is None
    assert error


def test_out_of_range_guess_is_rejected():
    ok, _, error = parse_guess("501", 1, 500)
    assert not ok
    assert "between" in error


def test_difficulty_changes_range_and_attempts():
    assert get_range_for_difficulty("Hard") == (1, 500)
    assert get_attempt_limit("Hard") == 9


def test_wrong_guess_never_earns_points():
    assert update_score(0, "Too High", 2) == 0


def test_win_score_decreases_with_attempts_but_has_floor():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 20) == 10


def test_proximity_hint_changes_with_distance():
    assert proximity_hint(49, 50, 1, 100) == "You are extremely close."
    assert proximity_hint(1, 50, 1, 100) == "You are cold."
