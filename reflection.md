# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
<<<<<<< HEAD
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Enter didn't actually submit the guess
  2. it took forever for the guess box to load
  3. Attempts are off and so it didn't update the first time (technically should have 8 attempts as written in the sidebar, but the UI displays that I have 7 attempts so it didn't decrement until 2 attmepts later)
  4. New game resets the attempts but doesn't actually start a new game (You already won. Start a new game to play again. is still there)
  5. When I do a guess, untoggle Show hint, and then retoggle it the hint no longer shows up and it takes another attempt for it to show up
  6. Buggy hints? don't know what the number is but it tells me to go lower when i type in 100 and higher when i say 99, must be changing the secret number or had the wrong hints. The secret number was 15, told me 99 was too low and 100 was too high how weird is that?
  7. When I run out of all attempts and game is over and I click "New Game" it just keeps flashing me that game is over and to start a new game which is so sus
  
=======
  (for example: "the hints were backwards").
>>>>>>> d28145213e029bd9f9244f5f8071e0985a5e266e

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
