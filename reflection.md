# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. The higher/lower hints were swapped. Guessing too high still said "Go HIGHER!" and guessing too low said "Go LOWER!", sending the player in the wrong direction.
  2. The number ranges were inconsistent. `get_range_for_difficulty` sets different ranges per difficulty (e.g., Easy: 1–20, Hard: 1–50), but the UI always displays "Guess a number between 1 and 100." The ranges themselves also don't make sense since Hard (1–50) is a smaller range than Normal (1–100), making it easier instead of harder.
  3. The game accepted out-of-bound guesses without any validation or warning.
  4. Normal difficulty allowed the most attempts (8), while Easy only allowed 6, which is counterintuitive.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used Claude Code as my AI teammate throughout this project. One correct suggestion it made was identifying that the higher/lower hints in `check_guess` were swapped. When the guess was too high, the game said "Go HIGHER!" instead of "Go LOWER!", and vice versa. I verified this by reading the original code and confirming the logic was backwards, and then by running pytest cases that assert the hint message contains "LOWER" when the guess is above the secret and "HIGHER" when below.

  One suggestion that was initially incomplete was when Claude Code helped polish my reflection notes for bug #2. It summarized the issue as just the difficulty ranges being illogical (Hard having a smaller range than Easy), but missed the other half of the bug: the UI always hardcodes "Guess a number between 1 and 100" regardless of the actual range set by `get_range_for_difficulty`. I caught this by re-reading `app.py` and pointed it out, and Claude Code then updated the description to cover both problems.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I decided a bug was fixed by writing targeted pytest cases and running them against the updated code. For the swapped hints bug, Claude Code generated two tests: `test_too_high_hint_says_lower` and `test_too_low_hint_says_higher`, which verify the hint message contains the correct direction. For the difficulty ranges bug, Claude Code generated `test_difficulty_ranges_scale_with_difficulty`, which asserts that Easy < Normal < Hard upper bounds, and `test_easy_range_is_not_trivial`, which checks that Easy's range is at least 1-50. All four tests passed after the fixes, confirming the logic works as expected. Claude Code helped design these tests. I asked it to generate pytest cases targeting each bug, and it wrote tests that would have failed against the original buggy code.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
