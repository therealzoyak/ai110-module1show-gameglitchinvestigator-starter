"""Streamlit interface for Glitch Hunt."""

import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_attempt_limit,
    get_range_for_difficulty,
    parse_guess,
    proximity_hint,
    update_score,
)

st.set_page_config(page_title="Glitch Hunt", page_icon="🎮", layout="centered")
st.title("Glitch Hunt")
st.caption("A number game rebuilt from an AI-generated mess—and a tiny case study in testing stateful apps.")

difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
low, high = get_range_for_difficulty(difficulty)
attempt_limit = get_attempt_limit(difficulty)


def reset_game() -> None:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_difficulty = difficulty


if "secret" not in st.session_state or st.session_state.get("game_difficulty") != difficulty:
    reset_game()

attempts_left = attempt_limit - st.session_state.attempts
metric_1, metric_2, metric_3 = st.columns(3)
metric_1.metric("Range", f"{low}–{high}")
metric_2.metric("Attempts left", attempts_left)
metric_3.metric("Score", st.session_state.score)
st.progress(st.session_state.attempts / attempt_limit)

raw_guess = st.text_input("Your guess", placeholder=f"Enter a whole number from {low} to {high}")
show_proximity = st.checkbox("Add a proximity hint", value=True)
submit_column, reset_column = st.columns(2)
submit = submit_column.button("Submit guess", type="primary", use_container_width=True)
new_game = reset_column.button("New game", use_container_width=True)

if new_game:
    reset_game()
    st.rerun()

if submit and st.session_state.status == "playing":
    valid, guess, error = parse_guess(raw_guess, low, high)
    if not valid:
        st.error(error)
    else:
        st.session_state.attempts += 1
        outcome, message = check_guess(guess, st.session_state.secret)
        st.session_state.history.append({"Guess": guess, "Result": outcome})
        st.session_state.score = update_score(
            st.session_state.score,
            outcome,
            st.session_state.attempts,
        )
        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
            st.success(f"{message} You found it in {st.session_state.attempts} attempts.")
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(f"Out of attempts—the number was {st.session_state.secret}.")
        else:
            hint = proximity_hint(guess, st.session_state.secret, low, high) if show_proximity else ""
            st.warning(f"{message} {hint}".strip())

if st.session_state.status != "playing":
    st.info("Start a new game or change difficulty to play again.")

if st.session_state.history:
    st.subheader("Guess history")
    st.dataframe(st.session_state.history, hide_index=True, use_container_width=True)

with st.expander("What was broken?"):
    st.write(
        "The original regenerated its secret, reversed higher/lower hints, counted attempts inconsistently, "
        "truncated decimal guesses, and used scoring rules that could reward a wrong answer. The game rules "
        "now live outside Streamlit so they can be tested without clicking through the UI."
    )
