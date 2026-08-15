# Glitch Hunt

Glitch Hunt is a small Streamlit number game and a debugging story: an AI-generated prototype looked playable, but its secret changed between reruns, its hints lied, its attempt counter drifted, and one branch rewarded wrong answers.

I separated the rules from the interface, wrote tests around the failure modes, and rebuilt the game state so Streamlit reruns are predictable.

## What changed

- stable per-round secret stored in session state
- difficulty-specific ranges and attempt limits
- whole-number and range validation that does not consume an attempt
- correct higher/lower and proximity hints
- scoring only on a win, weighted by attempts used
- automatic reset when difficulty changes
- visible progress and guess history
- pure game logic that can be tested without Streamlit

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Test it

```bash
python -m pytest -q
```

## Origin

This began as a CodePath debugging exercise. The intentionally broken app and brief were provided; the diagnosis, state repair, refactor, expanded rules, interface cleanup, and tests are my work.
