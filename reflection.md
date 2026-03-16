# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Enter didn't actually submit the guess
  2. it took forever for the guess box to load
  3. Attempts are off and so it didn't update the first time (technically should have 8 attempts as written in the sidebar, but the UI displays that I have 7 attempts so it didn't decrement until 2 attmepts later)
  4. New game resets the attempts but doesn't actually start a new game (You already won. Start a new game to play again. is still there)
  5. When I do a guess, untoggle Show hint, and then retoggle it the hint no longer shows up and it takes another attempt for it to show up
  6. Buggy hints? don't know what the number is but it tells me to go lower when i type in 100 and higher when i say 99, must be changing the secret number or had the wrong hints. The secret number was 15, told me 99 was too low and 100 was too high how weird is that?
  7. When I run out of all attempts and game is over and I click "New Game" it just keeps flashing me that game is over and to start a new game which is so sus
  
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?

I used VS Code Copilot for the actual debugging workflow and ChatGPT to help me plan how to use Copilot more carefully. One thing I did that helped a lot was starting separate Copilot chats for each bug, because otherwise the suggestions started mixing multiple problems together. For the hint bug, Copilot correctly pointed out that the comparison logic in check_guess was part of the problem and suggested moving that function into logic_utils.py so the logic wasn’t mixed with the Streamlit UI. After that change, I tested it using the debug panel in the app and also added a small pytest to make sure the function returned the correct outcome.

One suggestion Copilot gave that I didn’t end up keeping was fixing the hint text directly in app.py after calling check_guess. Technically that would have made the hints look correct, but it meant the UI code was patching the logic instead of fixing it at the source. Since the assignment wanted the logic moved to logic_utils.py, I rejected that version and asked for a cleaner change where check_guess itself returned the correct message. After that I reran the app and tested a bunch of guesses against the debug secret to make sure the hints matched the actual number.

---

## 3. Debugging and testing your fixes

I didn’t assume a bug was fixed just because Copilot suggested a change. For the hint issue, I kept using the Developer Debug Info panel and intentionally guessing numbers higher and lower than the secret to see if the hint direction made sense. For the New Game bug, I tested the flow where you win or lose first and then click New Game to make sure the app actually reset instead of showing the old “game over” state.

I also added a pytest for the check_guess function. That part actually took a bit of debugging because pytest couldn’t import logic_utils.py at first, which caused the tests to crash before they even ran. I had to adjust the test file so Python could find the module. Once the import issue was fixed, the tests passed and confirmed that the function returned the correct outcomes for higher, lower, and winning guesses.

---

## 4. What did you learn about Streamlit and state?

One thing that finally made sense during this project is that Streamlit reruns the whole script every time something happens, like clicking a button or entering input. That means normal variables reset constantly unless they’re stored in st.session_state. Session state basically acts like memory for the app, so things like the secret number, score, and attempts can survive across reruns. Without that, the game would basically restart every time the user clicked something. Once I understood that, a lot of the weird behavior in the app made more sense.

---

## 5. Looking ahead: your developer habits

One habit from this project that I want to reuse is slowing down and debugging the code line by line instead of immediately assuming the AI suggestion is correct or looking for another tool (like Chat). When I actually averted my frustration and just line by line went through the logic and instructions, especially around the check_guess function and how session state was behaving, it became much easier to understand why the bugs were happening. They really are simple just tedious to find and that process made the fixes feel more intentional instead of just trial and error.

One thing I would do differently next time when working with AI is relying a little less on ChatGPT when Copilot suggestions didn’t work immediately. I found that sometimes I jumped too quickly to another AI tool instead of first reading the console errors or tracing the code myself.

One thing I noticed is that AI solutions sometimes overcomplicate things or add extra logic that isn’t really necessary. A few of the suggestions technically worked but were harder to understand or put the logic in the wrong place, so I had to simplify them or move the fix somewhere more appropriate. It made me realize that AI suggestions are useful starting points, but they still need to be reviewed and cleaned up so the code actually makes sense.
